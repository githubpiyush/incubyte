import mysql.connector
from mysql.connector import Error
from config import host_name, user_name, user_password, database_name
from config import create_database_query, create_table_query

def create_stage_table(table_name):
    try:
        # Connection creation with mysql
        connection = mysql.connector.connect(host=host_name,
                                            user=user_name,
                                            password=user_password)
        database_cursor = connection.cursor()

        # DATABASE creation
        database_cursor.execute(create_database_query)
        database_cursor.execute('USE '+database_name)

        # Staging table creation
        database_cursor.execute(create_table_query)
    except Error as e:
        # Uncomment below line in order to see error on console
        # print('Erro occured::', e)
        pass
    # Return the connection and cursor object of database
    return connection, database_cursor
