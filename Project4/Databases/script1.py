import psycopg2


def create():
    con = psycopg2.connect(
        "dbname= 'database1' user= 'postgres' password= 'TUy)j&,q!n6!V8M!' host= 'localhost' port= '5432' ")
    cursor = con.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    con.commit()
    con.close()


def insert(item, quantity, price):
    con = psycopg2.connect(
        "dbname='database1' user='postgres' password='TUy)j&,q!n6!V8M!' host='localhost' port='5432'")
    cursor = con.cursor()
    cursor.execute("INSERT INTO store VALUES(%s, %s, %s)",
                   (item, quantity, price))
    con.commit()
    con.close()


def delete(item):
    con = psycopg2.connect(
        "dbname= 'database1' user= 'postgres' password= 'TUy)j&,q!n6!V8M!' host= 'localhost' port= '5432' ")
    cursor = con.cursor()
    cursor = cursor.execute("DELETE FROM store WHERE item = %s", (item,))
    con.commit()
    con.close()


def update(quantity, price, item):
    con = psycopg2.connect(
        "dbname= 'database1' user= 'postgres' password= 'TUy)j&,q!n6!V8M!' host= 'localhost' port= '5432' ")
    cursor = con.cursor()
    cursor.execute(
        'UPDATE store SET quantity = %s, price = %s WHERE item = %s', (quantity, price, item))
    con.commit()
    con.close()


def view():
    con = psycopg2.connect(
        "dbname= 'database1' user= 'postgres' password= 'TUy)j&,q!n6!V8M!' host= 'localhost' port= '5432' ")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    con.close()
    return rows


create()
insert("Wine", 6, 2)
insert("Water", 6, 2)
print(view())
