from models import Author, Quote

def search_quotes(query):
    # Функція для пошуку цитат за запитом query
    query = query.strip()

    if query.startswith("name:"):
        author_name = query.split(":")[1].strip()
        author = Author.objects(name=author_name).first()
        if author:
            quotes = Quote.objects(author=author)
            for quote in quotes:
                print(quote.text)
        else:
            print(f"Автор {author_name} не знайдений.")

    elif query.startswith("tag:"):
        tag = query.split(":")[1].strip()
        quotes = Quote.objects(tags=tag)
        for quote in quotes:
            print(quote.text)

    elif query.startswith("tags:"):
        tags = query.split(":")[1].strip().split(',')
        quotes = Quote.objects(tags__in=tags)
        for quote in quotes:
            print(quote.text)

    elif query == 'exit':
        return False

    else:
        print("Невірний формат запиту. Спробуйте ще раз.")

    return True

while True:
    user_input = input("Введіть команду: ")
    if not search_quotes(user_input):
        break
