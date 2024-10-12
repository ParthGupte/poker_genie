import sqlite3

sqliteConnection = sqlite3.connect('ranking.db')
cursor = sqliteConnection.cursor()
counter = 0

# Table Creation

# CREATE TABLE "sqlb_temp_table_3" (
# 	"rank"	INTEGER,
# 	"card1"	TEXT,
# 	"card2"	TEXT,
# 	"card3"	TEXT,
# 	"card4"	TEXT,
# 	"card5"	TEXT,
# 	"id_"	INTEGER,
# 	PRIMARY KEY("id_" AUTOINCREMENT)
# );

#Insert into table

def insertHandsIntoDBase(rankCounter:int, handList: list):
    global counter
    query = "INSERT into poker_ranking(rank, card1, card2, card3, card4, card5) VALUES ('{}', '{}', '{}', '{}' ,'{}', '{}'); ".format(rankCounter,handList[0],handList[1],handList[2],handList[3],handList[4])
    result = cursor.execute(query)
    counter+=1
    if counter % 10000 == 0:
        print("Commit",counter)
        sqliteConnection.commit()
    
def commiter():
    sqliteConnection.commit()
    sqliteConnection.close()
# INSERT into poker_ranking(rank, card1, card2, card3, card4, card5) VALUES (rankCounter, card1, card2, card3 ,card4, card5); 
# print(insertHandsIntoWoman(3,["2","3","4","5","6"]))