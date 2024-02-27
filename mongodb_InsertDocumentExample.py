from pymongo import MongoClient

#Use Cluster0
client = MongoClient("mongodb+srv://asamant:Spring2024@cluster0.oovet.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

#Use Cluster2
#client = MongoClient("mongodb+srv://asamant:APADSu2023@cluster2.oovet.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


db = client.gettingStartedSu24
people = db.people
import datetime
personDocument = {
  "name": { "first": "Abhay", "last": "Samant" },
  "birth": datetime.datetime(2014, 6, 23),
  "contribs": [ "Vet", "Photographer", "Friend" ],
  "views": 5000}
 
people.insert_one(personDocument)
