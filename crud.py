 import mysql.connector  # Import the MySQL connector module

# Connect to the database
mysqldb = mysql.connector.connect(
    host="localhost",        # Hostname
    user="root",             # Username
    database="crud",         # Database name
    password=""              # Password (empty in this case)
)
print("connected")  # Print a message confirming the connection

# Create a cursor object to interact with the database
sur = mysqldb.cursor()

# Create the class11 table if it doesn't exist
sur.execute("CREATE TABLE IF NOT EXISTS class11(rollno INT,name VARCHAR(255),class INT )")
print("table created")  # Print a message confirming table creation

# Insert a record into the class11 table
sur = mysqldb.cursor()
sur.execute("INSERT INTO class11 (rollno, name, class) VALUES (1, 'Lucky', 11)")
mysqldb.commit()  # Commit the transaction
print("done")  # Print a message confirming the insertion

# Retrieve the record from the class11 table where rollno equals 1
sur = mysqldb.cursor()
sur.execute("SELECT * FROM class11 WHERE rollno =1")
result = sur.fetchall()  # Fetch all matching rows
for i in result:
    print(i)  # Print each row

# Update the record in the class11 table where rollno equals 4
sur = mysqldb.cursor()
sur.execute("UPDATE class11 SET name ='deepak' WHERE rollno=4")
mysqldb.commit()  # Commit the transaction
print("updated")  # Print a message confirming the update

# Drop the class10 table if it exists
sur = mysqldb.cursor()
sur.execute("DROP TABLE class10")
print("delete")  # Print a message confirming the deletion
mysqldb.commit()  # Commit the transaction

# Close the database connection
mysqldb.close()
