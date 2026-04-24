from services.books import add_book, show_books
from services.issue import issue_book, return_book, show_issued

print("=" * 40)
print(" LIBRARY ")
print("=" * 40)

while True:
    print("\n==== MENU ======")
    print("  1. Add a Book")
    print("  2. Show All Books")
    print("  3. Issue a Book")
    print("  4. Return a Book")
    print("  5. View Issued Books")
    print("  6. Exit")
    print("=" * 34)

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_book()

    elif choice == "2":
        show_books()

    elif choice == "3":
        issue_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        show_issued()

    elif choice == "6":
        print("\n Thank you for using the Library System. ")
        break

    else:
        print(" Invalid choice! Please enter a number between 1 and 6.")
