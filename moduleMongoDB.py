from pymongo import MongoClient
 
def getConnection():
  return MongoClient("mongodb://127.0.0.1:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false")