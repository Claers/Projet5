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

- Access to a product in database by name : 
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
		```

- 

