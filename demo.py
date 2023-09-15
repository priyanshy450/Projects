import psycopg2

def create():
    conn = psycopg2.connect(dbname = "postgres", user="postgres", password = "Priy@2000", host ="localhost", port = "5432")
    cur = conn.cursor()
    cur.execute('''create table student(id serial, name text, age text, address text);''')
    print("table created")
    conn.commit()
    conn.close()

def insert_data():
    conn = psycopg2.connect(dbname = "postgres", user="postgres", password = "Priy@2000", host ="localhost", port = "5432")
    cur = conn.cursor()
    name = input("enter name")
    age = input("enter age")
    address = input("enter address")
    query ='''insert into student (name,age, address) values (%s, %s, %s);'''
    cur.execute(query,(name, age, address))
    print("table created")
    conn.commit()
    conn.close()

insert_data()