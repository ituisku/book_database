import sys

def books_to_list(file):
    books_list = []
    try:
        with open(file, 'r') as file:
            for line in file:
                name, writer, isbn, year = line.split('/')
                books_list.append({
                    'name': name,
                    'writer': writer,
                    'isbn': isbn,
                    'year': int(year)
                    })
    except ValueError:
        print("Error: Incorrect data format in the file. Each line must contain 'name/writer/isbn/year'.")
        sys.exit(1)
    except FileNotFoundError:
        print(f"File {file} not found. If you decide to add books, a new database with the given filename is created.")
    return books_list

def sort_books(books_list):
    return sorted(books_list, key=lambda x: x['year'])

def print_books(books_list):
    if len(books_list) == 0:
        print("\nNo books in the database.\n")
    else:
        print("\nCurrent database content in ascending order by publishing year:\n")
        for book in sort_books(books_list):
            print(f"{book['name']}, written by {book['writer']}, ISBN: {book['isbn']}, published in {book['year']}")
        print("\n")

def add_book(books_list):
    name = input("Enter the name of the book: ")
    writer = input("Enter name of the writer: ")
    isbn = get_isbn_from_user()
    year = get_publishing_year_from_user()
    new_book = {'name': name, 'writer': writer, 'isbn': isbn, 'year': year}
    print(f"\nNew book to be added:\n{name}, written by {writer}, ISBN: {isbn}, published in {year}")
    update = input("Do you want to add this book to the database? (y/n): ")
    if update.lower() == 'y':
        books_list.append(new_book)
        save_books(filename, books_list)
        print("\nBook saved to database successfully.\n")
    else:
        print("\nReturning to main menu.\n")

def get_isbn_from_user():
    while True:
        isbn = input("Enter ISBN: ")
        if len(isbn) == 13 and isbn.isdigit():
            return isbn
        else:
            print("Invalid ISBN. Please enter a 13-digit number.")

def get_publishing_year_from_user():
    while True:
        year = input("Enter publishing year: ")
        if year.isdigit() and int(year) > 0 and int(year) <= 2025:
            return int(year)
        else:
            print("Invalid year. Only positive numbers are accepted.")

def save_books(file, books_list):
    if len(books_list) == 0:
        print("No books to save.")
    else:
        with open(file, 'w') as file:
            for book in sort_books(books_list):
                file.write(f"{book['name']}/{book['writer']}/{book['isbn']}/{book['year']}\n")

if __name__ == '__main__':
    filename = sys.argv[1]
    books_list = books_to_list(filename)
    while True:
        print("1) Add new book")
        print("2) Print current database content in ascending order by publishing year")
        print("Q) Exit the program")
        choice = input("Please choose one of the options above: ")
        if choice == '1':
            add_book(books_list)
        elif choice == '2':
            print_books(books_list)
        elif choice.lower() == 'q':
            print("Exiting the program.")
            break
        else:
            print("\nInvalid option, please choose one of the given options (Q to exit).\n")