import mariadb 
import sys

# Connect to MariaDB Platform

try:
    conn = mariadb.connect(
        user="cermob_dev_joao",
        password="^P!y4nh41hhd",
        host="192.168.0.53",
        port=45150,
        database="design"
    )

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get cursor

cur = conn.cursor()