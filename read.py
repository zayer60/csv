from mysql.connector import connect
import csv
import datetime
import pandas


def insert_from_csv(csv_path):
    conn = connect(host="localhost",user="zayerwali",password="Z@zayer7006",db="studentdb")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS stud(roll INTEGER ,name TEXT, dob DATE, gender TEXT)")
    with open(csv_path, 'r') as files:
        contents = csv.DictReader(files)
        details = [(i['roll'], i['name'], i['dob'], i['gender']) for i in contents]
    cur.executemany("INSERT INTO stud VALUES(%s,%s,%s,%s) ", details)
    conn.commit()
    conn.close()
    print("database Updated")


def show_from_csv2(csv_path):
    with open(csv_path) as file:
        contents = csv.reader(file)
        all_data = []
        for row in contents:
            all_data.append(row)
        return print(all_data)


def csv_to_sql2(csv_path):
    file = pandas.read_csv(csv_path)
    data = pandas.DataFrame(file)
    conn = connect(host="localhost",user="zayerwali",password="Z@zayer7006",db="studentdb")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS stud(roll INTEGER ,name TEXT, dob DATE, gender TEXT)")
    for row in data.itertuples():
        cur.execute("INSERT INTO stud VALUES(%s,%s,%s,%s)", (row.roll, row.name, row.dob, row.gender))
    conn.commit()
    conn.close()


def fetch_from_csv(csv_path):
    csv_data = pandas.read_csv(csv_path)
    print(csv_data)

#def fetch_all_rows():
#    conn = sqlite3.connect("data.db")
#    cur = conn.cursor()
#    cur.execute("SELECT * FROM stu")
#    rows = cur.fetchall()
#    conn.close()
#    return rows


io = input("Read/Write from csv? Press csv, Read/Write from pandas? Press panda: ")
if io == "csv":
    file = input("csv file: ")
    insert_from_csv(file)
    print(show_from_csv2(file))
elif io == "panda":
    file = input("panda file: ")
    csv_to_sql2(file)
    fetch_from_csv(file)
else:
    ("no input provided")