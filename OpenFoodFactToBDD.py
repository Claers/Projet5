import pymysql
import json
import openfoodfacts

connection = pymysql.connect(host='localhost',
                             user='OpenFoodUser',
                             password='OpenPass',
                             db='OpenFoodDB',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

i=1
products = []


while (i<=500):
	products += openfoodfacts.products.get_by_country("France",i)
	i+=1

try:
	with connection.cursor() as cursor:
		sqlProduct = "INSERT INTO Products (product_name,shops,brands,product_url) SELECT %s,%s,%s,%s WHERE NOT EXISTS(SELECT * FROM Products WHERE product_name = %s);"
		for product in products:
			try:
				if(product['states_hierarchy'][1] == "en:complete") and (product['stores'] != None):
					for category in product['categories'].split(","):
						sqlCategory = "INSERT INTO Categories (category_name) SELECT %s WHERE NOT EXISTS(SELECT * FROM Categories WHERE category_name = %s);"
						cursor.execute(sqlCategory,(category,category))
					cursor.execute(sqlProduct,(product['product_name'],product['brands'],product['stores'],product['url'],product['product_name']))
			except KeyError:
				continue

		connection.commit()

	with connection.cursor() as cursor:
		for product in products:
			try:
				if(product['states_hierarchy'][1] == "en:complete") and (product['stores'] != None):
					for category in product['categories'].split(","):
						sql = "INSERT INTO product_category (product,category) SELECT productid,categoryid FROM Products, Categories WHERE (product_name = %s) AND (category_name = %s);"
						cursor.execute(sql,(product['product_name'],category))
			except KeyError:
				continue

		connection.commit()

finally:
	connection.close()