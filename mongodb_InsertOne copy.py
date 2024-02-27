from pymongo import MongoClient

#Use Cluster0
client = MongoClient("mongodb+srv://asamant:Spring2024@cluster0.oovet.mongodb.net/?retryWrites=true&w=majority")
db = client.HardwareSet


people = db.HWSet2
import datetime
personDocument = {
  "Description": "Document for HW2",
  "Capacity": 1000,
  "Availability": 1000,
  }
 
people.insert_one(personDocument)
