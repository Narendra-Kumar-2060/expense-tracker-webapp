# Expense Tracker Web App

A full-stack web application to track expenses and income. Built with Flask, SQLite, and HTML/CSS.

## Features

- ✅ Add expenses and income
- ✅ Categorize transactions (Food, Travel, Entertainment, Other)
- ✅ Choose payment method (UPI, Cash, Card)
- ✅ View all transactions in a sortable table
- ✅ Delete transactions with confirmation dialog
- ✅ Automatic date and time recording
- ✅ Total amount summary on main page
- ✅ Summary dashboard with:
  - Total income, total expense, net balance
  - Category breakdown (expenses by category)
  - Payment method breakdown
- ✅ Responsive, modern CSS design
- ✅ Empty state message when no transactions exist

## Tech Stack

- **Backend:** Python (Flask)
- **Database:** SQLite3
- **Frontend:** HTML5, CSS3, Jinja2 templating
- **Deployment:** Ready for PythonAnywhere

## How to Run

1. Clone the repository

```bash
git clone https://github.com/Narendra-Kumar-2060/expense-tracker-webapp.git
cd expense-tracker-webapp
```

2. Install dependencies (Flask only)

```bash
pip install flask
```

3. Run the application

```bash
python app.py
```

4. Open your browser and go to http://127.0.0.1:5000

## Project Structure

expense-tracker-webapp/
├── app.py # Flask backend with routes
├── templates/
│ ├── index.html # Main page (form + transactions table)
│ └── summary.html # Summary dashboard
├── expenses.db # SQLite database (auto-created)
└── README.md # This file

## Database Schema

| Column            | Type    | Description                        |
| ----------------- | ------- | ---------------------------------- |
| id                | INTEGER | Primary key                        |
| date              | TEXT    | Transaction date                   |
| time              | TEXT    | Transaction time                   |
| amount            | REAL    | Amount (positive number)           |
| category          | TEXT    | Food, Travel, Entertainment, Other |
| description       | TEXT    | Optional note                      |
| payment_method    | TEXT    | UPI, Cash, Card                    |
| expense_or_income | TEXT    | 'expense' or 'income'              |

## Future Improvements

- Edit transactions
- Charts and graphs
- User authentication (multiple users)
- Export to CSV/PDF
- Monthly/yearly filters

## Author

Narendra Kumar

## GitHub

[GitHub](https://github.com/Narendra-Kumar-2060/expense-tracker-webapp)
