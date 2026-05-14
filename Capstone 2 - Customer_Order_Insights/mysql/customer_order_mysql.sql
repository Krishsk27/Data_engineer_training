CREATE DATABASE supply_chain;
USE supply_chain;
CREATE TABLE suppliers (
    supplier_id INT PRIMARY KEY AUTO_INCREMENT,
    supplier_name VARCHAR(100),
    contact_email VARCHAR(100),
    city VARCHAR(50)
);
CREATE TABLE inventory (
    inventory_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100),
    stock_quantity INT,
    reorder_level INT,
    supplier_id INT,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100),
    quantity INT,
    order_date DATE,
    delivery_date DATE,
    supplier_id INT,
    status VARCHAR(50),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);
INSERT INTO suppliers(supplier_name, contact_email, city)
VALUES
('ABC Suppliers', 'abc@gmail.com', 'Chennai'),
('Global Traders', 'global@gmail.com', 'Bangalore');
INSERT INTO inventory(product_name, stock_quantity, reorder_level, supplier_id)
VALUES
('Laptop', 10, 5, 1),
('Mouse', 50, 20, 2);
INSERT INTO orders(product_name, quantity, order_date, delivery_date, supplier_id, status)
VALUES
('Laptop', 2, '2026-05-10', '2026-05-14', 1, 'Delivered'),
('Mouse', 5, '2026-05-12', '2026-05-18', 2, 'Pending');
SELECT * FROM orders;

UPDATE inventory
SET stock_quantity = 15
WHERE inventory_id = 1;
DELETE FROM orders
WHERE order_id = 2;
DELIMITER //

CREATE PROCEDURE CheckReorder()
BEGIN
    SELECT product_name, stock_quantity
    FROM inventory
    WHERE stock_quantity < reorder_level;
END //

DELIMITER ;
CALL CheckReorder();
