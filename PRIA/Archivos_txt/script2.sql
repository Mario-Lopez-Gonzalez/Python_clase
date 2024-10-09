ALTER TABLE products ADD CONSTRAINT FK_product_category_id
FOREIGN KEY(category_id) REFERENCES categories(category_id)
ON DELETE SET NULL
ON UPDATE CASCADE;

ALTER TABLE products ADD CONSTRAINT FK_product_provider_id
FOREIGN KEY(provider_id) REFERENCES providers(provider_id)
ON DELETE SET NULL
ON UPDATE CASCADE;

ALTER TABLE addresses ADD CONSTRAINT FK_addresses_person_id
FOREIGN KEY(person_id) REFERENCES people(person_id)
ON DELETE CASCADE
ON UPDATE CASCADE;

ALTER TABLE payment_information ADD CONSTRAINT FK_payment_information_person_id
FOREIGN KEY(person_id) REFERENCES people(person_id)
ON DELETE CASCADE
ON UPDATE CASCADE;

ALTER TABLE order_product ADD CONSTRAINT FK_order_product_order_id
FOREIGN KEY(order_id) REFERENCES orders(order_id)
ON DELETE CASCADE
ON UPDATE CASCADE;

ALTER TABLE order_product ADD CONSTRAINT FK_order_product_product_id
FOREIGN KEY(product_id) REFERENCES products(product_id)
ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE orders ADD CONSTRAINT FK_orders_person_id
FOREIGN KEY(person_id) REFERENCES people(person_id)
ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE orders ADD CONSTRAINT FK_orders_billing_address_id
FOREIGN KEY(billing_address) REFERENCES addresses(address_id)
ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE orders ADD CONSTRAINT FK_orders_delivery_address_id
FOREIGN KEY(delivery_address) REFERENCES addresses(address_id)
ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE accesses ADD CONSTRAINT FK_accesses_person_id 
FOREIGN KEY(person_id) REFERENCES people(person_id)
ON DELETE SET NULL
ON UPDATE CASCADE;

ALTER TABLE accesses ADD CONSTRAINT FK_accesses_page_id
FOREIGN KEY(page_id) REFERENCES web_pages(page_id)
ON DELETE CASCADE
ON UPDATE CASCADE;

ALTER TABLE carts ADD CONSTRAINT FK_carts_person_id 
FOREIGN KEY(person_id) REFERENCES people(person_id)
ON DELETE CASCADE
ON UPDATE CASCADE; 

ALTER TABLE cart_product ADD CONSTRAINT FK_cart_product_cart_id
FOREIGN KEY(cart_id) REFERENCES carts(cart_id)
ON DELETE CASCADE
ON UPDATE CASCADE;

ALTER TABLE cart_product ADD CONSTRAINT FK_cart_product_product_id
FOREIGN KEY(product_id) REFERENCES products(product_id)
ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE invoices ADD CONSTRAINT FK_invoices_order_id
FOREIGN KEY(order_id) REFERENCES orders(order_id)
ON DELETE RESTRICT
ON UPDATE RESTRICT;