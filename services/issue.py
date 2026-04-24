from datetime import datetime, timedelta
from services.books import books

issued_books = {}

def calculate_fine(days_late):
    """
    Fine structure (per day per book):
      Week 1 : ₹10/day
      Week 2 : ₹20/day  (10 * 2)
      Week 3 : ₹60/day  (10 * 2 * 3)
      Week 4+: ₹240/day (10 * 2 * 3 * 4)
    """
    if days_late <= 0:
        return 0

    fine = 0
    week_rate = 10
    multiplier = 1
    remaining = days_late

    for week in range(1, 5):
        rate = week_rate * multiplier
        days_in_this_week = min(remaining, 7)
        fine += days_in_this_week * rate
        remaining -= days_in_this_week
        multiplier *= (week + 1)
        if remaining <= 0:
            break

    if remaining > 0:
        fine += remaining * (week_rate * multiplier)

    return fine

def issue_book():
    print("\n--- Issue a Book ---")
    show_available()

    book_id = input("\nEnter Book ID to Issue  : ").strip()
    if book_id not in books:
        print(" Book ID not found in library.")
        return
    if books[book_id]["status"] == "Issued":
        print(f"'{books[book_id]['name']}' is already issued.")
        return

    student_name = input("Enter Student Name      : ").strip()
    try:
        days = int(input("Issue for how many days : "))
        if days <= 0:
            print("Days must be a positive number.")
            return
    except ValueError:
        print(" Invalid input. Please enter a number.")
        return

    issue_date  = datetime.now()
    due_date  = issue_date + timedelta(days=days)

    issued_books[book_id] = {
        "student"    : student_name,
        "issue_date" : issue_date,
        "due_date"   : due_date,
        "days"       : days
    }
    books[book_id]["status"] = "Issued"

    print(f"\n'{books[book_id]['name']}' issued to {student_name}")
    print(f"   Issue Date : {issue_date.strftime('%d-%m-%Y')}")
    print(f"   Due Date   : {due_date.strftime('%d-%m-%Y')}  ({days} days)")
    print(f"   Fine after due date: ₹10/day (Week 1), ₹20/day (Week 2), ₹60/day (Week 3)...")

def return_book():
    print("\n--- Return a Book ---")
    if not issued_books:
        print("No books are currently issued.")
        return

    show_issued()
    book_id = input("\nEnter Book ID to Return : ").strip()

    if book_id not in issued_books:
        print(" This book was not issued from this library.")
        return

    record       = issued_books[book_id]
    return_date  = datetime.now()
    due_date     = record["due_date"]
    days_late    = (return_date - due_date).days
    fine         = calculate_fine(days_late)

    print(f"\n Book     : {books[book_id]['name']}")
    print(f"   Student  : {record['student']}")
    print(f"   Issued   : {record['issue_date'].strftime('%d-%m-%Y')}")
    print(f"   Due Date : {due_date.strftime('%d-%m-%Y')}")
    print(f"   Returned : {return_date.strftime('%d-%m-%Y')}")

    if days_late > 0:
        print(f"\n   Book returned {days_late} day(s) late!")
        print(f"   Fine to Pay   : ₹{fine}")
    else:
        print(f"\n   Book returned on time! No fine.")

    # Update records
    books[book_id]["status"] = "Available"
    del issued_books[book_id]

def show_available():
    available = {k: v for k, v in books.items() if v["status"] == "Available"}
    if not available:
        print(" No books available right now.")
        return
    print("\nAvailable Books:")
    print(f"{'ID':<8} {'Book Name':<25} {'Author'}")
    print("-" * 50)
    for book_id, info in available.items():
        print(f"{book_id:<8} {info['name']:<25} {info['author']}")

def show_issued():
    if not issued_books:
        print(" No books currently issued.")
        return
    print("\nCurrently Issued Books:")
    print(f"{'ID':<8} {'Book Name':<22} {'Student':<18} {'Due Date'}")
    print("-" * 65)
    for book_id, record in issued_books.items():
        print(f"{book_id:<8} {books[book_id]['name']:<22} {record['student']:<18} {record['due_date'].strftime('%d-%m-%Y')}")
