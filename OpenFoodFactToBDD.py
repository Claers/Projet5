import pymysql
import json
import openfoodfacts

connection = pymysql.connect(host='localhost',
                             user='OpenFoodUser',
                             password='OpenPass',
                             db='OpenFoodDB',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)  # Used to connect to the database

# Initialisation
i = 1
products = []

try:
    while (i <= 400):
        # Use the OpenFoodFacts Python API to get a page of the product list in France
        products = openfoodfacts.products.get_by_country("France", i)
        # Use the OpenFoodFacts Python API to get a page of the product list in La Réunion
        products += openfoodfacts.products.get_by_country("Réunion", i)
        i += 1
        with connection.cursor() as cursor:
            # SQL request to register a Product
            sqlProduct = "INSERT INTO Products (product_name,shops,brands,product_url,nutriscore) SELECT %s,%s,%s,%s,%s WHERE NOT EXISTS(SELECT * FROM Products WHERE product_name = %s);"
            for product in products:
                try:
                    if(product['states_hierarchy'][1] == "en:complete") and (product['stores'] != None) and (len(product['nutrition_grades']) < 2):
                        for category in product['categories'].split(","):
                            # SQL request to register a Categorie
                            sqlCategory = "INSERT INTO Categories (category_name) SELECT %s WHERE NOT EXISTS(SELECT * FROM Categories WHERE category_name = %s);"
                            cursor.execute(sqlCategory, (category, category))
                        cursor.execute(sqlProduct, (product['product_name'], product['brands'], product[
                                       'stores'], product['url'], product['nutrition_grades'], product['product_name']))
                except KeyError:
                    continue
            connection.commit()  # Send to database

        with connection.cursor() as cursor:
            for product in products:
                try:
                    if(product['states_hierarchy'][1] == "en:complete") and (product['stores'] != None):
                        for category in product['categories'].split(","):
                            # SQL request to fill the product_category table.
                            # This link the productid and the categoryid into the table.
                            sql = "INSERT INTO product_category (product,category) SELECT productid,categoryid FROM Products, Categories WHERE (product_name = %s) AND (category_name = %s);"
                            cursor.execute(
                                sql, (product['product_name'], category))
                except KeyError:
                    continue

            connection.commit()  # Send to database

        products = []  # Reset the product list
finally:
    connection.close()
