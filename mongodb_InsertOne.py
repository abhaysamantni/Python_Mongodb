from pymongo import MongoClient

#Use Cluster0
client = MongoClient("mongodb+srv://asamant:Bhai0226@cluster0.oovet.mongodb.net/?retryWrites=true&w=majority")
db = client.test


people = db.people3
import datetime
personDocument = {
  "name": { "first": "Ishika", "last": "Samant" },
  "birth": datetime.datetime(1912, 6, 23),
  "death": datetime.datetime(2030,10,15),
  "contribs": [ "Engineer", "Teacher", "Friend" ],
  "views": 250}
 
people.insert_one(personDocument)
