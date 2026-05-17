import sqlite3
from datetime import datetime

from flask import Flask, redirect, render_template, request


def init_db():
    con = sqlite3.connect("expenses.db")
    cur = con.cursor()

    create_table = """
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY,
        date TEXT NOT NULL, 
        time TEXT NOT NULL,
        amount REAL NOT NULL,    
        category TEXT NOT NULL,
        description TEXT,
        payment_method TEXT NOT NULL,
        expense_or_income TEXT NOT NULL CHECK(expense_or_income IN ('expense', 'income'))          
    );
    """

    cur.execute(create_table)

    con.commit()
    con.close()


app = Flask(__name__)


@app.route("/")
def index():
    con = sqlite3.connect("expenses.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM expenses ORDER BY date DESC, time DESC")
    transactions = cur.fetchall()

    cur.execute("SELECT SUM(amount) FROM expenses")
    total_amount = cur.fetchone()[0] or 0

    con.close()
    return render_template(
        "index.html", transactions=transactions, total_amount=total_amount
    )


@app.route("/delete/<int:id>")
def delete(id):
    con = sqlite3.connect("expenses.db")
    cur = con.cursor()
    cur.execute("DELETE FROM expenses WHERE id = ?", (id,))
    con.commit()
    con.close()
    return redirect("/")


@app.route("/summary")
def summary():
    con = sqlite3.connect("expenses.db")
    cur = con.cursor()

    cur.execute("SELECT SUM(amount) FROM expenses WHERE expense_or_income = 'expense'")
    total_expense = cur.fetchone()[0] or 0

    cur.execute("SELECT SUM(amount) FROM expenses WHERE expense_or_income = 'income'")
    total_income = cur.fetchone()[0] or 0

    cur.execute(
        "SELECT category, SUM(amount) FROM expenses WHERE expense_or_income = 'expense' GROUP BY category"
    )
    category_summary = cur.fetchall()

    cur.execute(
        "SELECT payment_method, SUM(amount) FROM expenses GROUP BY payment_method"
    )
    payment_summary = cur.fetchall()

    con.close()

    net = total_income - total_expense

    return render_template(
        "summary.html",
        total_expense=total_expense,
        total_income=total_income,
        net=net,
        category_summary=category_summary,
        payment_summary=payment_summary,
    )


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        now = datetime.now()
        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M")
        try:
            amount = float(request.form["amount"])
        except ValueError:
            return "Invalid amount. Please enter a number.", 400
        transaction_type = request.form["transaction_type"]
        transaction_category = request.form["transaction_category"]
        payment_method = request.form["payment_method"]
        description = request.form["description"]

        con = sqlite3.connect("expenses.db")
        cur = con.cursor()

        cur.execute(
            "INSERT INTO expenses (date, time, amount, category, description, payment_method, expense_or_income) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                date,
                time,
                amount,
                transaction_category,
                description,
                payment_method,
                transaction_type,
            ),
        )

        con.commit()
        con.close()

    return redirect("/")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
