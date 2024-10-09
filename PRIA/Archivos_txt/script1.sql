DROP SCHEMA IF EXISTS shop;
CREATE SCHEMA shop CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE shop;

DROP TABLE IF EXISTS accesses;
CREATE TABLE accesses (
    access_id INT,
    person_id INT NULL DEFAULT NULL,
    date DATETIME,
    ip VARCHAR(20),
    method VARCHAR(10),
    page_id INT,
    PRIMARY KEY(access_id)
)
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

DROP TABLE IF EXISTS web_pages;
CREATE TABLE web_pages (
    page_id INT,
    path VARCHAR(250),
    PRIMARY KEY(page_id)
)
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

DROP TABLE IF EXISTS carts;
CREATE TABLE carts (
    cart_id INT,
    person_id INT,
    date DATETIME,
    PRIMARY KEY(cart_id)
)
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

DROP TABLE IF EXISTS cart_product;
CREATE TABLE cart_product (
    cart_id INT,
    product_id INT,
    quantity INT,
    PRIMARY KEY(cart_id, product_id)
)
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

DROP TABLE IF EXISTS categories;
CREATE TABLE categories (
    category_id INT,
    name VARCHAR(100),
    PRIMARY KEY(category_id)
)
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

DROP TABLE IF EXISTS invoices;
CREATE TABLE invoices (
    invoice_id INT,
    order_id INT,
    date DATETIME,
    rating INT,
    PRIMARY KEY(invoice_id)
)
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    order_id INT,
    person_id INT,
    date DATETIME,
    billing_address INT,
    delivery_address INT,
    price DECIMAL(18,6),
    PRIMARY KEY(order_id)
)
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

DROP TABLE IF EXISTS order_product;
CREATE TABLE order_product (
    order_id INT,
    product_id INT,
    quantity INT,
    PRIMARY KEY(order_id, product_id)
)
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

DROP TABLE IF EXISTS payment_information;
CREATE TABLE payment_information (
    payment_id INT,
    person_id INT,
    number VARCHAR(30),
    provider VARCHAR(200),
    security_code VARCHAR(10),
    expiration VARCHAR(5),
    PRIMARY KEY(payment_id)
)
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

DROP TABLE IF EXISTS people;
CREATE TABLE people (
    person_id INT,
    birth_date DATETIME,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(150),
    job VARCHAR(100),
    phone VARCHAR(20),
    username VARCHAR(50),
    password VARCHAR(100),
    PRIMARY KEY(person_id)
)
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

DROP TABLE IF EXISTS addresses;
CREATE TABLE addresses (
    address_id INT,
    person_id INT,
    city VARCHAR(30),
    country VARCHAR(20),
    number INT,
    street VARCHAR(100),
    zipcode INT,
    PRIMARY KEY(address_id)
)
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

DROP TABLE IF EXISTS products;
CREATE TABLE products (
    product_id INT,
    category_id INT NULL DEFAULT NULL,
    provider_id INT NULL DEFAULT NULL,
    name VARCHAR(200),
    price DECIMAL(10,4),
    PRIMARY KEY(product_id)
)
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

DROP TABLE IF EXISTS providers;
CREATE TABLE providers (
    provider_id INT,
    name VARCHAR(50),
    email VARCHAR(100),
    webpage VARCHAR(100),
    PRIMARY KEY(provider_id)
)
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

COMMIT;