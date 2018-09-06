import pymysql
import json


class DataBase():

    def __init__(self, username, password, db, host):
        self.connection = pymysql.connect(host=host,
                                          user=username,
                                          password=password,
                                          db=db,
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)  # Used to connect to the database
        self.productsql = None
        self.categorysql = None
        self.productlistsql = None
        self.categorylistsql = None
        self.favoritesql = None
        self.substitutesql = None

    # Close the connection
    def close(self):
        self.connection.close()

    # Get a product in the database.
    # Can use the product id or the product name
    # If the product name return multiple product it will not return a complete product description
    # Else it will return a full description with all the categories.
    def product(self, *args):
        try:
            if(len(args) < 2):  # Accept only 1 argument
                with self.connection.cursor() as cursor:
                    if(type(*args) is int):
                        # SQL query to get a product by id
                        sql = "SELECT DISTINCT productid, product_name,category_name,brands,shops,product_url,nutriscore FROM (SELECT Products.*, Categories.* FROM product_category INNER JOIN Products ON Products.productid = product_category.product INNER JOIN Categories ON Categories.categoryid = product_category.category) AS ProductDesc WHERE productid LIKE %s;"
                        cursor.execute(sql, (args))
                        self.productsql = cursor.fetchall()
                        for product in self.productsql:
                            print("Id : " + str(product['productid']) + " | Nom du produit : " + str(
                                product['product_name']) + " | Catégorie : " + str(product['category_name']) + " | Marques : " + str(product['brands']) + " | Magasins : " + str(product['shops']) + " | Url : " + str(product['product_url']) + " | Nutriscore : " + str(product['nutriscore']))
                        return self.productsql
                    elif(type(*args) is str):
                        # SQL query to get a product by name
                        sql = "SELECT DISTINCT productid, product_name,category_name,brands,shops,product_url,nutriscore FROM (SELECT Products.*, Categories.* FROM product_category INNER JOIN Products ON Products.productid = product_category.product INNER JOIN Categories ON Categories.categoryid = product_category.category) AS ProductDesc WHERE product_name LIKE %s;"
                        cursor.execute(sql, (str(*args)))
                        self.productsql = cursor.fetchall()
                        # Test to check if only one product is found
                        oldproductid = self.productsql[0]['productid']
                        onlyone = True
                        for product in self.productsql:
                            if(oldproductid != product['productid']):
                                onlyone = False
                        if(onlyone):  # If only one product is found, show is full description
                            for product in self.productsql:
                                print("Id : " + str(product['productid']) + " | Nom du produit : " + str(
                                    product['product_name']) + " | Catégorie : " + str(product['category_name']) + " | Marques : " + str(product['brands']) + " | Magasins : " + str(product['shops']) + " | Url : " + str(product['product_url']) + " | Nutriscore : " + str(product['nutriscore']))
                        elif(onlyone == False):  # Else show the list of the products
                            sql = "SELECT DISTINCT productid, product_name, nutriscore FROM (SELECT Products.*, Categories.* FROM product_category INNER JOIN Products ON Products.productid = product_category.product INNER JOIN Categories ON Categories.categoryid = product_category.category) AS ProductDesc WHERE product_name LIKE %s;"
                            cursor.execute(sql, (str(*args)))
                            self.productsql = cursor.fetchall()
                            for product in self.productsql:
                                print(
                                    "Id : " + str(product['productid']) + " | Nom du produit : " + str(product['product_name']) + " | Nutriscore : " + str(product['nutriscore']))
                        return self.productsql
                    elif(type(*args) is not int and type(*args) is not str):
                        raise TypeError
            elif(len(args) >= 2):  # If more of 2 argument is passed, return a error
                raise TypeError

        except TypeError:  # Catch all error to return this message
            print("Bad type argument or too much arguments, only one is accepted. Only non-decimal number accepted or text. Arguments passed :")
            print(args)
            print("Correct syntax : product(\"name\") or product(id)")
            return "Error"

    # Get a category in the database.
    # Can use the category id or the category name
    def category(self, *args):
        try:
            if(len(args) < 2):  # Accept only 1 argument
                with self.connection.cursor() as cursor:
                    if(type(*args) is int):
                        # SQL query to get a category by id
                        sql = "SELECT DISTINCT categoryid, category_name FROM Categories WHERE categoryid LIKE %s;"
                        cursor.execute(sql, (args))
                        self.categorysql = cursor.fetchall()
                        for category in self.categorysql:
                            print("Id : " + str(category['categoryid']) + " | Nom de la catégorie : " + str(
                                category['category_name']))
                        return self.categorysql
                    elif(type(*args) is str):
                        # SQL query to get a category by name
                        sql = "SELECT DISTINCT categoryid, category_name FROM Categories WHERE category_name LIKE %s;"
                        cursor.execute(sql, (str(*args)))
                        self.categorysql = cursor.fetchall()
                        for category in self.categorysql:
                            print("Id : " + str(category['categoryid']) + " | Nom de la catégorie : " + str(
                                category['category_name']))
                        return self.categorysql
                    elif(type(*args) is not int and type(*args) is not str):
                        raise TypeError
            elif(len(args) >= 2):
                raise TypeError

        except TypeError:  # Catch all error to return this message
            print("Bad type argument or too much arguments, only one is accepted. Only non-decimal number accepted or text. Arguments passed :")
            print(args)
            print("Correct syntax : product(\"name\") or product(id)")
            return "Error"

    # Get the product list in the database.
    # Can add a argument to limit the query to a number of product
    def productlist(self, *args):
        try:
            if(len(args) == 0):
                with self.connection.cursor() as cursor:
                    # SQL query to get the product list
                    sql = "SELECT DISTINCT productid,product_name,brands,shops,nutriscore FROM Products"
                    cursor.execute(sql, (args))
                    self.productlistsql = cursor.fetchall()
                    for product in self.productlistsql:
                        print("Id : " + str(product['productid']) + " | Nom du produit : " + str(product[
                              'product_name']) + " | Marques : " + str(product['brands']) + " | Magasins : " + str(product['shops']) + " | Nutriscore : " + str(product['nutriscore']))
                    return self.productlistsql
            elif(type(*args) is int):
                if(len(args) == 1):
                    with self.connection.cursor() as cursor:
                        # SQL query to get the product list with a limit
                        sql = "SELECT DISTINCT productid,product_name,brands,shops,nutriscore FROM Products LIMIT %s"
                        cursor.execute(sql, (args))
                        self.productlistsql = cursor.fetchall()
                        for product in self.productlistsql:
                            print("Id : " + str(product['productid']) + " | Nom du produit : " + str(product[
                                  'product_name']) + " | Marques : " + str(product['brands']) + " | Magasins : " + str(product['shops']) + " | Nutriscore : " + str(product['nutriscore']))
                        return self.productlistsql
                elif(len(args) >= 2):
                    raise TypeError
            elif(type(*args) is not int):
                raise TypeError

        except TypeError:  # Catch all error to return this message
            print(
                "Bad type argument or too much arguments. Only non-decimal number accepted. Arguments passed :")
            print(args)
            print("Correct syntax : productlist() or productlist(lastid)")
            return "Error"

    # Get the category list in the database.
    # Can add a argument to limit the query to a number of category
    def categorylist(self, *args):
        try:
            if(len(args) == 0):
                with self.connection.cursor() as cursor:
                    # SQL query to get the category list
                    sql = "SELECT DISTINCT categoryid,category_name FROM Categories"
                    cursor.execute(sql, (args))
                    self.categorylistsql = cursor.fetchall()
                    for category in self.categorylistsql:
                        print("Id : " + str(category['categoryid']) +
                              " | Categorie : " + str(category['category_name']))
                    return self.categorylistsql
            elif(type(*args) is int):
                if(len(args) == 1):
                    with self.connection.cursor() as cursor:
                        # SQL query to get the category list with a limit
                        sql = "SELECT DISTINCT categoryid,category_name FROM Categories LIMIT %s"
                        cursor.execute(sql, (args))
                        self.categorylistsql = cursor.fetchall()
                        for category in self.categorylistsql:
                            print(
                                "Id : " + str(category['categoryid']) + " | Categorie : " + str(category['category_name']))
                        return self.categorylistsql
                elif(len(args) >= 2):
                    raise Exception
            elif(type(*args) is not int):
                raise TypeError

        except TypeError:  # Catch all error to return this message
            print(
                "Bad type argument or too much arguments. Only non-decimal number accepted. Arguments passed :")
            print(args)
            print("Correct syntax : categorylist() or categorylist(lastid)")
            return "Error"

    # Get the product list that are in the category given in argument.
    # Can use category id or category name
    def product_category(self, *args):
        try:
            if(len(args) < 2):
                with self.connection.cursor() as cursor:
                    if(type(*args) is int):
                        # SQL query to get the product list that are in the
                        # category id given
                        sql = "SELECT DISTINCT productid, product_name,category_name,nutriscore FROM (SELECT Products.*, Categories.* FROM product_category INNER JOIN Products ON Products.productid = product_category.product INNER JOIN Categories ON Categories.categoryid = product_category.category) AS ProductDesc WHERE categoryid LIKE %s;"
                        cursor.execute(sql, (args))
                        self.productsql = cursor.fetchall()
                        for product in self.productsql:
                            print("Id : " + str(product['productid']) + " | Nom du produit : " + str(
                                product['product_name']) + " | Catégorie : " + str(product['category_name']) + " | Nutriscore : " + str(product['nutriscore']))
                        return self.productsql
                    elif(type(*args) is str):
                        # SQL query to get the product list that are in the
                        # category name given
                        sql = "SELECT DISTINCT productid, product_name,category_name FROM (SELECT Products.*, Categories.* FROM product_category INNER JOIN Products ON Products.productid = product_category.product INNER JOIN Categories ON Categories.categoryid = product_category.category) AS ProductDesc WHERE category_name LIKE %s;"
                        cursor.execute(sql, (str(*args)))
                        self.productsql = cursor.fetchall()
                        for product in self.productsql:
                            print("Id : " + str(product['productid']) + " | Nom du produit : " + str(
                                product['product_name']) + " | Catégorie : " + str(product['category_name']))
                        return self.productsql
                    elif(type(*args) is not int and type(*args) is not str):
                        raise TypeError
            elif(len(args) >= 2):
                raise TypeError

        except TypeError:  # Catch all error to return this message
            print("Bad type argument or too much arguments. Only non-decimal number accepted or text. Arguments passed :")
            print(args)
            print("Correct syntax : product_category(\"name\") or product_category(id)")
            return "Error"

    # Add a product in the favorite table
    # Need 2 arguments : the product id and the substistuted product id
    def add_favorite(self, productid, substitutedid):
        try:
            with self.connection.cursor() as cursor:
                if(type(productid) is int):
                        # SQL query to add a product in the favorite table
                    sql = "INSERT INTO Favorites (favorite,productsubid) SELECT %s,%s WHERE NOT EXISTS(SELECT * FROM Favorites WHERE favorite = %s AND productsubid = %s)"
                    cursor.execute(
                        sql, (productid, substitutedid, productid, substitutedid))
                    self.connection.commit()
                elif(type(productid) is not int):
                    raise TypeError

        except TypeError:  # Catch all error to return this message
            print("Bad type argument or too much arguments, only one is accepted. Only non-decimal number accepted. Arguments passed :")
            print(productid)
            print("Correct syntax : add_favorite(id)")

        # Get the favorite list
    def show_favorites(self):
        with self.connection.cursor() as cursor:
                # SQL query to get the favorite list
            sql = "SELECT * FROM Favorites;"
            cursor.execute(sql)
            self.favoritesql = cursor.fetchall()
            for favorite in self.favoritesql:
                # SQL query to get the description of the substitute
                sql = "SELECT DISTINCT productid, product_name,category_name,brands,shops,product_url,nutriscore FROM (SELECT Products.*, Categories.* FROM product_category INNER JOIN Products ON Products.productid = product_category.product INNER JOIN Categories ON Categories.categoryid = product_category.category) AS ProductDesc WHERE productid LIKE %s;"
                cursor.execute(sql, (favorite['favorite']))
                product = cursor.fetchall()
                product = product[0]
                # SQL query to get the description of the substituted product
                sql = "SELECT DISTINCT productid, product_name,category_name,brands,shops,product_url,nutriscore FROM (SELECT Products.*, Categories.* FROM product_category INNER JOIN Products ON Products.productid = product_category.product INNER JOIN Categories ON Categories.categoryid = product_category.category) AS ProductDesc WHERE productid LIKE %s;"
                cursor.execute(sql, (favorite['productsubid']))
                substituteproduct = cursor.fetchall()
                substituteproduct = substituteproduct[0]
                print("Id du Favori : " + str(favorite['favoriteid']) + " | Id du Produit : " + str(favorite['favorite']) + " | Nom du produit : " + str(product[
                      'product_name']) + " | Produit substitué : " + str(favorite['productsubid']) + " | Nom du produit substitué : " + str(substituteproduct['product_name']) + "\n")
            return self.favoritesql

    # Remove a favorite in the list with the favorite id given
    def remove_favorite(self, favoriteid):
        try:
            with self.connection.cursor() as cursor:
                if(type(favoriteid) is int):
                        # SQL query to remove a favorite by the id
                    sql = "DELETE FROM Favorites WHERE favoriteid = %s"
                    cursor.execute(sql, (favoriteid))
                    self.connection.commit()
                elif(type(favoriteid) is not int):
                    raise TypeError

        except TypeError:  # Catch all error to return this message
            print("Bad type argument or too much arguments, only one is accepted. Only non-decimal number accepted. Arguments passed :")
            print(productid)
            print("Correct syntax : remove_favorite(id)")

    # Find a substitue of a product in a category with the nutriscore
    def substitute(self, category, productid):
        with self.connection.cursor() as cursor:
                # SQL query to get a substitute
            sql = "SELECT DISTINCT productid,product_name,category_name,categoryid,brands,shops,product_url,nutriscore FROM (SELECT Products.*, Categories.* FROM product_category INNER JOIN Products ON Products.productid = product_category.product INNER JOIN Categories ON Categories.categoryid = product_category.category) AS ProductDesc WHERE categoryid LIKE %s ORDER BY nutriscore ASC LIMIT 1;"
            cursor.execute(sql, (category))
            self.substitutesql = cursor.fetchall()
            self.substitutesql = self.substitutesql[0]
            # If the substitute id is the same that the product id given return
            # that this product is the best
            if(productid == self.substitutesql['productid']):
                return "Best"
            else:
                print("\nSubstitut trouvé : Id : " + str(self.substitutesql['productid']) + " | Nom du produit : " + str(
                    self.substitutesql['product_name']) + " | Catégorie : " + str(self.substitutesql['category_name']) + " | Marques : " + str(self.substitutesql['brands']) + " | Magasins : " + str(self.substitutesql['shops']) + " | Url : " + str(self.substitutesql['product_url']) + " | Nutriscore : " + str(self.substitutesql['nutriscore']))
                return self.substitutesql
