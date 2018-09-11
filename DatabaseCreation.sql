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