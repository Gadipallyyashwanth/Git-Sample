#import pandas as pd
import psycopg2
from datetime import datetime
#import xml.etree.ElementTree as ET
#import os



# Create a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="Techprojects@yash"
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a SQL query
cursor.execute("select * FROM emp01 order by emp_id ")

# Fetch all the rows from the query result
rows = cursor.fetchall()

# Loop through the rows and print the data
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()