from create_table import create_stage_table
import re
from mysql.connector import Error
from config import table_name
from config import fetch_country_query, delete_staging_table

def check_date_format(DOB):
    match = re.match("^(0[1-9]|[12][0-9]|3[01])(0[1-9]|1[012])\d{4}$", DOB)
    return bool(match)

def read_file(filename) :

    line_counter = 0
    column_name_list = []
    file_object = open(filename, "r")
    column_name_string = ""

    for current_row in file_object :
        line_counter += 1

        current_row = current_row.split('|')
        current_row = current_row[2:]
        current_row[len(current_row) - 1] = current_row[len(current_row) - 1].strip('\n')

        if line_counter == 1:
            for index in current_row :
                column_name_list.append(index)
                column_name_string = column_name_string + index + ","

            country_index = column_name_list.index('Country')
            DOB_index = column_name_list.index('DOB')

        else:
            DOB = current_row[DOB_index]
            if check_date_format(DOB):
                current_row[DOB_index] = DOB[4:] + DOB[2:4] + DOB[0:2]

            connection, database_cursor = create_stage_table(table_name)
            try:
                insert_table_query = 'INSERT INTO '+ table_name +' ('+column_name_string[:-1]+ ') VALUES '+ str(tuple(current_row))
                database_cursor.execute(insert_table_query)
                connection.commit()
            except Error as e:
                # print('Error occured :: ', e)
                pass

    database_cursor.execute(fetch_country_query)
    result = database_cursor.fetchall()

    for new_table in result:
        try:
            create_country_table = 'create table IF NOT EXISTS Table_'+new_table[0]+' like '+table_name
            transfer_data_query = 'INSERT INTO Table_'+new_table[0]+' SELECT * FROM '+table_name+' WHERE Country="'+new_table[0]+'"'

            database_cursor.execute(create_country_table)
            database_cursor.execute(transfer_data_query)
            connection.commit()
        except Error as e:
            print("Error occured ::", e)
            pass
    # Uncomment below line to delete staging table after execution
    # database_cursor.execute(delete_staging_table)

if __name__ == '__main__':
    read_file('sample.txt')
