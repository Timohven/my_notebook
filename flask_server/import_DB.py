import mysql.connector
import csv

def create_notes_DB():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="MyNoteBookDB"
        )

    except mysql.connector.Error as error:
        print("Ошибка при работе с MySQL", error)
    finally:
        if mydb:
            mydb.close()
            print("Соединение с MySQL закрыто")

def find_note(note_id):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ErhCthdbC_2006",
            database="MyNoteBookDB"
        )
        cursor = mydb.cursor()
        sql_select_query = """SELECT content FROM notes WHERE note_id = %s;"""
        cursor.execute(sql_select_query, (note_id,))
        result = cursor.fetchone()
        cursor.close()
        return result

    except mysql.connector.Error as error:
        print("Error at work at MySQL", error)
    finally:
        if mydb:
            mydb.close()
            print("Connection with MySQL closed")

def get_all_notes():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ErhCthdbC_2006",
            database="MyNoteBookDB"
        )
        cursor = mydb.cursor(buffered=True)
        sql_select_query = """SELECT * FROM notes;"""
        cursor.execute(sql_select_query)
        result = cursor.fetchall()
        #for row in result: print(row)
        cursor.close()
        return result

    except mysql.connector.Error as error:
        print("Error at work at MySQL", error)
    finally:
        if mydb:
            mydb.close()
            print("Connection with MySQL closed")