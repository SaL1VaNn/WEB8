import argparse
import json
from models import Authors, Quotes
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from mongoengine import * 
from prod import main2, maker_contacts
from consumer import channel

uri = "mongodb+srv://topsya1986:topsya1986@cluster0.jyxrtyu.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client.homework8

# db='homework8' 
# connect(
#     db ,
#     host='mongodb+srv://topsya1986:topsya1986@cluster0.jyxrtyu.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp',
#     )

# client = MongoClient("mongodb://localhost:27017")
# db = client.homework8
 
if __name__ == '__main__':
    #  for i in db.authors.find():
    #   print (i)
     while  True:
       a= 'enter "4" for start RabbitMQ (id contakt) send to emeil'
       b= 'enter "3" start generate contacts for db '
       menu = input (f' enter "0" for load db from json file\n enter "1" if you want to find quotes by author\n enter "2" if you want to find quotes by tags\n {b}\n {a}\n enter "exit" to quiet : ')
       
       if menu == 'exit':
           print("Good bye!")
           break
       elif menu == '0':
            with open('authors.json', "r") as f:
                data = json.load(f)
                for author in data:
                    result = Authors(fullname=author['fullname'], born_date=author['born_date'],
                            born_location=author['born_location'], description=author['description'])
                    result.save()

            with open('quotes.json', "r") as f:
                data = json.load(f)
                for quote in data:
                    result = Quotes(tags=quote['tags'], author=quote['author'],
                                    quotes=quote['quote'])
                    result.save()
            print ('vse ok')     

       elif menu == "1":
           name =  input('author: ') 
           for i in db.authors.find({'fullname':  f"{name}" }, { '_id':1,'description': 1, 'author': 1}):
                 print (i)
        #    for name  in db.autors.find( {fullname:  f"{fullname}" }):
        #       print(name)      
       elif menu == '2' : 
            tags = input('enter tags no spaces separated by commas : ')  
            for i in db.quotes.find( {'tags': f'{tags}'}, {'tags': 1, 'quotes': 1},):
                print( i )
       elif menu == '3' : 
           maker_contacts()

       elif menu == '4' : 
           main2()
           channel.start_consuming()
        
       else : print( 'unknown command, try again' )
 