from mongoengine import Document, StringField, ListField, ReferenceField, connect


connect('Sali', host='mongodb+srv://nedwarov:hetshot53@cluster0.ti0rbne.mongodb.net/<dbname>')

class Author(Document):
    name = StringField(required=True)
    birth_date = StringField()
    birth_place = StringField()
    biography = StringField()

class Quote(Document):
    text = StringField(required=True)
    tags = ListField(StringField())
    author = ReferenceField(Author)
