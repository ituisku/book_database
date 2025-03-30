# Book Database

## Running the Program

1. Download the `book_database` directory
2. Install Python
3. Navigate to the `book_database` directory in your IDE or terminal.
4. Run the program using one of the following commands:

   ```bash
   python .\book_db.py <filename>
   ```

Depending on your operating system, you might prefer to use:

   ```bash
   python3 .\book_db.py <filename>
   ```

Where filename should be the name of a file containing a book database.

You can also run the program with the example database file:

   ```bash
   python .\book_db.py example_database.txt
   ```

## How to Create Your Own Database File

### Option 1: Using the Program

You can create your own database file by running the program and giving a filename that does not yet exist.
You can then start adding new books to the database with the program. If you do not add any books, the file is not created.

### Option 2: Manually Creating A Database File

If you want to create a database file in another way you can create one manually. The following rules should be considered:

- File is .txt format
- Each book is on their own line
- Book data is in the following format: name of the book/name of the writer/ISBN/publishing year

