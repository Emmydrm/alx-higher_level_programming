-- Script that converts hbtn_0c_0 database to UTF8
-- Convert db 'hbt'
# Convert hbtn_0c_0 database to UTF8
echo "Converting hbtn_0c_0 database to UTF8..."
mysql -e "ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"

# Convert first_table table to UTF8
echo "Converting first_table table to UTF8..."
mysql -e "ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"

# Convert name field in first_table table to UTF8
echo "Converting name field in first_table table to UTF8..."
mysql -e "ALTER TABLE hbtn_0c_0.first_table MODIFY name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
