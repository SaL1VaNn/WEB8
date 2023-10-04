from mongoengine import *
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi 

# uri = "mongodb+srv://topsya1986:topsya1986@cluster0.jyxrtyu.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"
# client = MongoClient(uri, server_api=ServerApi('1'))
# db = client.homework8

connect(
    db='homework8',
    host='mongodb+srv://topsya1986:topsya1986@cluster0.jyxrtyu.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp',
    )


 

class Authors(Document):
    fullname = StringField()
    born_date = StringField( )
    born_location = StringField( )
    description = StringField( )


class Quotes(Document):
    tags = ListField( )
    author =  ReferenceField (Authors)
    quotes = StringField ( )
    
class Contact(Document):
    fullname = StringField()
    email = EmailField()
    done = BooleanField(default=False)


      