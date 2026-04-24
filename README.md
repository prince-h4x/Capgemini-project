# Library Management System 📚

A command-line Library Management System built in Python using dictionaries, functions, and package architecture.

## Features

- ✅ Add books (stored as a dictionary with ID, name, author, status)
- ✅ View all books with availability status
- ✅ Issue a book — records student name, issue date, due date
- ✅ Return a book — checks if returned on time, applies fine if late
- ✅ View all currently issued books
- ✅ Fine system:
  - Week 1: ₹10/day
  - Week 2: ₹20/day
  - Week 3: ₹60/day
  - Week 4+: ₹240/day

## Project Structure

```
LIBRARY_MANAGEMENT/
├── main.py              # Menu + entry point (no logic)
├── services/
│   ├── __init__.py
│   ├── books.py         # Book records (dictionary), add & show books
│   └── issue.py         # Issue, return, fine calculation
└── README.md
```

## How to Run

```bash
python main.py
```

## Requirements

- Python 3.x — no external libraries needed
