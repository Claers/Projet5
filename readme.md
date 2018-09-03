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

Put % before to have a response with everything before your word
Put % after to have a response with everything after your word
Put % after and before to have a response with everything around your word 

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
		>> "db.product("Coca Cola Cherry")"
		>> Id : 1632 | Nom du produit : Coca Cola Cherry | Categorie : Boissons
		>> Id : 1632 | Nom du produit : Coca Cola Cherry | Categorie : Boissons gazeuses
		>> Id : 1632 | Nom du produit : Coca Cola Cherry | Categorie : Sodas
		>> Id : 1632 | Nom du produit : Coca Cola Cherry | Categorie : Sodas au cola
		>> Id : 1632 | Nom du produit : Coca Cola Cherry | Categorie : Boissons sucrées 
		>> db.product("Coca Cola")
		>> Id : 285 | Nom du produit : Coca Cola Light 330ml
		>> Id : 544 | Nom du produit : Coca Cola Zéro Sucre
		>> Id : 567 | Nom du produit : Coca cola saveur framboise zéro sucres
		>> Id : 717 | Nom du produit : Coca Cola
		>> Id : 1632 | Nom du produit : Coca Cola Cherry
		>> Id : 1989 | Nom du produit : Coca Cola original taste
		>> "db.product("1632")"
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

- Get all the categories :

	- Command : 
	```python
	db.categorylist()
	``` 
	or
	```python
	db.categorylist("lastid")
	``` 
	or
	```python
	db.categorylist("startid","number")
	``` 

	- Example :
		```python
		>> db.categorylist()
		>> ...ALL THE CATEGORY LIST...
		>> db.categorylist("2")
		>> Id : 1 | Categorie : en:meals
		>> Id : 2 | Categorie :  en:starters
		>> db.categorylist("20,2")
		>> Id : 21 | Categorie :  en:durum-wheat-pasta
		>> Id : 22 | Categorie :  fr:Serpentini
		```

- Get all the products in a category :

Put % before to have a response with everything before your word
Put % after to have a response with everything after your word
Put % after and before to have a response with everything around your word 

	- Command : 
	```python
	db.product_category("category_name")
	``` 
	or
	```python
	db.product_category("category_id")
	``` 

