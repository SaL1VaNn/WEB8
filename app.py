import argparse
import json
from models import *
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from mongoengine import * 
from prod import main2, maker_contacts
from consumer import channel


if __name__ == '__main__':
   
     while  True:
       a= 'enter "4" for start RabbitMQ (id contakt) send to emeil'
       b= 'enter "3" start generate contacts for db '
       menu = input (f' enter "0" for load db from json file\n enter "1" if you want to find quotes by author\n enter "2" if you want to find quotes by tags\n {b}\n {a}\n enter "exit" or "5" to quiet : ')
       
       if menu == 'exit' or menu == '5':
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
                    result = Quotes(tags=quote['tags'], author=Authors.objects.get(fullname=quote['author']),  
                                    quotes=quote['quote'])
                    result.save()
            print ('vse ok')     

       elif menu == "1":
           name =  input('author: ') 
           i = Authors.objects.get( fullname = f"{name}" )
           print (f'{i.description}' )
         
       elif menu == '2' : 
            tags = input('enter tags no spaces separated by commas : ')  
            j =  Quotes.objects.get( tags= f'{tags}' )
            print(f'{j.quotes }' )
       elif menu == '3' : 
           maker_contacts()

       elif menu == '4' : 
           main2()
           channel.start_consuming()
        
       else : print( 'unknown command, try again' )
 
