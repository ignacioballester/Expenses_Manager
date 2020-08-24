from .Movement import *
from datetime import timedelta, datetime


# --------- CATEGORY EXPENSES --------- #
def expensesIn(category, db):
    rows = movementsOfCategory(category, db)
    total = 0.0
    for row in rows:
        total += row[2]
    print("Category " + category + ": " + str(round(total, 2)))


def expensesInAll(db):
    categories = db.fetchColumnFromTable("*", "categories")
    for category in categories:
        expensesIn(str(category[0]), db)


# ---------- MONTHLY EXPENSES ----------- #
def expensesMonth(month, year, db):
    total = 0.0
    rows = movementsOfMonth(month, year, db)
    for row in rows:
        if row[3] != "Deposit":
            total += row[2]
    return "Monthly Expenses " + str(month) + "/" + str(year) + ": " + str(round(total, 2))


def expensesPerMonth(year, db):
    result = ""
    total = 0.0
    for i in range(1, 13):
        month = expensesMonth(i, year, db)
        if (month.find(str("0.0")) == -1):
            result += "\n" + month
            total += float(month.split(" ")[3])
    print(result + "\n")
    print("Total Expenses of {}: {}".format(str(year), total))


# ---------- WEEKLY EXPENSES ----------- #
def expensesOfLastWeeks(limit, db):
    result = ""
    for i in range(0, limit):
        now = datetime.now() - timedelta(weeks=i)
        start_week = now + timedelta(days=8 - now.isoweekday()) - timedelta(weeks=1)
        end_week = now + timedelta(days=7 - now.isoweekday())
        week_expenses = expensesBetween(start_week, end_week, db)
        if week_expenses.find(str("0.0")) == -1:
            result += "\n" + week_expenses

    print(result + "\n")


# ---------- TIMEFRAME EXPENSES ----------- #

def expensesBetween(start, end, db):
    total = 0.0
    rows = movementsBetween(start, end, db)
    for row in rows:
        if row[3] != "Deposit":
            total += row[2]
    return "Weekly Expenses of " + str(start.date()) + ": " + str(round(total, 2))
