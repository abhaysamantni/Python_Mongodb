import pymongo

#Use Cluster0
client = pymongo.MongoClient("mongodb+srv://asamant:EE461LSp23@cluster0.oovet.mongodb.net/?retryWrites=true&w=majority")


print("List of databases before deletion\n--------------------------")
for x in client.list_database_names():
  print(x)

#pick one of the databases for deletion. In this case, it is zhc94 
db = client.zc5785

status=client.drop_database(db)

print(status)