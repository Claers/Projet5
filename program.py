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
        self.productlistsql = None
        self.categorylistsql = None

    def product(self, *args):
        try:
            if(len(args) < 2):
                with self.connection.cursor() as cursor:
                    if(type(*args) is int):
                        sql = "SELECT DISTINCT productid, product_name,category_name FROM (SELECT Products.*, Categories.* FROM product_category INNER JOIN Products ON Products.productid = product_category.product INNER JOIN Categories ON Categories.categoryid = product_category.category) AS ProductDesc WHERE product_name LIKE %s;"
                        cursor.execute(sql, (args))
                        self.productsql = cursor.fetchall()
                        self.productsql = self.productsql[0]
                        print("Id : " + str(self.productsql['productid']) + " | Nom du produit : " + str(
                            self.productsql['product_name']) + " | Catégorie : " + str(self.productsql['category_name']))
                    elif(type(*args) is str):
                        sql = "SELECT DISTINCT productid, product_name FROM (SELECT Products.*, Categories.* FROM product_category INNER JOIN Products ON Products.productid = product_category.product INNER JOIN Categories ON Categories.categoryid = product_category.category) AS ProductDesc WHERE product_name LIKE %s;"
                        cursor.execute(sql, (str(*args)))
                        self.productsql = cursor.fetchall()
                        if((len(self.productsql)) == 1):
                            sql = "SELECT DISTINCT productid, product_name,category_name FROM (SELECT Products.*, Categories.* FROM product_category INNER JOIN Products ON Products.productid = product_category.product INNER JOIN Categories ON Categories.categoryid = product_category.category) AS ProductDesc WHERE product_name LIKE %s;"
                            cursor.execute(sql, ("%" + str(*args) + "%"))
                            self.productsql = cursor.fetchall()
                            for product in self.productsql:
                                print("Id : " + str(product['productid']) + " | Nom du produit : " + str(
                                    product['product_name']) + " | Categorie : " + str(product['category_name']))
                        elif((len(self.productsql)) > 1):
                            for product in self.productsql:
                                print(
                                    "Id : " + str(product['productid']) + " | Nom du produit : " + str(product['product_name']))
                    elif(type(*args) is not int and type(*args) is not str):
                    	raise TypeError
            elif(len(args) >= 2):
                raise TypeError

        except TypeError:
            print("Bad type argument or too much arguments, only one is accepted. Only non-decimal number accepted or text. Arguments passed :")
            print(args)
            print("Correct syntax : product(\"name\") or product(id)")

    def productlist(self, *args):
        try:
            if(type(*args) is int):
                if(len(args) == 0):
                    with self.connection.cursor() as cursor:
                        sql = "SELECT DISTINCT productid,product_name,brands,shops FROM Products"
                        cursor.execute(sql, (args))
                        self.productlistsql = cursor.fetchall()
                        for product in self.productlistsql:
                            print("Id : " + str(product['productid']) + " | Nom du produit : " + str(product[
                                  'product_name']) + " | Marques : " + str(product['brands']) + " | Magasins : " + str(product['shops']))
                if(len(args) == 1):
                    with self.connection.cursor() as cursor:
                        sql = "SELECT DISTINCT productid,product_name,brands,shops FROM Products LIMIT %s"
                        cursor.execute(sql, (args))
                        self.productlistsql = cursor.fetchall()
                        for product in self.productlistsql:
                            print("Id : " + str(product['productid']) + " | Nom du produit : " + str(product[
                                  'product_name']) + " | Marques : " + str(product['brands']) + " | Magasins : " + str(product['shops']))

                elif(len(args) == 2):
                    with self.connection.cursor() as cursor:
                        sql = "SELECT DISTINCT productid,product_name,brands,shops FROM Products LIMIT %s,%s"
                        cursor.execute(sql, (args[0], args[1]))
                        self.productlistsql = cursor.fetchall()
                        for product in self.productlistsql:
                            print("Id : " + str(product['productid']) + " | Nom du produit : " + str(product[
                                  'product_name']) + " | Marques : " + str(product['brands']) + " | Magasins : " + str(product['shops']))
                elif(len(args) >= 3):
                    raise TypeError
            elif(type(*args) is not int):
                    raise TypeError

        except TypeError:
            print("Bad type argument or too much arguments. Only non-decimal number accepted. Arguments passed :")
            print(args)
            print("Correct syntax : productlist() or productlist(lastid) or productlist(startid, number)")

    def categorylist(self, *args):
        try:
            if(type(*args) is int):
                if(len(args) == 0):
                    with self.connection.cursor() as cursor:
                        sql = "SELECT DISTINCT categoryid,category_name FROM Categories"
                        cursor.execute(sql, (args))
                        self.categorylistsql = cursor.fetchall()
                        for category in self.categorylistsql:
                            print("Id : " + str(category['categoryid']) + " | Categorie : " + str(category['category_name']))
                if(len(args) == 1):
                    with self.connection.cursor() as cursor:
                        sql = "SELECT DISTINCT categoryid,category_name FROM Categories LIMIT %s"
                        cursor.execute(sql, (args))
                        self.categorylistsql = cursor.fetchall()
                        for category in self.categorylistsql:
                            print("Id : " + str(category['categoryid']) + " | Categorie : " + str(category['category_name']))
                elif(len(args) == 2):
                    with self.connection.cursor() as cursor:
                        sql = "SELECT DISTINCT categoryid,category_name FROM Categories LIMIT %s,%s"
                        cursor.execute(sql, (args[0], args[1]))
                        self.categorylistsql = cursor.fetchall()
                        for category in self.categorylistsql:
                            print("Id : " + str(category['categoryid']) + " | Categorie : " + str(category['category_name']))
                elif(len(args) >= 3):
                    raise Exception
            elif(type(*args) is not int):
                raise TypeError

        except TypeError:
            print("Bad type argument or too much arguments. Only non-decimal number accepted. Arguments passed :")
            print(args)
            print("Correct syntax : categorylist() or categorylist(lastid) or categorylist(startid, number)")

    def product_category(self, *args):
        try:
            if(len(args) < 2):
                with self.connection.cursor() as cursor:
                    if(type(*args) is int):
                        sql = "SELECT DISTINCT productid, product_name,category_name FROM (SELECT Products.*, Categories.* FROM product_category INNER JOIN Products ON Products.productid = product_category.product INNER JOIN Categories ON Categories.categoryid = product_category.category) AS ProductDesc WHERE category_name LIKE %s;"
                        cursor.execute(sql, (args))
                        self.productsql = cursor.fetchall()
                        self.productsql = self.productsql[0]
                        print("Id : " + str(self.productsql['productid']) + " | Nom du produit : " + str(
                            self.productsql['product_name']) + " | Catégorie : " + str(self.productsql['category_name']))
                    elif(type(*args) is str):
                        sql = "SELECT DISTINCT productid, product_name,category_name FROM (SELECT Products.*, Categories.* FROM product_category INNER JOIN Products ON Products.productid = product_category.product INNER JOIN Categories ON Categories.categoryid = product_category.category) AS ProductDesc WHERE category_name LIKE %s;"
                        cursor.execute(sql, (str(*args)))
                        self.productsql = cursor.fetchall()
                        for product in self.productsql:
                            print("Id : " + str(product['productid']) + " | Nom du produit : " + str(
                                product['product_name']) + " | Catégorie : " + str(product['category_name']))
                    elif(type(*args) is not int and type(*args) is not str):
                    	raise TypeError
            elif(len(args) >= 2):
                raise TypeError

        except TypeError:
            print("Bad type argument or too much arguments. Only non-decimal number accepted or text. Arguments passed :")
            print(args)
            print("Correct syntax : product_category(\"name\") or product_category(id)")


    def add_favorite(self, productid):
        try:
        	with self.connection.cursor() as cursor:
        		if(type(productid) is int):
        			sql = "INSERT INTO Favorites (favorite) SELECT %s WHERE NOT EXISTS(SELECT * FROM Favorites WHERE favorite = %s)"
        			cursor.execute(sql,(productid,productid))
        			self.connection.commit()
        		elif(type(productid) is not int):
        			raise TypeError

        except TypeError:
            print("Bad type argument or too much arguments, only one is accepted. Only non-decimal number accepted. Arguments passed :")
            print(productid)
            print("Correct syntax : add_favorite(id)")


    def show_favorites(self):
    	with self.connection.cursor() as cursor:
    		sql = "SELECT DISTINCT productid,product_name,brands,shops FROM (SELECT Products.*, product_category.* FROM favorites INNER JOIN Products ON Products.productid = Favorites.favorite INNER JOIN product_category ON product_category.product = Favorites.favorite) AS FavoriteProductDesc;"
    		cursor.execute(sql)
    		self.favoritesql = cursor.fetchall()
    		for favorite in self.favoritesql:
    			print("Id : " + str(favorite['productid']) + " | Produit : " + str(favorite['product_name']) + " | Marques : " + str(favorite['brands'])+ " | Magasins : " + str(favorite['shops']))


    def remove_favorite(self, productid):
        try:
        	with self.connection.cursor() as cursor:
        		if(type(productid) is int):
        			sql = "DELETE FROM Favorites WHERE favorite = %s"
        			cursor.execute(sql,(productid))
        			self.connection.commit()
        		elif(type(productid) is not int):
        			raise TypeError

        except TypeError:
            print("Bad type argument or too much arguments, only one is accepted. Only non-decimal number accepted. Arguments passed :")
            print(productid)
            print("Correct syntax : remove_favorite(id)")

    def close(self):
        self.connection.close()


class App():

    def __init__():
        pass


if __name__ == '__main__':
    db = DataBase("OpenFoodUser", "OpenPass", "OpenFoodDB", "localhost")
    db.remove_favorite(10)
    db.show_favorites()
    db.close()
