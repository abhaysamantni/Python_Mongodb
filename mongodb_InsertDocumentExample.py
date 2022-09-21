from pymongo import MongoClient

#Use Cluster0
client = MongoClient("mongodb+srv://asamant:jgaP0PINkADCHqRX@cluster0.oovet.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

#Use Cluster2
#client = MongoClient("mongodb+srv://asamant:sbP6JpRe4N6HNclJ@cluster2.oovet.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


db = client.gettingStartedSp22
people = db.people3
import datetime
personDocument = {
  "name": { "first": "Ally", "last": "Samant" },
  "birth": datetime.datetime(1912, 6, 23),
  "death": datetime.datetime(2030,10,15),
  "contribs": [ "Engineer", "Teacher", "Friend" ],
 "views": 250}
 
people.insert_one(personDocument)
