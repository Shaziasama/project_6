class Book:
    total_books = 0  # Class variable to keep track of total books

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()  # Increment count when a book is created

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
# Creating Book objects
book1 = Book("Python Basics")
book2 = Book("Advanced Python")
book3 = Book("Data Structures")

# Displaying total book count
print("Total books added:", Book.total_books)
