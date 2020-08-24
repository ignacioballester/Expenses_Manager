from ExpensesManager.DataBase import *
from ExpensesManager.ExpensesGraphView import *

if __name__ == '__init__':
    db = DataBase("data/movements.db")
    db.initialize()

    movements = Movement.updateDataBase(db)


    # expensesPerMonth("2019", db)
    # expensesPerMonth("2020", db)
    #
    # expensesOfLastWeeks(7, db)
    #db.insertKeyword("Canteen", "sdf, s")
    show()

    db.closeConnection()