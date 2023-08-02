class BookType:
    FICTION = "Fiction"
    NON_FICTION = "Non-Fiction"
    SCIENCE_FICTION = "Science Fiction"
    MYSTERY = "Mystery"
    ROMANCE = "Romance"
    FANTASY = "Fantasy"
    # Add more book types as needed


class Book:
    def __init__(self, title, author, isbn, book_type):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.book_type = book_type


class Library:
    def __init__(self):
        self.books = []
        self.authors = set()

    def add_book(self, book):
        self.books.append(book)
        self.authors.add(book.author)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            self.authors.discard(book.author)

    def search_book_by_title(self, title):
        return [book for book in self.books if book.title == title]

    def get_unique_authors(self):
        return list(self.authors)

    def search_book_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def search_book_by_isbn(self, isbn):
        return [book for book in self.books if book.isbn == isbn]

    def display_all_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author} (ISBN: {book.isbn})")

    def add_popular_books(self):
        # Adding some popular books to the library
        popular_books = [
            # Fiction
            Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "059035342X", BookType.FICTION),
            Book("To Kill a Mockingbird", "Harper Lee", "0061120081", BookType.FICTION),
            # Non-Fiction
            Book("Educated: A Memoir", "Tara Westover", "0399590501", BookType.NON_FICTION),
            Book("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", "0062316117", BookType.NON_FICTION),
            # Science Fiction
            Book("Dune", "Frank Herbert", "0441172717", BookType.SCIENCE_FICTION),
            Book("Foundation", "Isaac Asimov", "0553803719", BookType.SCIENCE_FICTION),
            # Mystery
            Book("The Da Vinci Code", "Dan Brown", "0307474275", BookType.MYSTERY),
            Book("Gone Girl", "Gillian Flynn", "0307588378", BookType.MYSTERY),
            # Romance
            Book("The Notebook", "Nicholas Sparks", "0553816713", BookType.ROMANCE),
            Book("Outlander", "Diana Gabaldon", "0385319959", BookType.ROMANCE),
            # Fantasy
            Book("The Name of the Wind", "Patrick Rothfuss", "0756404746", BookType.FANTASY),
            Book("Mistborn: The Final Empire", "Brandon Sanderson", "076531178X", BookType.FANTASY),
        ]

        for book in popular_books:
            self.add_book(book)

    def add_book_with_type(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        isbn = input("Enter the ISBN of the book: ")

        print("Select the book type:")
        print("1. Fiction")
        print("2. Non-Fiction")
        print("3. Science Fiction")
        print("4. Mystery")
        print("5. Romance")
        print("6. Fantasy")

        book_type_choice = input("Enter your choice (1-6): ")

        book_type_map = {
            "1": BookType.FICTION,
            "2": BookType.NON_FICTION,
            "3": BookType.SCIENCE_FICTION,
            "4": BookType.MYSTERY,
            "5": BookType.ROMANCE,
            "6": BookType.FANTASY,
        }

        book_type = book_type_map.get(book_type_choice)
        if book_type:
            self.add_book(Book(title, author, isbn, book_type))
            print("Book added successfully!")
        else:
            print("Invalid choice. Book not added.")


def main():
    library = Library()
    library.add_popular_books()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book by Title")
        print("4. Search Book by Author")
        print("5. Display Unique Authors")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            library.add_book_with_type()
        elif choice == "2":
            library.display_all_books()
        elif choice == "3":
            title = input("Enter the title of the book: ")
            result = library.search_book_by_title(title)
            if result:
                print(f"Found {len(result)} book(s) with the title '{title}':")
                for book in result:
                    print(f"Author: {book.author}, ISBN: {book.isbn}")
            else:
                print(f"No books found with the title '{title}'.")
        elif choice == "4":
            author = input("Enter the author of the book: ")
            result = library.search_book_by_author(author)
            if result:
                print(f"Found {len(result)} book(s) by the author '{author}':")
                for book in result:
                    print(f"Title: {book.title}, ISBN: {book.isbn}")
            else:
                print(f"No books found by the author '{author}'.")
        elif choice == "5":
            unique_authors = library.get_unique_authors()
            print("Unique Authors:")
            for idx, author in enumerate(unique_authors, 1):
                print(f"{idx}. {author}")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
