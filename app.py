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

    Movement.expensesIn("Canteen", db)
    for movement in movements:
        if(movement.category[0] == "Others"):
            print(movement.description + " " +str(movement.date))



    #plotExpensesOfYear(connection, "2020",  db)
    db.closeConnection()







