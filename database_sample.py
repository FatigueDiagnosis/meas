import mysql.connector
from mysql.connector import errorcode
from mysql.connector.constants import ClientFlag
# Obtain connection string information from the portal


cnx = mysql.connector.connect(user="USER", password="PASSWORD", host="HOST", port=3306, database="guest")
cursor = cnx.cursor(buffered=True)

# Drop previous table of same name if one exists
cursor.execute("DROP TABLE IF EXISTS inventory;")
print("Finished dropping table (if existed).")

# Create table
#I'm still considering database layout
cursor.execute("CREATE TABLE inventory (*****);")
print("Finished creating table.")

# Insert some data into table


# Cleanup
cnx.commit()
cursor.close()
cnx.close()
print("Done.")