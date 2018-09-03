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
		product_name : VARCHAR(80) NOT NULL
		shops : TEXT NOT NULL
        brands : TEXT NOT NULL
        product_url : TEXT NOT NULL

    ## product_category
    	product : SMALLINT NOT NULL
    	category : SMALLINT NOT NULL

Table creation command :
``SQL
CREATE TABLE Categories (
                categoryid SMALLINT AUTO_INCREMENT NOT NULL,
                category_name VARCHAR(80) NOT NULL,
                PRIMARY KEY (categoryid)
)
ENGINE=INNODB;
CREATE TABLE Products (
                productid SMALLINT AUTO_INCREMENT NOT NULL,
                product_name VARCHAR(80) NOT NULL,
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
``

Table destruction command :
``SQL
DROP TABLE product_category;
DROP TABLE Categories;
DROP TABLE Products;
``

# Features

- Add to database the OpenFoodFact api responses (Only in a standalone file)

- Access to a product in database by name : 
	- Command : 
		``python
			Product("name")
		``
		or
		``python
			Product("id")
		``

	- Return example :
		``python
			"Name : "
		``

- 

