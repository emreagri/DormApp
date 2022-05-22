import sqlite3 as sql

def create_table():
    conn = sql.connect('proje.db')
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS OGRENCI(
        id integer PRIMARY KEY,
        name text,
        yas text,
        cinsiyet text,
        okul text        
    ) """)

    conn.commit()
    conn.close()

def insert(name, yas, cinsiyet, okul):
    conn = sql.connect('proje.db')
    cursor = conn.cursor()

    add_command = """INSERT INTO OGRENCI(name, yas, cinsiyet, okul) VALUES {} """
    data = (name, yas, cinsiyet, okul)

    cursor.execute(add_command.format(data))

    conn.commit()
    conn.close()

def print_all():
    conn = sql.connect('proje.db')
    cursor = conn.cursor()

    cursor.execute("""SELECT * from OGRENCI""")
    list_all = cursor.fetchall()

    conn.close()
    return list_all
