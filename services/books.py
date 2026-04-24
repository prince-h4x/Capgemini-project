
books = {}

def add_book():
    print("\n--- Add New Book ---")
    book_id = input("Enter Book ID       : ").strip()
    if book_id in books:
        print(f" Book ID '{book_id}' already exists.")
        return
    name   = input("Enter Book Name     : ").strip()
    author = input("Enter Author Name   : ").strip()

    books[book_id] = {
        "name"   : name,
        "author" : author,
        "status" : "Available"
    }
    print(f"\n '{name}' by {author} added successfully!")

def show_books():
    print("\n- All Books in Library -")
    if not books:
        print(" No books available in the library.")
        return
    print(f"{'ID':<8} {'Book Name':<25} {'Author':<20} {'Status'}")
    print("-" * 65)
    for book_id, info in books.items():
        print(f"{book_id:<8} {info['name']:<25} {info['author']:<20} {info['status']}")
