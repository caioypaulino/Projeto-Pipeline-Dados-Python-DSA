# Versão 1

import csv 
import sqlite3

with open('producao_alimentos.csv', 'r') as file:

    reader = csv.reader(file)

    next(reader)

    conn = sqlite3.connect('database.db')

    conn.execute('DROP TABLE IF EXISTS producao')

    conn.execute('''CREATE TABLE producao (
                        produto         TEXT,
                        quantidade      INTEGER,
                        preco_medio     REAL,
                        receita_total   REAL
                    )''')

    for row in reader:
        conn.execute('INSERT INTO producao (produto, quantidade, preco_medio, receita_total) VALUES (?, ?, ?, ?)', row)

    conn.commit()
    conn.close()

print("Job v1 Completed Successfully!")