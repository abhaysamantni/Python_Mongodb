import pymongo

#Use Cluster0
client = pymongo.MongoClient("mongodb+srv://asamant:MApeZZu5VcMpD6t3@cluster0.oovet.mongodb.net/?retryWrites=true&w=majority")
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
