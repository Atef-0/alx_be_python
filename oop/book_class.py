class Book:
    def __init__(self, title, author, year):
        """Initialize the book with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """Return a detailed string representation of the book."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
    
    def __del__(self):
        """Clean up resources when the book object is deleted."""
        print(f"Deleting {self.title}")