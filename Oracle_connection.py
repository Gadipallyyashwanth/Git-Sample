import oracledb

# Connect to the database
connection = oracledb.connect(
    user="myoracle",
    password="9704",
    dsn="localhost:1521/xe"  
)
print ( " Connection successfull with sql developer")

cursor = connection.cursor()
#updating a row in the column in product.
update_query =  """ 
                   update product set PNAME = 'MY WORLD'
                   WHERE PCODE = 1
                  """
cursor.execute(update_query)
print("\n Row updated successfully!")
connection.commit()

#Deleting a row from register 
Delete_query = """
                   Delete from  system.register where regno = 10002
                """                    
print("\n Row deleted successfully")                      
connection.commit()

# Create a cursor and execute a query
print("\n register TABLE")
cursor.execute("SELECT * FROM system.register")
for row in cursor:
    print(row)

print("\n product TABLE")
cursor.execute("SELECT * FROM product")
for row in cursor:
    print(row)
    
print("\n employees TABLE")
cursor.execute("SELECT * FROM system.employees")
for row in cursor:
    print(row)

cursor.close()
connection.close()