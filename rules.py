import re

# Check whether value is string with length less than specified length
def check_varchar(value, length):
    if type(value) == str and len(value) <= length:
            return True
    else:
        return False

# Check whether value is string with length equal to specified length
def check_char(value, length):
    if type(value) == str and len(value) == length:
            return True
    else:
        return False

# Check whether value is string with length equal to specified length
def check_int(value, length):
    if type(value) == int and len(str(value)) == length:
            return True
    else:
        return False

# Check whether value is in YYYYMMDD or DDMMYYYY form
# If reverse is True it will check DDMMYYYY form
def check_date_field(value, reverse):
    if reverse:
        match = re.match("^(0[1-9]|[12][0-9]|3[01])(0[1-9]|1[012])\d{4}$", value)
        return bool(match)
    else:
        match = re.match("^\d{4}(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])$", value)
        return bool(match)

#By using above function it validates the entry
def check_dict(main_dict):
    date_8 = ["Open_Date", "Last_Consulted_Date", "DOB"]
    varchar_255 = ["Customer_Name","Dr_Name"]
    char_5 = ["Vaccination_Id", "State", "Country", "Is_Active"]
    # check manadatory fields
    required_field = ["Customer_Name", "Customer_Id", "Open_Date"]
    for x in required_field:
        if x not in main_dict:
            print("Some required fields are missing for::",x)
            return False
        elif main_dict[x] == "" or main_dict[x] == "-":
            print("Some required fields are missing for::",x)
            return False

    for key, value in main_dict.items():
        if key == "Customer_Id":
            if not check_varchar(value, 18):
                print("error in this field with value::", key, value)
                return False

        elif key == "Post_Code":
            if not check_int(value, 5):
                print("error in this field with value::", key, value)
                return False
        elif key in varchar_255:
            if not check_varchar(value, 255):
                print("error in this field with value::", key, value)
                return False
        elif key in date_8:
            reverse = False
            if key == "DOB":
                reverse = True
            if not check_date_field(value, reverse):
                print("error in this field with value::", key, value)
                return False
        elif key in char_5:
            if not check_char(value, 5):
                print("error in this field with value::", key, value)
                return False
    return True
