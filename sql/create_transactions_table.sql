CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    amount DECIMAL(10, 2) NOT NULL,
    transaction_date DATE NOT NULL,
    sub_category_id INT,
    FOREIGN KEY (sub_category_id) REFERENCES sub_categories(sub_category_id)
);
