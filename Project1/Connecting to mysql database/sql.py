import mysql.connector
import difflib as db

con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

cursor = con.cursor()
word = input("Enter the word: ")
query = cursor.execute("SELECT * FROM Dictionary")
# query = cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{word}'")

result = cursor.fetchall()

if result:
    print(result)
else:
    print("No such word exists")
