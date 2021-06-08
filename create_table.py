import mysql.connector
from mysql.connector import Error
from config import host_name, user_name, user_password, database_name
from config import create_database_query, create_table_query

def create_stage_table(table_name):
    try:
        connection = mysql.connector.connect(host=host_name,
                                            user=user_name,
                                            password=user_password)
        database_cursor = connection.cursor()

        database_cursor.execute(create_database_query)
        database_cursor.execute('USE '+database_name)

        database_cursor.execute(create_table_query)
    except Error as e:
        # print('Erro occured::', e)
        pass

    return connection, database_cursor
