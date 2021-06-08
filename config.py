host_name = 'localhost'
user_name = 'root'
user_password = 'Pass@123'
database_name = 'incubyte'
table_name = 'staging_table'

create_database_query = "CREATE DATABASE IF NOT EXISTS "+ database_name
create_table_query = 'CREATE TABLE IF NOT EXISTS '+ table_name+' (Customer_Name varchar(255) not null, Customer_Id varchar(18) not null, Open_Date date not null, Last_Consulted_Date date, Vaccination_Id char(5), Dr_Name char(255), State char(5), Post_Code int(5), Country char(5), DOB date, Is_Active char(1), PRIMARY KEY(Customer_Name), CHECK ( Post_Code BETWEEN 10000 AND 99999))'

fetch_country_query = 'select distinct Country from '+ table_name
delete_staging_table = 'DROP TABLE '+table_name
