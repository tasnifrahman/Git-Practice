import add_book_file
import view_all_book_file
import search_book_file
import remove_book_file



book = []



print("Welcome!")

menu_text = """
Your options:
1. Add new Book
2. View All Books
3. Search Contacts
4. Remove Book
5. Update Contact
6. Backup Contact
7. Restore Contact
0. Exit
"""

while True:
    print(menu_text)
    choice = input("Enter your choice: ")

    if choice == "1":
        book = add_book_file.add_book(book)
    elif choice == "2":
        view_all_book_file.view_all_book()
    elif choice == "3":
        search_book_file.search_book()
    elif choice == "4":
        remove_book_file.remove_book()
    # elif choice == "5":
    #     # update_contact()
    # elif choice == "6":
    #     # backup_contact()
    # elif choice == "7":
    #     # restore_contact()
    elif choice == "0":
        print("Thanks for using the application.")
        break
    else:
        print("Wrong Choice!")




