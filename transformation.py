import json
from models import Author

# Завантаження даних з authors.json
with open('authors.json', 'r', encoding='utf-8') as file:
    authors_data = json.load(file)

# Збереження даних у колекції authors
for author_data in authors_data:
    author = Author(**author_data)
    author.save()
