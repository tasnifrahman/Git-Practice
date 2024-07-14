def remove_book():
    title_to_remove = input("Enter title of the book for remove : ")
    with open('books.csv', 'r') as file:
        lines = file.readlines()
    rows = lines[0:]

    book_found = False
    
    matching_books = []
    for row in rows:
        columns = row.split(',')
        title = columns[0].strip()
        if title.lower() == title_to_remove.lower():
            matching_books.append(row)

    if not matching_books:
        print("Book not found.")
        return


    print(f"Found {len(matching_books)} book(s) with the title '{title_to_remove}':")
    for i, book in enumerate(matching_books, start=1):
        print(f"{i}. {book.strip()}")

    
    while True:
        try:
            choice = int(input("Enter the index number of the book you want to delete: "))
            if 1 <= choice <= len(matching_books):
                break
            else:
                print("Invalid choice. Please choose a valid index number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    book_to_delete = matching_books[choice - 1]
    remaining_rows = [row for row in rows if row != book_to_delete]

    # Write the remaining rows back to the file
    with open('books.csv', 'w') as file:
        file.writelines(remaining_rows)
    
    print("Book removed successfully.")