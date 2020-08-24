import os, sys
from .CalculateExpenses import *
from .DataBase import DataBase
from .ExpensesGraphView import *

db = DataBase("/Users/ignacioballester/Portfolio/Expenses_Manager/data/movements.db")


def main():

    db.initialize()
    while True:
        updateDataBase(db)

        print("\n")
        print("Choose between these commands: ")
        print("expyear y         -- " + "(returns expenses of year y per month)")
        print("expmonth m y      -- " + "(returns expenses of month m and year y)")
        print("expweeks l        -- " + "(returns expenses of last l weeks)")
        print("expcat (category) -- " + "(prints expenses by category)")
        print("expgraph y        -- " + "(prints expenses of year y)")
        print("catgraph y        -- " + "(prints expenses of year y by category)")
        print("\n")

        var = input("Your command: ")
        var = var.split(" ")

        try:
            if var[0] == "expmonth":
                print(expensesMonth(int(var[1]), int(var[2]), db))

            elif var[0] == "expgraph":
                plotExpensesOfYear(int(var[1]), db)
                print("Close the graph to terminate command.")
                show()

            elif var[0] == "catgraph":
                plotYearlyOverview(int(var[1]), db)
                print("Close the graph to terminate command.")
                show()

            elif var[0] == "expweeks":
                expensesOfLastWeeks(int(var[1]), db)

            elif var[0] == "expyear":
                expensesPerMonth(int(var[1]), db)

            elif var[0] == "expcat":
                if len(var) == 2:
                    expensesIn(var[1], db)
                else:
                    expensesInAll(db)

            elif var[0] == "clear":
                os.system('cls' if os.name == 'nt' else 'clear')

            elif var[0] == "exit":
                sys.exit()

            else:
                print("ERROR: Command was not correctly formatted.")

        except Exception as e:
            print("An exception occurred: {}".format(e))

        print("\n" + "           ---- ----           " + "\n")



if __name__ == '__main__':
    main()
    db.closeConnection()