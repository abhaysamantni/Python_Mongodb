import pymongo

#Use Cluster0
client = pymongo.MongoClient("mongodb+srv://asamant:Spring2024@cluster0.oovet.mongodb.net/?retryWrites=true&w=majority")


print("List of databases before deletion\n--------------------------")
for x in client.Users.list_collection_names():
  print(x)
  status=client.Users.drop_collection(x)
  #print(status)

#pick one of the databases for deletion. In this case, it is zhc94 


#status=client.Users.drop_collection('yuvrajkhullar')


print(status)