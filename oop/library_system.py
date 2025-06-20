class Book:
    def __init__(self, title, author):
        self.title = str(title)
        self.author = str(author)

def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = int(file_size)
def __str__(self):
    return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):  # ✅ fixed: page_count (no dash)
        super().__init__(title, author)
        self.page_count = int(page_count)

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):  # ✅ fixed: added colon
            self.books.append(book)
        else:
            print("Only Book, EBook, or PrintBook instances can be added.")

    def list_books(self):
        if not self.books:
            print("Library is empty")
        else:
            for book in self.books:
                print(book)
