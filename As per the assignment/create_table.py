import pymongo
from config import mongo_url

def create_collection_obj(db_name, coll_name):
    myclient = pymongo.MongoClient(mongo_url)
    mydb = myclient[db_name]
    mycol = mydb[coll_name]
    mycol.create_index("Customer_Name", unique=True)
    return mycol
