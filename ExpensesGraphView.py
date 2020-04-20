import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

from Movement import *


def plotGraphs(year, connection, db):
    f1 = plt.figure("Overview (" + str(year) + ")")
    Movement.updateDataBase(connection, db)
    movements = Movement.movementsOfYear(year, db)
    categories = db.fetchColumnFromTable("*", "categories")

    # Data to plot
    values = Category.categorizedBalance(categories, movements)


    # Plot
    plt.pie(dict.values(values), labels=dict.keys(values),
            autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')



def plotExpensesOfYear(connection, year, db):
    f2 = plt.figure("Overview of " + str(year))
    Movement.updateDataBase(connection, db)
    categories = db.fetchColumnFromTable("*", "categories")
    df = pd.DataFrame()
    columns = []
    importantCategory = []

    for i in range(1, len(categories)):
        columns.append(categories[i][0])
        df[categories[i][0]] = []

    for i in range (1, 13):
        movesMonth = Movement.movementsOfLastMonth(i, year, db)
        values = Category.categorizedBalance(categories, movesMonth)



        df = df.append(values, ignore_index=True)

    df.index = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nob', 'Dec']
    df.plot(kind='bar', stacked=True)




def show():
    plt.show()