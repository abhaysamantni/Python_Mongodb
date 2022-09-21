import pymongo
import ssl
#Use Cluster0

client = pymongo.MongoClient("mongodb+srv://asamant:<password>@cluster0.oovet.mongodb.net/?retryWrites=true&w=majority")




db = client.gettingStartedSp22
people = db.people3
import datetime
personDocument = {
  "name": { "first": "Abhay", "last": "Samant" },
  "birth": datetime.datetime(1912, 6, 23),
  "death": datetime.datetime(2030,10,15),
  "contribs": [ "Engineer", "Teacher", "Friend" ],
 "views": 250}
 
people.insert_one(personDocument)
myquery={"name.first":"Ishika"}
x=people.find_one(myquery)
print(x)
if(x==None):
    print("Name not found\n")
else:
    print("Name found\n")
   