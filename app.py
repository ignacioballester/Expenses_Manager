from Movement import Movement
from Connection import Connection
from DataBase import *
from ExpensesGraphView import *

connection = Connection('data/Excel_Transferwise.xlsx', 'Hoja 1')


if __name__ == '__main__':
    db = DataBase("data/movements.db")
    db.initialize()

    movements = Movement.updateDataBase(connection, db)


    Movement.expensesPerMonth("2019", db)
    Movement.expensesPerMonth("2020", db)

    Movement.expensesOfLastWeeks(7, db)


    for movement in Movement.movementsOfCategory("Canteen", db):
        print("Description: " + str(movement[4]) + "-------- Date:" +str(movement[1]))



    plotYearlyOverview("2020", connection,  db)
    plotExpensesOfYear("2020", connection, db)
    show()

    db.closeConnection()







