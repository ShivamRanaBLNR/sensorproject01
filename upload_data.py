# t5his code reads the data set and upload it in mongodb

from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
uri="mongodb+srv://shivamrana:shivamrana@cluster0.w0dek.mongodb.net/?retryWrites=true&w=majority"

#create new client and connect to server
client = MongoClient(uri)
#create databaser name and collection name
DATABASE_NAME="shivamrana"
COLLECTION_NAME='waferfault'
df=pd.read_csv("C:\Users\STUDENT\Downloads\sensorproject\notebooks\wafer_23012020_041211.csv")
df=df.drop("Unnamed: 0",axis=1)
#Converting to json
json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)