-- Creating the parent_categories table without the computed amount column
CREATE TABLE parent_categories (
    parent_category_id SERIAL PRIMARY KEY,
    parent_category_name VARCHAR(255) NOT NULL,
    description TEXT
);

-- Creating the sub_categories table without the computed amount column
CREATE TABLE sub_categories (
    sub_category_id SERIAL PRIMARY KEY,
    sub_category_name VARCHAR(255) NOT NULL,
    parent_category_id INT
);

-- Creating the transactions table
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    amount DECIMAL(10, 2) NOT NULL,
    transaction_date DATE NOT NULL,
    sub_category_id INT,
    FOREIGN KEY (sub_category_id) REFERENCES sub_categories(sub_category_id)
);

-- Inserting sample data into parent_categories
INSERT INTO parent_categories (parent_category_name, description)
VALUES ('Bills', 'Rent, Housing, Insurance expenses, ect.');

-- Inserting sample data into sub_categories
INSERT INTO sub_categories (sub_category_name, parent_category_id)
VALUES 
('Rent', 1),
('Car Insurance', 1),
('Internet', 1); 

-- Inserting sample data into transactions
INSERT INTO transactions (amount, transaction_date, sub_category_id) VALUES
(1705.25, '2024-01-21', 1),
(65.00, '2024-01-22', 2),
(31.00, '2024-01-23', 3);

