from create_table import create_table
import re
from mysql.connector import Error

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
            table_name = current_row[country_index]

            DOB = current_row[DOB_index]
            if check_date_format(DOB):
                current_row[DOB_index] = DOB[4:] + DOB[2:4] + DOB[0:2]

            connection, database_cursor = create_table(table_name)
            try:
                insert_table_query = 'INSERT INTO Table_'+ table_name +' ('+column_name_string[:-1]+ ') VALUES '+ str(tuple(current_row))
                database_cursor.execute(insert_table_query)
                connection.commit()
            except Error as e:
                # print('Error occured :: ', e)
                pass
if __name__ == '__main__':
    read_file('sample.txt')
