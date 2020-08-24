from ExpensesManager import Category
import calendar
from datetime import datetime
import pandas as pd

class Movement:
    def __init__(self, id, date, description, amount, category):
        self.id = id
        self.date = date
        self.description = description
        self.amount = amount
        self.category = category

def updateDataBase(db):
    movements = []
    db.executeQuery("UPDATE 'categories' SET 'balance' = 0;")

    df = pd.read_csv("data/movements.csv")
    for index, row in df.iterrows():
        id = row['TransferWise ID']
        date = row['Date']
        description =row['Description']
        amount = row['Amount']

        id = int(id.split("-")[1])


        # creando objetos Movimiento para todos los movimientos
        movement = Movement(id, date, description, amount, None)

        categories = db.fetchColumnFromTable("*", "categories")

        movements.append(movement)
        try:
            db.insertMovementDB(id, date, amount, None, str(description))
        except Exception as e :
            pass
        Category.categorize(categories, movement, db)

    return movements

def printUncategorizedMoves(db):
    for movement in movementsOfCategory("Others", db):
        print("Description: " + str(movement[4]) + "-------- Date:" + str(movement[1]))
    return


# -------- RETURN MOVEMENTS DIFF TIMEFRAMES -------- #
def movementsOfCategory(category, db):
    query = "select * from movements where category =  '"+str(category)+"'"
    rows = db.executeQuery(query)
    return rows

def movementsOfYear(year, db):
    query = "select * from movements where date BETWEEN '" + str(year) + "-01-1' AND '" + str(year) + "-12-31'"
    rows = db.executeQuery(query)
    return rows

def movementsOfMonth(month, year, db):
    lastDay = calendar.monthrange(int(year), int(month))[1]

    startDate = datetime(int(year), int(month), 1).strftime('%Y-%m-%d')
    endDate = datetime(int(year), int(month), lastDay).strftime('%Y-%m-%d')

    query = "select * from movements where date BETWEEN '"+startDate+"' AND '"+endDate+"' AND category<>'Deposit'"
    rows = db.executeQuery(query)
    return rows

def movementsBetween(start, end, db):
    query = "select * from movements where date BETWEEN '" + str(start.date()) + "' AND '" + str(end.date()) + "'";
    rows = db.executeQuery(query)
    return rows






