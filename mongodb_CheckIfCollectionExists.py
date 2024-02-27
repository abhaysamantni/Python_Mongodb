import pymongo

myclient = pymongo.MongoClient("mongodb+srv://asamant:Spring2024@cluster0.oovet.mongodb.net/?retryWrites=true&w=majority")
mydb = myclient.mydatabase

mycol = mydb.customers

collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")
else:  
  print("The collection does not exist.")