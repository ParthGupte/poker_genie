import sqlite3

sqliteConnection = sqlite3.connect('ranking.db')
cursor = sqliteConnection.cursor()
print('DB Init')