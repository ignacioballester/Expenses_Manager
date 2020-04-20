import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

from Movement import *

def plotGraphs(connection, db):
    movements = Movement.updateDataBase(connection, db)
    categories = db.fetchColumnFromTable("*", "categories")
    # data to plot
    labels = []
    sizes = []
    total = 0.0
    for category in categories:
        if (category[0] != "Deposit"):
            total += category[1]

    print(total)

    for category in categories:
        if (category[0] != "Deposit"):
            labels.append(category[0])
            sizes.append((category[1]/total)*100)

    # Plot
    plt.pie(sizes, labels=labels,
            autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.show()


def plotExpensesOfYear(connection, year, db):
    movements = Movement.updateDataBase(connection, db)
    categories = db.fetchColumnFromTable("*", "categories")

    matplotlib.style.use('ggplot')

    data = [[2000, 2000, 2000, 2001, 2001, 2001, 2002, 2002, 2002],
            ['Jann', 'Feb', 'Mar', 'Jan', 'Feb', 'Mar', 'Jan', 'Feb', 'Mar'],
            [1, 2, 3, 4, 5, 6, 7, 8, 9]]

    rows = zip(data[0], data[1], data[2])
    headers = ['Year', 'Month', 'Value']
    df = pd.DataFrame(rows, columns=headers)



    fig, ax = plt.subplots(figsize=(10, 7))

    months = df['Month'].drop_duplicates()
    margin_bottom = np.zeros(len(df['Year'].drop_duplicates()))
    colors = ["#006D2C", "#31A354", "#74C476" , "#74C576" ]

    for num, month in enumerate(months):
        values = list(df[df['Month'] == month].loc[:, 'Value'])

        df[df['Month'] == month].plot.bar(x='Year', y='Value', ax=ax, stacked=True,
                                          bottom=margin_bottom, color=colors[num], label=month)
        margin_bottom += values

    plt.show()
