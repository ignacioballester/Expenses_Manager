import sys
from .CalculateExpenses import *
from .DataBase import DataBase as db

def main():
    print("Choose between these commands: ")
    print("expmonth m y   -- " + "(returns expenses of month m and year y)")
    print("explweeks l    -- " + "(returns expenses of last l weeks)")
    print("expgraph y     -- " + "(prints expenses of year y)")
    print("catgraph y     -- " + "(prints expenses of year y by category)")


    var = input("Your command: ")

    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        if (arg == "-lmonth"):
            expensesMonth
            print('passed argument :: {}'.format(arg))

    print("hello World")

if __name__ == '__main__':
    main()
    db.closeConnection()