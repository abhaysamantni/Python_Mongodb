import pymongo
import ssl
#Use Cluster0

client = pymongo.MongoClient("mongodb+srv://asamant:Spring2024@cluster0.oovet.mongodb.net/?retryWrites=true&w=majority")




db = client.gettingStartedSp24
people = db.people
import datetime
personDocument = {
  "name": { "first": "Abhay", "last": "Samant" },
  "birth": datetime.datetime(1912, 6, 23),
  "contribs": [ "Engineer", "Teacher", "Friend" ],
 "views": 255}
 
people.insert_one(personDocument)
myquery={"name.first":"Ishika"}
x=people.find_one(myquery)
print(x)
if(x['name']=={'first': 'Abhay', 'last': 'Samant'}):
    print("Name found\n")
else:
    print("Name not found\n")
   