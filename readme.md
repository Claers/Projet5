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
                nutriscore VARCHAR(1) NOT NULL,
                PRIMARY KEY (productid)
)
ENGINE=INNODB;


CREATE TABLE product_category (
                product SMALLINT NOT NULL,
                category SMALLINT NOT NULL
)
ENGINE=INNODB;

CREATE TABLE Favorites (
				favoriteid SMALLINT AUTO_INCREMENT NOT NULL,
                favorite SMALLINT NOT NULL,
                productsubid SMALLINT NOT NULL,
                PRIMARY KEY (favoriteid)
)
ENGINE=INNODB;


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

ALTER TABLE favorites ADD CONSTRAINT products_favorites_fk1
FOREIGN KEY (productsubid)
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

All the commands here are accessible in the file : DataBaseOperations.py
All the responses will be in French !

## Database

- Add to database the OpenFoodFact api responses (Only in a standalone file : OpenFoodFactToDBB.py)

- Create database connection with a object :

	- Command :
```python
DataBase("username","password","database","host")
```

For all commands with "db" before the name we assume that we are using a variable to stock our Database object name "db" :
```python
db = DataBase("username","password","database","host")
```

## Products : 
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
		db.product(id)
```

- Example :
```python
>> "db.product("Coca-Cola")"
>> Id : 9 | Nom du produit : Coca-Cola | Catégorie : Beverages | Marques :  | Magasins : Coca-Cola | Url : https://world.openfoodfacts.org/product/5449000000996/coca-cola | Nutriscore : e
>> Id : 9 | Nom du produit : Coca-Cola | Catégorie : Carbonated drinks | Marques :  | Magasins : Coca-Cola | Url : https://world.openfoodfacts.org/product/5449000000996/coca-cola | Nutriscore : e
>> Id : 9 | Nom du produit : Coca-Cola | Catégorie : Sodas | Marques :  | Magasins : Coca-Cola | Url : https://world.openfoodfacts.org/product/5449000000996/coca-cola | Nutriscore : e
>> Id : 9 | Nom du produit : Coca-Cola | Catégorie : Sugared beverages | Marques :  | Magasins : Coca-Cola | Url : https://world.openfoodfacts.org/product/5449000000996/coca-cola | Nutriscore : e
>> Id : 9 | Nom du produit : Coca-Cola | Catégorie : Boissons | Marques :  | Magasins : Coca-Cola | Url : https://world.openfoodfacts.org/product/5449000000996/coca-cola | Nutriscore : e
>> Id : 9 | Nom du produit : Coca-Cola | Catégorie : Boissons gazeuses | Marques :  | Magasins : Coca-Cola | Url : https://world.openfoodfacts.org/product/5449000000996/coca-cola | Nutriscore : e
>> Id : 9 | Nom du produit : Coca-Cola | Catégorie : Boissons sucrées | Marques :  | Magasins : Coca-Cola | Url : https://world.openfoodfacts.org/product/5449000000996/coca-cola | Nutriscore : e
>> Id : 9 | Nom du produit : Coca-Cola | Catégorie : Sodas au cola | Marques :  | Magasins : Coca-Cola | Url : https://world.openfoodfacts.org/product/5449000000996/coca-cola | Nutriscore : e
>> db.product("Coca%")
>> Id : 9 | Nom du produit : Coca-Cola | Nutriscore : e
>> Id : 35 | Nom du produit : Coca Cola Light | Nutriscore : b
>> Id : 74 | Nom du produit : Coca Cola | Nutriscore : e
>> Id : 799 | Nom du produit : Coca Cola Light 330ml | Nutriscore : b
>> Id : 1027 | Nom du produit : Coca Cola Zéro Sucre | Nutriscore : b
>> Id : 1049 | Nom du produit : Coca cola saveur framboise zéro sucres | Nutriscore : b
>> "db.product(9)"
>> Id : 9 | Nom du produit : Coca-Cola | Catégorie : Beverages | Marques :  | Magasins : Coca-Cola | Url : https://world.openfoodfacts.org/product/5449000000996/coca-cola | Nutriscore : e
>> Id : 9 | Nom du produit : Coca-Cola | Catégorie : Carbonated drinks | Marques :  | Magasins : Coca-Cola | Url : https://world.openfoodfacts.org/product/5449000000996/coca-cola | Nutriscore : e
>> Id : 9 | Nom du produit : Coca-Cola | Catégorie : Sodas | Marques :  | Magasins : Coca-Cola | Url : https://world.openfoodfacts.org/product/5449000000996/coca-cola | Nutriscore : e
>> Id : 9 | Nom du produit : Coca-Cola | Catégorie : Sugared beverages | Marques :  | Magasins : Coca-Cola | Url : https://world.openfoodfacts.org/product/5449000000996/coca-cola | Nutriscore : e
>> Id : 9 | Nom du produit : Coca-Cola | Catégorie : Boissons | Marques :  | Magasins : Coca-Cola | Url : https://world.openfoodfacts.org/product/5449000000996/coca-cola | Nutriscore : e
>> Id : 9 | Nom du produit : Coca-Cola | Catégorie : Boissons gazeuses | Marques :  | Magasins : Coca-Cola | Url : https://world.openfoodfacts.org/product/5449000000996/coca-cola | Nutriscore : e
>> Id : 9 | Nom du produit : Coca-Cola | Catégorie : Boissons sucrées | Marques :  | Magasins : Coca-Cola | Url : https://world.openfoodfacts.org/product/5449000000996/coca-cola | Nutriscore : e
>> Id : 9 | Nom du produit : Coca-Cola | Catégorie : Sodas au cola | Marques :  | Magasins : Coca-Cola | Url : https://world.openfoodfacts.org/product/5449000000996/coca-cola | Nutriscore : e
```

- Get all the products :
	- Command : 
```python
db.productlist()
``` 
or
```python
db.productlist(lastid)
``` 
- Example :
```python
>> db.productlist()
>> ...ALL THE PRODUCT LIST...
>> db.productlist(2)
>> Id : 1 | Nom du produit : 16 galettes au Beurre | Marques : Leclerc | Magasins : €co+,Eco+ | Nutriscore : e
>> Id : 2 | Nom du produit : Riz Curcuma Gingembre | Marques : Franprix | Magasins : Alaya,Beendhi | Nutriscore : b
```

## Categories : 
- Get all the categories :
	- Command : 
```python
	db.categorylist()
``` 
or
```python
	db.categorylist(lastid)
```
- Example :
```python
		>> db.categorylist()
		>> ...ALL THE CATEGORY LIST...
		>> db.categorylist(2)
		>> Id : 1 | Categorie : Snacks sucrés
		>> Id : 2 | Categorie : Biscuits et gâteaux
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
	db.product_category(category_id)
``` 

- Access to a category in database by name or id:

Put % before to have a response with everything before your word

Put % after to have a response with everything after your word

Put % after and before to have a response with everything around your word 
	
- Command :

```python
		db.category("name")
```
or
```python
		db.category(id)
```
- Example :
```python
		>> "db.category("Coca-Cola")"
		>> Id : 96 | Nom de la catégorie : Viandes
		>> db.category("%Viandes%")
		>> Id : 31 | Nom de la catégorie : Viandes en conserve
		>> Id : 96 | Nom de la catégorie : Viandes
		>> Id : 414 | Nom de la catégorie : Viandes fraîches
		>> Id : 768 | Nom de la catégorie : Viandes surgelées
		>> Id : 769 | Nom de la catégorie : Viandes hachées
		>> Id : 1170 | Nom de la catégorie : Viandes de porc
		>> Id : 1227 | Nom de la catégorie : Viandes fraîches de bœuf
		>> Id : 1258 | Nom de la catégorie : Poissons et viandes et oeufs
		>> Id : 1334 | Nom de la catégorie : Viandes séchées
		>> Id : 1888 | Nom de la catégorie : Viandes de poulet
		>> "db.category(2)"
		>> Id : 2 | Nom de la catégorie : Biscuits et gâteaux
```

## Favorites :
- Register a product in the favorite table :
	- Command :
```python
	db.add_favorite(productid,substituteid)
```
- Show the favorite table :
	- Command :
```python
	db.show_favorites()
```
- Example :
```python
	>> db.show_favorites()
	>> Id du Favori : 1 | Id du Produit : 25 | Nom du produit : Moutarde de Dijon au Cassis | Produit substitué : 49 | Nom du produit substitué : Moutarde au yuzu
	>> 
	>> Id du Favori : 2 | Id du Produit : 900 | Nom du produit : Nuggets de poulet | Produit substitué : 154 | Nom du produit substitué : Le Haché de Poulet Grillé (2 Portions)
	>> 
	>> Id du Favori : 3 | Id du Produit : 1329 | Nom du produit : Salsa Mexicana Medium | Produit substitué : 1329 | Nom du produit substitué : Salsa Mexicana Medium
	>> 
	>> Id du Favori : 4 | Id du Produit : 130 | Nom du produit : Crousty Chicken l'original | Produit substitué : 154 | Nom du produit substitué : Le Haché de Poulet Grillé (2 Portions)
	>> 
	>> Id du Favori : 5 | Id du Produit : 130 | Nom du produit : Crousty Chicken l'original | Produit substitué : 900 | Nom du produit substitué : Nuggets de poulet
	>> 
	>> Id du Favori : 6 | Id du Produit : 850 | Nom du produit : Cacao Faiblement Dégraissé | Produit substitué : 81 | Nom du produit substitué : Crunch
```

- Remove a product in the favorite table :
	
	- Command :
```python
	db.remove_favorite(productid,substituteid)
```

# Program

To launch the program use program.py. 
The program is redacted in French ! 
The program is structured around 2 functionnalities :
 - The possiblity to search a product easily with the categories and to register him and his substitute in the category selected into the favorite table of the database

 - The possiblity to show the products registred by the user