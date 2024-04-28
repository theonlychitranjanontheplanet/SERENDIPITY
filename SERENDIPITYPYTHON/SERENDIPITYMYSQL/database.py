import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    user="root",
    passwd="Bro123@bruh",
    database="serendipity"
)


myCursor = mydb.cursor()


def intoDatabase(ID, text, vector):
    
    formula = "INSERT INTO memory (ID, memoryWords, vector) VALUES (%s, %s, %s)"
    variables = (ID, text, vector)

    myCursor.execute(formula, variables)

    mydb.commit()




def clearDatabase():
    myCursor.execute("TRUNCATE memory")
    


clearDatabase()