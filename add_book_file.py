def add_book(book):
    title = input('enter book title : ')

    author_name = ()
    while True:
        print('how many authors : ')
        num = input()
        try:
            num = int(num)
            if(num<1):
                print('number must be at least 1.')
                continue
            elif(num==1):
                name = input('enter author name : ')
                author_name=(name)
            else:
                for i in range(num):
                    name = input('enter author name : ')
                    author_name+=(name,)
            break
        except ValueError:
            print('Invalid input. Please enter a valid number of authors.')
            # return
        

    isbn = input('enter ISBN : ')


    
    while True:
        publish = input('enter publishing year : ')
        try:
            publish = int(publish)
            break
        except ValueError:
            print('Invalid input. Please enter a valid publish year.')


    
    while True:
        price = input('enter price : ')
        try:
            price = float(price)
            break
        except ValueError:
            print("Invalid input. Please enter a valid price.")



    
    while True:
        quantity = input('enter quantity of this book : ')
        try:
            quantity=int(quantity)
            break
        except ValueError:
            print('Invalid input. Please enter a valid number of quantity.')


    new_book = {
        "title": title,
        "author_name": author_name,
        "isbn" : isbn,
        "publish" : publish,
        "price" : price,
        "quantity" : quantity
    }
    # book.append(new_book)
    print('book added successfully')

    # append to books.csv file after creating every book
    with open("books.csv", "at") as fp:
        line = f"{new_book['title']},{new_book['author_name']},{new_book['isbn']},{new_book['publish']},{new_book['price']},{new_book['quantity']}\n"
        fp.write(line)

    # return book
