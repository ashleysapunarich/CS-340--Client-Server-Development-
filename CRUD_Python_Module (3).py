# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password, host='localhost', port=27017, db='aac', collection='animals'):
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'aacuser' 
        PASS = 'password' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://aacuser:password@localhost:27017/aac') 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data: dict) -> bool:
        if data:
            try:
                result = self.collection.insert_one(data)
                return result.acknowledged
            except Exception as e:
                print(f"Create operation failed: {e}")
                return False
        else:
            raise ValueError("Nothing to save, because data parameter is empty")


    # Create method to implement the R in CRUD.

    def read(self, searchData: dict = {}) -> list:
        try:
            cursor = self.collection.find(searchData, {"_id": False})
            return list(cursor)
        except Exception as e:
            print(f"Read operation failed: {e}")
            return []


    
    #  Create method to implement the U in CRUD 
    
    def update(self, query: dict, update_values: dict, multiple: bool = False) -> int:
        try:
            if multiple:
                result = self.collection.update_many(query, {'$set': update_values})
            else:
                result = self.collection.update_one(query, {'$set': update_values})
            return result.modified_count
        except Exception as e:
            print(f"Update operation failed: {e}")
            return 0

        
    # Create method to implement the D in CRUD   

    def delete(self, query: dict, multiple: bool = False) -> int:
        try:
            if multiple:
                result = self.collection.delete_many(query)
            else:
                result = self.collection.delete_one(query)
            return result.deleted_count
        except Exception as e:
            print(f"Delete operation failed: {e}")
            return 0
