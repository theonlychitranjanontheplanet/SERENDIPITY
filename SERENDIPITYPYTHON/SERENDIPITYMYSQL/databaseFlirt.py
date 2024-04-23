import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    user="root",
    passwd="Bro123@bruh",
    database="serendipity"
)


myCursor = mydb.cursor()

testFormula = "INSERT INTO test (age, name) VALUES (%s, %s)"
chadOne = (20, "Zamn")

myCursor.execute(testFormula, chadOne)

mydb.commit()