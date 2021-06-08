I have used python 3.9.5 for this assignment.

  config.py :
    This file contains host name, user name, user password and name of the database.

    table_name contains staging table name.

    create_database_query contains query required to create database.

    create_table_query contains query required to create table with given structure.

    fetch_country_query contains query for fetching all the distinct country from staging table.

    delete_staging_table contains query for deletion of staging table.

  create_table.py:
    This file contains one function named create_stage_table that will create database and staging table using queries written in config file and also return the connection and cursor object of the database.

  Assignmentt.py
    This file contains primary function of this assignment named read_file which needs path of text file (which contains detail information) as argument.
    Functionality of this method is given using comment in every part of the code. 
    It will use create_table and config sripts in order to insert data into staging file followed by insertion of data from staging table into corresponding country tables.
    Uncomment line number 82 in this script if you want to delete staging table. It is good to delete staging table once all operations are done.
