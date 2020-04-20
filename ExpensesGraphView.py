import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

from Movement import *


def plotYearlyOverview(year, connection, db):
    Movement.updateDataBase(connection, db)
    movements = Movement.movementsOfYear(year, db)
    categories = db.fetchColumnFromTable("*", "categories")

    # Data to plot
    values = Category.categorizedBalance(categories, movements)

    # Plot
    plt.pie(dict.values(values), labels=dict.keys(values),
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title("Overview Expenses ("+ str(year) + ")")
    plt.axis('equal')



def plotExpensesOfYear(year, connection, db):
    Movement.updateDataBase(connection, db)
    categories = db.fetchColumnFromTable("*", "categories")
    df = pd.DataFrame()



    for i in range (1, 13):
        movesMonth = Movement.movementsOfLastMonth(i, year, db)
        values = Category.categorizedBalance(categories, movesMonth)



        df = df.append(values, ignore_index=True)

    df.index = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nob', 'Dec']
    df.plot(kind='bar', stacked=True, title="Monthly View Expenses (" +str(year) + ")")




def show():
    plt.show()