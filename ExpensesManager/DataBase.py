import sqlite3
import datetime
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
            print("Movements DB created")
        except:
            pass

        try:
            self.createCategoriesTable()
            self.insertCateogory("Deposit", "Topped")
            self.insertCateogory("Others", None)
            self.insertCateogory("Canteen", "Uzh, ETH")
            self.insertCateogory("Supermarket", "Coop, Denner, Migros, Migrolino")
            self.insertCateogory("Restaurant", "Chinarestaurant, Suan, Domino's, Restaurant, Vbg, bar, March, Bistro")
            self.insertCateogory("Shopping", "Zara, Confiserie, Interdiscount, Movie, Decathlon, Orell")
            self.insertCateogory("Transport", "Vbz, SBB")
            self.insertCateogory("Cash Withdrawal", "Ubs")
            self.insertCateogory("Activities", "Uetliberg, Dolder")
            print("Basic categories DB created")
        except:
            pass

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



    def executeQuery(self, query):
        self.c.execute(query)
        rows = self.c.fetchall()
        return rows

    def insertCateogory(self, name, keywords):
        query = """INSERT INTO 'categories'
                                         (id, balance, keywords) 
                                         VALUES (?, ?, ?);"""

        param = (name, 0, keywords)
        self.c.execute(query, param)
        return


    def insertMovementDB(self, id, date, amount, category, description):
        query = """INSERT INTO 'movements'
                                  (id, date, amount, category, description) 
                                  VALUES (?, ?, ?, ?, ?);"""
        date = datetime.datetime.strptime(date, '%d-%m-%Y')
        param = (id, date, amount, category, description)
        self.c.execute(query, param)
        return


    def insertKeyword(self, category, word):
        if(word[-1] is "," or word[-1] is " " or word[-1] is "-"):
            raise Exception("Incorrect formating")

        query = "SELECT keywords FROM 'categories' WHERE id= '" + str(category)+"'"
        self.c.execute(query)
        currKeywords = self.c.fetchall()[0][0]
        newKeywords = str(currKeywords) + ", " + word
        self.updateRow("categories", "keywords", str(newKeywords), str(category))
        return


    def fetchColumnFromTable(self, column, table):
        query = "SELECT " + column + " from '"+table+"';"
        self.c.execute(query)
        rows = self.c.fetchall()
        return rows

    def fetchBalance(self, id):
        querry = "SELECT balance from 'categories' WHERE id= '"+ str(id)+"';"
        self.c.execute(querry)

        rows = self.c.fetchall()
        return rows


    def updateRow(self, table, column, value, id):
        query = "UPDATE '" + str(table) + "' SET '" + str(column) + "' = '" + str(value) + "' WHERE id = '" + str(
            id) + "';"
        self.c.execute(query)
        return


    def resetBalance(self):
        query = "UPDATE 'categories' SET 'balance' = 0;"
        self.c.execute(query)
        return


    def closeConnection(self):
        self.conn.commit()
        self.conn.close()
        return


    def commit(self):
        self.conn.commit()
        return

