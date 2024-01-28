import psycopg2
from psycopg2 import sql

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="192.168.0.9",
    database="budget_boys",
    user="python",
    password="python"
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Example: Query data
cursor.execute('SELECT * FROM all_transactions')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()
