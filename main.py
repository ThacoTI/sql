import sqlite3

from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'sqlite3.db'

DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()


#cuidado: fazendo delete sem where

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)

connection.commit()
#valores na coluna da tabela

cursor.execute(
    f'INSERT INTO  {TABLE_NAME} (id, name, weight)'
    ' VALUES (NULL, "mateus", 9.9), (NULL, "lazar0", 70)'
    )

connection.commit()


cursor.close()
connection.close()