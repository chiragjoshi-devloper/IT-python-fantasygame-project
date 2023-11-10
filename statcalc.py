import sqlite3
import mainprogram
from mainprogram import players

conn=sqlite3.connect("players.db")
curse=conn.cursor()
#conn.execute("""CREATE TABLE matches(
 #               game_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
 #              the_game TEXT,
 #              player_name TEXT,
 #              playing_style TEXT,
 #              player_points INTEGER
 #               )""")
#conn.commit()
def insert_player():
    pass

#conn.execute("""CREATE TABLE  my_team(
 #               game_id INTEGER,
 #               player_name TEXT,
 #               player_match_points TEXT,
 #               FOREIGN KEY (game_id) REFERENCES matches(game_id)
 #               );
 #               """)
#conn.commit()
#conn.close()
