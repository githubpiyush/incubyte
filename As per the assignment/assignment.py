from create_table import create_collection_obj
import time
db_name = 'local'
from rules import check_dict

def read_file(filename) :
    y = 0
    temp_list = []
    file_obj = open(filename, "r")
    for x in file_obj :
        y += 1

        x = x.split('|')
        x = x[2:]
        x[len(x) - 1] = x[len(x) - 1].strip('\n')

        if y == 1:
            for index in x :
                temp_list.append(index)
            country_index = temp_list.index('Country')
        else:
            coll_obj = create_collection_obj(db_name ,x[country_index])
            dict_info = {}
            temp_count = 0

            for z in x :
                dict_info[temp_list[temp_count]] = z
                temp_count += 1
            flag_insert = check_dict(dict_info)
            if flag_insert:
                try:
                    last_temp = coll_obj.insert_one(dict_info)
                except:
                    print("Duplicate error")
                    continue
if __name__ == '__main__':
    read_file('sample.txt')
