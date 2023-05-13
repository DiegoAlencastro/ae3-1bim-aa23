import os
import sqlite3

db_filename = 'ejemplo02.db'

db_is_new = not os.path.exists(db_filename)

conn = sqlite3.connect(db_filename)

if db_is_new:
    print('Se creo base de datos con nombre: '+db_filename)
else:
    print('Base de datos '+db_filename+ ' ya existe')

conn.close()
