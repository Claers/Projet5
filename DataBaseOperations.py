import pymysql
import json

class DataBase():

    def __init__(self, username, password, db, host):
        self.connection = pymysql.connect(host=host,
                                          user=username,
                                          password=password,
                                          db=db,
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)
        self.productsql = None
        self.categorysql = None
        self.productlistsql = None
        self.categorylistsql = None
        self.favoritesql = None
        self.substitutesql = None

    
    def close(self):
        self.connection.close()

    def product(self, *args):
        try:
            if(len(args) < 2):
                with self.connection.cursor() as cursor:
                    if(type(*args) is int):
                        sql = "SELECT DISTINCT productid, product_name,category_name,brands,shops,product_url,nutriscore FROM (SELECT Products.*, Categories.* FROM product_category INNER JOIN Products ON Products.productid = product_category.product INNER JOIN Categories ON Categories.categoryid = product_category.category) AS ProductDesc WHERE productid LIKE %s;"
                        cursor.execute(sql, (args))
                        self.productsql = cursor.fetchall()
                        for product in self.productsql:
                            print("Id : " + str(product['productid']) + " | Nom du produit : " + str(
                                product['product_name']) + " | Catégorie : " + str(product['category_name']) + " | Marques : " + str(product['brands'])+ " | Magasins : " + str(product['shops']) + " | Url : " + str(product['product_url']) + " | Nutriscore : " + str(product['nutriscore']))
                        return self.productsql
                    elif(type(*args) is str):
                        sql = "SELECT DISTINCT productid, product_name,category_name,brands,shops,product_url,nutriscore FROM (SELECT Products.*, Categories.* FROM product_category INNER JOIN Products ON Products.productid = product_category.product INNER JOIN Categories ON Categories.categoryid = product_category.category) AS ProductDesc WHERE product_name LIKE %s;"
                        cursor.execute(sql, (str(*args)))
                        self.productsql = cursor.fetchall()
                        oldproductid = self.productsql[0]['productid']
                        onlyone = True
                        for product in self.productsql:
                            if(oldproductid != product['productid']):
                                onlyone = False
                        if(onlyone):
                            for product in self.productsql:
                                print("Id : " + str(product['productid']) + " | Nom du produit : " + str(
                            product['product_name']) + " | Catégorie : " + str(product['category_name']) + " | Marques : " + str(product['brands'])+ " | Magasins : " + str(product['shops']) + " | Url : " + str(product['product_url']) + " | Nutriscore : " + str(product['nutriscore']))
                        elif(onlyone == False):
                            sql = "SELECT DISTINCT productid, product_name, nutriscore FROM (SELECT Products.*, Categories.* FROM product_category INNER JOIN Products ON Products.productid = product_category.product INNER JOIN Categories ON Categories.categoryid = product_category.category) AS ProductDesc WHERE product_name LIKE %s;"
                            cursor.execute(sql, (str(*args)))
                            self.productsql = cursor.fetchall()
                            for product in self.productsql:
                                print(
                                    "Id : " + str(product['productid']) + " | Nom du produit : " + str(product['product_name']) + " | Nutriscore : " + str(product['nutriscore']))
                        return self.productsql
                    elif(type(*args) is not int and type(*args) is not str):
                        raise TypeError
            elif(len(args) >= 2):
                raise TypeError

        except TypeError:
            print("Bad type argument or too much arguments, only one is accepted. Only non-decimal number accepted or text. Arguments passed :")
            print(args)
            print("Correct syntax : product(\"name\") or product(id)")
            return "Error"
