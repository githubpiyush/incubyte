import re
arr_field = ["Customer_Id", "Customer_Name", "Dr_Name","Open_Date", "Last_Consulted_Date", "DOB",
                "Vaccination_Id", "State", "Country", "Post_Code", "Is_Active"]

def check_varchar(value, length):
    if type(value) == str and len(value) <= length:
            return True
    else:
        return False

def check_char(value, length):
    if type(value) == str and len(value) == length:
            return True
    else:
        return False

def check_int(value, length):
    if type(value) == int and len(str(value)) == length:
            return True
    else:
        return False

def check_required_field(all_field):
    required_field = ["Customer_Name", "Customer_Id", "Open_Date"]
    for x in required_field:
        if x not in all_field:
            return False
    return True

def check_date_field(value):
    match = re.match("^\d{4}(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])$", value)
    return bool(match)
