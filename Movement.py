from Category import Category
import calendar
from datetime import datetime, timedelta

class Movement:

    def __init__(self, id, date, description, amount, category):
        self.id = id
        self.date = date
        self.description = description
        self.amount = amount
        self.category = category

    @staticmethod
    def updateDataBase(connection, db):
        movements = []
        db.executeQuerry("UPDATE 'categories' SET 'balance' = 0;")
        for i in range(3, connection.sheet.max_row + 1):
            id = connection.sheet.cell(row=i, column=1).value
            date = connection.sheet.cell(row=i, column=2).value
            description = connection.sheet.cell(row=i, column=5).value
            amount = float(connection.sheet.cell(row=i, column=3).value)

            id = int(id.split("-")[1])

            # creando objetos Movimiento para todos los movimientos
            movement = Movement(id, date, description, amount, None)

            categories = db.fetchColumnFromTable("*", "categories")

            movements.append(movement)

            try:
                db.insertMovementDB(id, date, amount, None, str(description))
            except:
                pass
            Category.categorize(categories, movement, db)

        return movements

    @staticmethod
    def movementsOfCategory(category, db):
        querry = "select * from movements where category =  '"+str(category)+"'"
        rows = db.executeQuerry(querry)
        return rows

    @staticmethod
    def expensesIn(category, db):
        rows = Movement.movementsOfCategory(category, db)
        total = 0.0
        for row in rows:
            total += row[2]
        print("Category " + category +": " + str(round(total, 2)))
    # ------ MONTH EXPENSES ------ #

    @staticmethod
    def movementsOfLastMonth(month, year, db):
        lastDay = calendar.monthrange(int(year), int(month))[1]
        querry = "select * from movements where date BETWEEN '"+year +"-"+ month +"-1' AND '"+ year +"-"+ month +"-"+str(lastDay) +"'"
        rows = db.executeQuerry(querry)
        return rows

    @staticmethod
    def expensesMonth(month, year, db):
        total = 0.0
        rows = Movement.movementsOfLastMonth(month,year, db)
        for row in rows:
            if (row[3] != "Deposit"):
                total += row[2]
        return "Monthly Expenses " + month+"/"+ year+": "+str(round(total,2))

    @staticmethod
    def expensesPerMonth(year, db):
        result = ""
        for i in range(1,10):
            month = Movement.expensesMonth("0"+str(i), year, db)
            if(month.find(str("0.0")) == -1):
                result += "\n" + month

        for i in range(10,13):
            month = Movement.expensesMonth(str(i), year, db)
            if(month.find(str(0.0)) == -1):
                result += "\n" + month
        print(result)


    # ------ WEEK EXPENSES ------ #

    @staticmethod
    def movementsOfWeek(start, end, db):
        querry = "select * from movements where date BETWEEN '" + str(start.date()) + "' AND '" + str(end.date()) + "'";
        rows = db.executeQuerry(querry)
        return rows

    @staticmethod
    def expensesWeek(start, end, db):
        total = 0.0
        rows = Movement.movementsOfWeek(start, end, db)
        for row in rows:
            if (row[3] != "Deposit"):
                total += row[2]
        return "Weekly Expenses of " + str(start.date()) + ": " + str(round(total,2))

    @staticmethod
    def expensesOfLastWeeks(limit, db):
        result = ""
        for i in range (0, limit):
            now = datetime.now()-timedelta(weeks=i)
            start_week = now +timedelta(days=8-now.isoweekday()) - timedelta(weeks=1)
            end_week = now +timedelta(days=7-now.isoweekday())
            week_expenses = Movement.expensesWeek(start_week, end_week, db)
            if (week_expenses.find(str("0.0")) == -1):
                result += "\n" + week_expenses

        print(result + "\n")