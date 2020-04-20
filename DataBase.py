import sqlite3


class DataBase:
    c = None

    def __init__(self, file):
        self.file = file
        self.conn = None
        self.c = None

    def openConnection(self):
        self.conn = sqlite3.connect(self.file)
        self.c = self.conn.cursor()

    def initialize(self):
        self.openConnection()
        try:
            self.createMovementTable()
        except:
            print("Already Created")

        try:
            self.createCategoriesTable()
            self.insertCateogory("Deposit", "Topped")
            self.insertCateogory("Others", None)
            self.insertCateogory("Canteen", "Uzh, ETH")
            self.insertCateogory("Supermarket", "Coop, Denner, Migros, Migrolino")
            self.insertCateogory("Restaurant", "Chinarestaurant, Suan, Domino's, Restaurant, Vbg, bar")
            self.insertCateogory("Shopping", "Zara, Confiserie, Interdiscount, Movie")
            self.insertCateogory("Transport", "Vbz, SBB")
            self.insertCateogory("Cash Withdrawal", "Ubs")
            self.insertCateogory("Activities", "Uetliberg, Dolder")
        except:
            print("Already Created")

    def createMovementTable(self):
        self.c.execute(""" CREATE TABLE movements (
                             id INTEGER UNIQUE,
                             date timestamp,
                             amount REAL,
                             category TEXT,
                             description TEXT
                             )""")

    def createCategoriesTable(self):
        self.c.execute(""" CREATE TABLE categories (
                             id TEXT UNIQUE,
                             balance REAL,
                             keywords TEXT
                             )""")

    def executeQuerry(self, querry):

        self.c.execute(querry)
        rows = self.c.fetchall()
        return rows

    def insertCateogory(self, name, keywords):
        querry = """INSERT INTO 'categories'
                                         (id, balance, keywords) 
                                         VALUES (?, ?, ?);"""

        param = (name, 0, keywords)
        self.c.execute(querry, param)

    def insertMovementDB(self, id, date, amount, category, description):
        querry = """INSERT INTO 'movements'
                                  (id, date, amount, category, description) 
                                  VALUES (?, ?, ?, ?, ?);"""

        param = (id, date, amount, category, description)
        self.c.execute(querry, param)

    def fetchColumnFromTable(self, column, table):
        querry = "SELECT " + column + " from '"+table+"';"
        self.c.execute(querry)

        rows = self.c.fetchall()
        return rows

    def fetchBalance(self, id):
        querry = "SELECT balance from 'categories' WHERE id= '"+ str(id)+"';"
        self.c.execute(querry)

        rows = self.c.fetchall()
        return rows



    def updateRow(self, table, column, value, id):
        querry = "UPDATE '" + str(table) + "' SET '" + str(column) + "' = '" + str(value) + "' WHERE id = '" + str(
            id) + "';"
        self.c.execute(querry)

    def resetBalance(self):
        querry = "UPDATE 'categories' SET 'balance' = 0;"
        self.c.execute(querry)

    def closeConnection(self):
        self.conn.commit()
        self.conn.close()

    def commit(self):
        self.conn.commit()
