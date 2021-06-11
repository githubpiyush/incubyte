from config import host_name, user_name, user_password
from config import database_name, table_name
from config import create_database_query, create_table_query
from config import fetch_country_query, delete_staging_table

import re, sys
import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.database_name = database_name
        self.table_name = table_name
        self.create_database_query = create_database_query
        self.create_table_query = create_table_query
        self.fetch_country_query = fetch_country_query
        self.delete_staging_table = delete_staging_table

    def create_stage_table(self, table_name):
        try:
            # Connection creation with mysql
            connection = mysql.connector.connect(host=self.host_name,
                                                user=self.user_name,
                                                password=self.user_password)
            database_cursor = connection.cursor()

            # DATABASE creation
            database_cursor.execute(self.create_database_query)
            database_cursor.execute('USE '+self.database_name)

            # Staging table creation
            database_cursor.execute(self.create_table_query)
        except Error as e:
            # Uncomment below line in order to see error on console
            # print('Erro occured::', e)
            pass
        # Return the connection and cursor object of database
        return connection, database_cursor

    # This function will return True if DOB is in DDMMYYYY format
    def check_date_format(self,DOB):
        match = re.match("^(0[1-9]|[12][0-9]|3[01])(0[1-9]|1[012])\d{4}$", DOB)
        return bool(match)

    def read_file(self, filename) :

        # Initialize variables in order to read the file and iterate over it
        line_counter = 0
        column_name_list = []
        column_name_string = ""
        try:
            file_object = open(filename, "r")
        except Exception as e:
            print('File not found')
            sys.exit()

        # Start the iteration process with file object
        for current_row in file_object :
            line_counter += 1

            # Split the current row by '|'
            # Remove some unnecessary port from both ends
            current_row = current_row.split('|')
            current_row = current_row[2:]
            current_row[len(current_row) - 1] = current_row[len(current_row) - 1].strip('\n')

            if line_counter == 1:
                # Store coulmn information from first line into variables
                for index in current_row :
                    column_name_list.append(index)
                    column_name_string = column_name_string + index + ","
                # Store DOB index inorder to check date format later
                DOB_index = column_name_list.index('DOB')

            else:
                # This part will iterate from 2nd to last line of the file

                # Extract DOB using DOB index and check the format
                DOB = current_row[DOB_index]
                # If date format is not YYYYMMDD then correct the format
                if self.check_date_format(DOB):
                    current_row[DOB_index] = DOB[4:] + DOB[2:4] + DOB[0:2]

                # Create connection and cursor object of staging table
                connection, database_cursor = self.create_stage_table(self.table_name)
                try:
                    # Insert current row into staging table and commit into DB
                    insert_table_query = 'INSERT INTO '+ table_name +' ('+column_name_string[:-1]+ ') VALUES '+ str(tuple(current_row))
                    database_cursor.execute(insert_table_query)
                    connection.commit()
                except Error as e:
                    # Uncomment below line in order to see error on console
                    # print('Error occured :: ', e)
                    pass

        # Fetch distinct country from staging table
        database_cursor.execute(self.fetch_country_query)
        result = database_cursor.fetchall()
        # Interate over distinct country
        for new_table in result:
            try:
                # Create country table if it does not exists
                # Transfer related data from staging table
                create_country_table = 'create table IF NOT EXISTS Table_'+new_table[0]+' like '+table_name
                transfer_data_query = 'INSERT INTO Table_'+new_table[0]+' SELECT * FROM '+table_name+' WHERE Country="'+new_table[0]+'"'

                database_cursor.execute(create_country_table)
                database_cursor.execute(transfer_data_query)
                connection.commit()
            except Error as e:
                # Uncomment below line in order to see error on console
                # print("Error occured ::", e)
                pass
        # Uncomment below line to delete staging table after execution
        # database_cursor.execute(self.delete_staging_table)

if __name__ == '__main__':
    d = Database()
    d.read_file('sample.txt')
