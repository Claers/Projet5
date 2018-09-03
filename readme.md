## This is the fifth project of the OpenClassRoom Python formation.

# Dependencies

- Python 3.6.2
- [OpenFoodFact Api for python](https://github.com/openfoodfacts/openfoodfacts-python)
- [PyMySQL 0.9.2](https://github.com/PyMySQL/PyMySQL)

# Table Structure

	## Categories
		categoryid : SMALLINT AUTO_INCREMENT NOT NULL 
		category_name : VARCHAR(80) NOT NULL

	## Products
		productid : SMALLINT AUTO_INCREMENT NOT NULL
		product_name : TEXT NOT NULL
		shops : TEXT NOT NULL
        brands : TEXT NOT NULL
        product_url : TEXT NOT NULL

    ## product_category
    	product : SMALLINT NOT NULL
    	category : SMALLINT NOT NULL

    ## favorites
    	favorite : SMALLINT NOT NULL


Table creation command :
```SQL

CREATE TABLE Categories (
                categoryid SMALLINT AUTO_INCREMENT NOT NULL,
                category_name VARCHAR(80) NOT NULL,
                PRIMARY KEY (categoryid)
)
ENGINE=INNODB;


CREATE TABLE Products (
                productid SMALLINT AUTO_INCREMENT NOT NULL,
                product_name TEXT NOT NULL,
                shops TEXT NOT NULL,
                brands TEXT NOT NULL,
                product_url TEXT NOT NULL,
                PRIMARY KEY (productid)
)
ENGINE=INNODB;


CREATE TABLE product_category (
                product SMALLINT NOT NULL,
                category SMALLINT NOT NULL
)
ENGINE=INNODB;

CREATE TABLE Favorites (
                favorite SMALLINT NOT NULL,
                PRIMARY KEY (favorite)
);


ALTER TABLE product_category ADD CONSTRAINT fk_product
FOREIGN KEY (category)
REFERENCES Categories (categoryid)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE product_category ADD CONSTRAINT fk_category
FOREIGN KEY (product)
REFERENCES Products (productid)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE favorites ADD CONSTRAINT products_favorites_fk
FOREIGN KEY (favorite)
REFERENCES Products (productid)
ON DELETE NO ACTION
ON UPDATE NO ACTION;
```

Table destruction command :
```SQL
DROP TABLE product_category;
DROP TABLE Favorites;
DROP TABLE Categories;
DROP TABLE Products;
```

# Features

- Add to database the OpenFoodFact api responses (Only in a standalone file)

- Create database connection with a object :

	- Command :
		```python
		DataBase("username","password","database","host")
		```

For all commands with "db" before the name we assume that we are using a variable to stock our Database object name "db" :
```python
db = DataBase("username","password","database","host")
```

- Access to a product in database by name or id:
	If for the name search multiple product are found it will shows the found product list and not the product description, you will have to enter exactly the product name to access to the complete description 
	- Command : 
		```python
		db.product("name")
		```
		or
		```python
		db.product("id")
		```

	- Example :
		```python
		>> "db.Product("Coca Cola Cherry")"
		>> Id : 1632 | Nom du produit : Coca Cola Cherry 
		>> "db.Product("1632")"
		>> Id : 1632 | Nom du produit : Coca Cola Cherry
		```

- Get all the products :

	- Command : 
	```python
	db.productlist()
	``` 
	or
	```python
	db.productlist("lastid")
	``` 
	or
	```python
	db.productlist("startid","number")
	``` 

	- Example :
		```python
		>> db.productlist()
		>> ...ALL THE PRODUCT LIST...
		>> db.productlist("2")
		>> Id : 1 | Nom du produit : Taboulé oriental | Marques : Leclerc, Franprix, Magasins U | Magasins : Bonduelle
		>> Id : 2 | Nom du produit : Les 3 Minutes, Coudes Rayés | Marques : Carrefour, Magasins U | Magasins : Panzani,Ebro Foods
		>> db.productlist("20,2")
		>> Id : 21 | Nom du produit : Sel de Guérande | Marques :  | Magasins : Reflets de France
		>> Id : 22 | Nom du produit : Belvita Petit déjeuner brut 5 céréales | Marques : Magasins U | Magasins : LU,Mondelez 
		```


- Get all the products in a category


