import os
import sqlite3
from sqlite3 import Error

engelska_glosor = []
svenska_glosor = []

def main():
   
    while True:
        add_glosa()
        a = input("Har du någon fler glosa att lägga till? j/n")

        if (a == "n"):
            break

def add_glosa():
    os.system('cls' if os.name == 'nt' else 'clear')

    svenska=input("Mata in Svensk glosa: ")
    engelska=input("Mata in Engelsk glosa: ")
    #Skapar Connection
    sqliteConnection = sqlite3.connect("glosor.db")
    Cursor = sqliteConnection.cursor()
    sqlite_insert_query= f"""INSERT INTO glosor (svensk_glosa, engelsk_glosa) VALUES ('{svenska}', '{engelska}'); """

    Cursor.execute(sqlite_insert_query)
    sqliteConnection.commit()
    print("Klar med din glosa")
    Cursor.close()
    sqliteConnection.close()

def list_glosor_table():
    #skapar Connection
    sqliteConnection = sqlite3.connect("glosor.db")
    cursor=sqliteConnection.cursor()
    sql_select_query="""SELECT * FROM glosor ORDER BY groups_id"""
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    cursor.close()
    sqliteConnection.close()

    for row in records: 
        engelska_glosor.append(row[2])
        svenska_glosor.append(row[1])


def train_glosa():
    list_glosor_table()

    for x in range(len(svenska_glosor)):
        
        print(svenska_glosor[x])
        print(engelska_glosor[x])


train_glosa()