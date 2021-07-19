import sqlite3


def connect():
    con = sqlite3.connect("bookstore.db")
    cursor = con.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS bookstore(id INTEGER PRIMARY KEY, Book TEXT, Author TEXT, Year INTEGER, ISBN INTEGER)")
    con.commit()
    con.close()


def insert(title, author, year, isbn):
    con = sqlite3.connect("bookstore.db")
    cursor = con.cursor()
    cursor.execute(
        "INSERT INTO bookstore VALUES(NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    con.commit()
    con.close()


def view():
    con = sqlite3.connect("bookstore.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM bookstore")
    rows = cursor.fetchall()
    con.commit()
    con.close()
    return rows


def search(title="", author="", year="", isbn=""):
    con = sqlite3.connect("bookstore.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM bookstore WHERE Book = ? or Author = ? or Year = ? or ISBN= ?",
                   (title, author, year, isbn))
    rows = cursor.fetchall()
    con.commit()
    con.close()
    return rows


connect()


def delete(id):
    con = sqlite3.connect("bookstore.db")
    cursor = con.cursor()
    cursor.execute("DELETE FROM bookstore WHERE id=?", (id,))
    rows = cursor.fetchall()
    con.commit()
    con.close()


def update(id, title, author, year, isbn):
    con = sqlite3.connect("bookstore.db")
    cursor = con.cursor()
    cursor.execute("UPDATE bookstore SET Book=?, Author=?, Year=?, ISBN=? WHERE id=?",
                   (title, author, year, isbn, id))
    con.commit()
    con.close()


# insert("The sun", "Ricky Fool", 1358, 91422253132)
# print(view())
# delete(1)

update(4, "The Moon", "John Doe", 2014, 4561321233)
print(view())
