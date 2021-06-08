import mysql.connector
from mysql.connector import Error
from config import host_name, user_name, user_password, database_name

def create_table(table_name):
    connection = mysql.connector.connect(host=host_name,
                                        user=user_name,
                                        password=user_password)
    database_cursor = connection.cursor()
    try:
        create_database_query = "CREATE DATABASE IF NOT EXISTS "+ database_name
        database_cursor.execute(create_database_query)
    except Error as e:
        # print('Error occured ::',e)
        pass
    try:
        database_cursor.execute('USE '+database_name)
        create_table_query = 'CREATE TABLE IF NOT EXISTS Table_'+ table_name+' (Customer_Name varchar(255) not null, Customer_Id varchar(18) not null, Open_Date date not null, Last_Consulted_Date date, Vaccination_Id char(5), Dr_Name char(255), State char(5), Post_Code int(5), Country char(5), DOB date, Is_Active char(1), PRIMARY KEY(Customer_Name), CHECK ( Post_Code BETWEEN 10000 AND 99999))'
        database_cursor.execute(create_table_query)
        database_cursor.execute('create table mi like table_usa')
    except Error as e:
        # print('Erro occured::', e)
        pass

    return connection, database_cursor
