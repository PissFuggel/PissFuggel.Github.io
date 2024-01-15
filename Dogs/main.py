import os
import sqlite3
from sqlite3 import Error

#main()-----------------------------------------------------------

def main():
   
    while True:
        add_dog()
        list_dog_table()

        a = input("Vill ni lägga till en hund till? j/n")

        if (a == "n"):
            break

def add_dog():
    os.system('cls' if os.name == 'nt' else 'clear')

    hundnamn=input("Mata in hundnman: ")
    hundras=input("Mata in hundras: ")

    sqliteConnection = sqlite3.connect("dogs.db")
    Cursor = sqliteConnection.cursor()
    sqlite_insert_query= f"""INSERT INTO dogs (namn, ras) VALUES ('{hundnamn}', '{hundras}'); """

    Cursor.execute(sqlite_insert_query)
    sqliteConnection.commit()
    print("la Till Hund")
    Cursor.close()
    sqliteConnection.close()

#List_dog_table----------------------------
def list_dog_table():
    #skapar Connection
    sqliteConnection = sqlite3.connect("dogs.db")
    cursor=sqliteConnection.cursor()
    sql_select_query="""SELECT * FROM dogs ORDER BY NAMN"""
    cursor.execute(sql_select_query)
    records = cursor.fetchall()

    for row in records: 
        print(f"\tID: {row[0]}, \tNAMN: {row[1]}, \tRAS: {row[2]}")

    cursor.close()
    sqliteConnection.close()
    

main()
