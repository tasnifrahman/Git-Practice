import re

def search_book():
    search_term = input("Enter input for your search: ")
    with open('books.csv', 'r') as file:
        for line in file:

            fields = re.split(r',(?![^(]*\))', line.strip())

            title = fields[0].strip()
            authors_list = fields[1].strip()

            # Clean up the authors list to remove parentheses and single quotes
            authors_list = authors_list.strip('()').replace("'", "")
            authors = tuple(authors_list.split(','))
            
            
            
            isbn = fields[2]
            publish = fields[3]
            price = fields[4]
            quantity = fields[5]
            
            # search logic
            if (search_term.lower() in title.lower() or any(search_term.lower() in author.lower() for author in authors) or search_term == isbn):
                print(f"title : {title}, authors : {authors_list}, ISBN : {isbn}, Publishing Year : {publish}, Price : {price}, Quanity : {quantity}\n")
