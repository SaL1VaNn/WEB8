from mongoengine import *
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi 

connect(
    db='homework8',
    host='mongodb+srv://nedwarov:<password>@cluster0.ti0rbne.mongodb.net/',
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


      