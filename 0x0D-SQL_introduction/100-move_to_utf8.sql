-- Script that converts hbtn_0c_0 database to UTF8
-- Convert db 'hbtn_0c_0'
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Convert table 'first_table'
USE hbtn_0c_0;
ALTER TABLE first_table
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Convert field 'name' in 'first_table'
ALTER TABLE first_table
MODIFY name VARCHAR(256)
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
