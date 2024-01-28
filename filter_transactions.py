import json
import psycopg2
from psycopg2 import sql

# import json object from test.json
with open('test.json') as json_file:
    json_data = json.load(json_file)

# parse json_data for keys in the first transaction
first_transaction = json_data[0]
key_variables = []

for key in first_transaction:
    key_variables.append(key)

# Create the CREATE TABLE query
query = sql.SQL("CREATE TABLE all_transactions ({})").format(
    sql.SQL(', ').join(sql.SQL("{} text").format(sql.Identifier(column)) for column in key_variables)
)

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="192.168.0.9",
    database="budget_boys",
    user="python",
    password="python"
)

cursor = conn.cursor()

# Execute the query
cursor.execute(query)

# Insert the data into the table
for transaction in json_data:
    values = [transaction[column] for column in key_variables]
    cursor.execute(
        sql.SQL("INSERT INTO all_transactions ({}) VALUES ({})").format(
            sql.SQL(', ').join(sql.Identifier(column) for column in key_variables),
            sql.SQL(', ').join(sql.Placeholder() for column in key_variables)
        ),
        values
    )

# Commit the changes and close the connection
conn.commit()
cursor.close()
conn.close()
