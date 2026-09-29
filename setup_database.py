
import sqlite3

# Create the orders database
conn = sqlite3.connect("orders.db")
cur = conn.cursor()

# Create customers table
cur.execute("DROP TABLE IF EXISTS orders")
cur.execute("DROP TABLE IF EXISTS customers")

cur.execute("""
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
)
""")

# Create orders table
cur.execute("""
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount REAL,
    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
)
""")

# Insert six customers
customers = [
    (1, "Ali", "Islamabad"),
    (2, "Sara", "Lahore"),
    (3, "Bilal", "Karachi"),
    (4, "Ayesha", "Islamabad"),
    (5, "Ahmed", "Lahore"),
    (6, "Zara", "Peshawar")
]

cur.executemany(
    "INSERT INTO customers VALUES (?, ?, ?)",
    customers
)

# Insert ten orders
orders = [
    (1, 1, 4500),
    (2, 1, 7200),
    (3, 2, 6000),
    (4, 2, 5800),
    (5, 3, 3000),
    (6, 3, 6800),
    (7, 4, 5000),
    (8, 5, 4200),
    (9, 5, 7000),
    (10, 6, 2500)
]

cur.executemany(
    "INSERT INTO orders VALUES (?, ?, ?)",
    orders
)

conn.commit()
conn.close()

print("Orders database created successfully.")