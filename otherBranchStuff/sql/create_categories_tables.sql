-- Creating the parent_categories table with the computed amount column
CREATE TABLE parent_categories (
    parent_category_id SERIAL PRIMARY KEY,
    parent_category_name VARCHAR(255) NOT NULL,
    description TEXT,
    amount DECIMAL(10, 2) GENERATED ALWAYS AS (
        COALESCE((SELECT SUM(amount) FROM transactions WHERE transactions.sub_category_id IN
                   (SELECT sub_category_id FROM sub_categories WHERE sub_categories.parent_category_id = parent_categories.parent_category_id)), 0)
    )
);

-- Creating the sub_categories table with the computed amount column
CREATE TABLE sub_categories (
    sub_category_id SERIAL PRIMARY KEY,
    sub_category_name VARCHAR(255) NOT NULL,
    parent_category_id INT,
    FOREIGN KEY (parent_category_id) REFERENCES parent_categories(parent_category_id),
    amount DECIMAL(10, 2) GENERATED ALWAYS AS (
        COALESCE((SELECT SUM(amount) FROM transactions WHERE transactions.sub_category_id = sub_categories.sub_category_id), 0)
    )
);

