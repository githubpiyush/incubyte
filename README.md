I have used python 3.9.5 for this assignment.

There were some conflicts in the datatype given in the table and the sample file. SO I have given you two folders which has almost same scripts with slight changes which I thought is correct.

Common things:
  config.py :
      This will have two variable one is mongo_url and another one is db_name.
      As the name suggest please put mongoDB url and database name.
  create_table.py:
    This file will create collection for country and will make name primary key.

  As per assignment folder:
    rules.py:
      As per datatype and constraints I have created all the functions.
      "Customer_Name" and "Dr_Name" will have this type:
      VARCHAR (255) : Variable length string with 250 max length.

      "Vaccination_Id", "State", "Country", "Is_Active" will have this:
      CHAR (5) : String with fixed length 5

      "Open_Date", "Last_Consulted_Date", "DOB" will have this type:
      Date(8) : DOB will have DDMMYYYY format and other two will have YYYYMMDD format. If you put reverse = False in line 66 and 64 of rules.py then all dates should be on YYYYMMDD format.

      "Customer_Id" will have VARCHAR(18) datatype.

      "Post_Code" will have int(5) datatype with fixed length of 5.
    assignment.py:
      Use read_file function and pass the sample file path in order to have all the right entry in our database.



      As per sample file:
        rules.py:
          As per datatype and constraints I have created all the functions.
          "Customer_Name" and "Dr_Name" will have this type:
          VARCHAR (255) : Variable length string with 250 max length.

          "Vaccination_Id", "State", "Country", "Is_Active" will have this:
          CHAR (5) : String with max length 5

          "Open_Date", "Last_Consulted_Date", "DOB" will have this type:
          Date(8) : DOB will have DDMMYYYY format and other two will have YYYYMMDD format. If you put reverse = False in line 66 and 64 of rules.py then all dates should be on YYYYMMDD format.

          "Customer_Id" will have VARCHAR(18) datatype.

          "Post_Code" will have int(5) datatype with fixed length of 5.
        Assignmentt.py:
          Use read_file function and pass the sample file path in order to have all the right entry in our database.

  So in order to run my code you have to import read_file function from assignment script and pass the path of sample file.

  I have not used TDD function but I have created the assignment in a functional way so that you can import and check any function.
  I have added comment where I feel it's necessary.

  If you find any difficulties please let me know.
