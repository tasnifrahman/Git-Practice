def view_all_book():
    with open("books.csv", "rt") as fp:
        for line in fp:
            b = line.strip().split(",")
            print(b[0], b[1], b[2], b[3], b[4], b[5])
            # print(
            #     b["title"],
            #     b["author_name"],
            #     b["isbn"],
            #     b["publish"],
            #     b["price"],
            #     b["quantity"],
            #     sep=" -=> ",
            # )
