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


def insert_player(player):

        with conn:
              curse.execute("INSERT INTO matches VALUES (:game_id,:the_game,:player_name,:playing_style,:player_points)",
                             {'game_id':mainprogram.gameid,'the_game':mainprogram.thematch,'player_name':mainprogram.name,'playing_style':player.playingstyle,'player_points':mainprogram.pts})

#conn.execute("""CREATE TABLE  my_team(
 #               game_id INTEGER,
 #               player_name TEXT,
 #               player_match_points TEXT,
 #               FOREIGN KEY (game_id) REFERENCES matches(game_id)
 #               );
 #               """)
#conn.commit()
#conn.close()
#conn.execute("""CREATE TABLE  match_players(
 #               game_id INTEGER,
 #               player_name TEXT,
 #               player_match_points TEXT,
 #               FOREIGN KEY (game_id) REFERENCES matches(game_id)
  #              );
 #               """)
#conn.commit()
#conn.close()


muttiah=players()
muttiah.player("Muttiah", "Muralitharan", "Bowler", "350", "674", "7", "45", "0", "0", "22", "534", "23", "3", "10", "7", "0")

#insert_player(muttiah)
sachin=players()
sachin.player("Sachin","Tendulkar", "Batsman", "463", "18426", "45", "87", "96", "49", "200", "154", "45", "5.1", "0", "0", "0")
#insert_player(sachin)

virender=players()
virender.player("Virender", "Sehwag", "Batsman", "104", "8273", "35", "104", "38", "15", "219", "40", "47", "6", "1", "5", "0")
#insert_player(virender)
gautam=players()
gautam.player("Gautam", "Gambhir", "Batsman", "147", "5238", "39", "85", "37", "11", "150", "0", "0", "0", "0", "0","0")
#insert_player(gautam)
virat=players()
virat.player("Virat", "Kohli", "Batsman", "254", "12169", "59", "93", "62", "43", "183", "4", "166", "5", "0", "1", "0")
#insert_player(virat)
yuvraj=players()
yuvraj.player( "Yuvraj", "Singh", "All-Rounder", "304", "8701", "36", "87", "52", "14", "150", "111", "38", "5", "1", "5", "0")
#insert_player(yuvraj)
msd=players()
msd.player("MS", "Dhoni", "Wicket-Keeper", "350", "10773", "50", "87", "73", "10", "183", "0", "0", "0", "0", "0", "256")
#insert_player(msd)
suresh=players()
suresh.player("Suresh", "Raina", "All-Rounder", "226", "5615", "35", "93", "36", "5", "116", "36", "46", "5", "0", "3", "0")
#insert_player(suresh)
harbhajan=players()
harbhajan.player("Harbhajan", "Singh", "Bowler", "236", "1237", "12", "78", "0", "0", "37", "269", "33", "4", "3", "5", "0")
#insert_player(harbhajan)
zaheer=players()
zaheer.player("Zaheer", "Khan", "Bowler", "200", "792", "11", "66", "0", "0", "34", "311", "29", "4", "1", "5", "0")
#insert_player(zaheer)
munaf=players()
munaf.player("Munaf", "Patel", "Bowler", "70", "88", "4", "63", "0", "0", "13", "86", "34", "5", "0", "5", "0")
#insert_player(munaf)
sreesanth=players()
sreesanth.player("Sreesanth", "Sreesanth", "Bowler", "27", "41", "5", "59", "0", "0", "6", "27", "33", "6", "0", "3", "0")

#insert_player(sreesanth)
tillakaratne=players()
tillakaratne.player("Tillakaratne", "Dilshan", "Batsman", "330", "10290", "40", "87", "47", "22", "161", "68", "52", "5", "0", "4", "0")
#insert_player(tillakaratne)
upul=players()
upul.player("Upul", "Tharanga", "Batsman", "235", "6951", "34", "75", "37", "15", "174", "0", "0", "0", "0", "0","0")
#insert_player(upul)
kumar=players()
kumar.player("Kumar", "Sangakkara", "Wicket-Keeper", "404", "14234", "42", "79", "93", "25", "169", "0", "0", "0", "0", "0","99")
#insert_player(kumar)
mahela=players()
mahela.player("Mahela", "Jayawardene", "Batsman", "652", "14912", "34", "79", "77", "19", "144", "8", "44", "4", "1", "6", "0")
#insert_player(mahela)
thilan=players()
thilan.player("Thilan", "Samaraweera", "Batsman", "81", "5462", "49", "80", "38", "14", "231", "0", "0", "0", "0", "0","0")
#insert_player(thilan)
chamara=players()
chamara.player("Chamara", "Kapugedera", "All-Rounder", "126", "1945", "21", "75", "7", "0", "67", "18", "39", "5", "0", "4", "0")
#insert_player(chamara)
thisara=players()
thisara.player("Thisara", "Perera", "All-Rounder", "166", "2338", "18", "93", "6", "0", "80", "169", "30", "5", "1", "5", "0")
#insert_player(thisara)
nuwan=players()
nuwan.player("Nuwan", "Kulasekara", "Bowler", "184", "1352", "10", "67", "2", "0", "73", "199", "37", "4", "0", "5", "0")
#insert_player(nuwan)
suraj=players()
suraj.player("Suraj", "Randiv", "Bowler", "12", "108", "21", "57", "0", "0", "20", "15", "35", "4", "0", "3", "0")
#insert_player(suraj)
lasith=players()
lasith.player("Lasith", "Malinga", "Bowler", "226", "1083", "9", "36", "0", "0", "56", "338", "28", "5", "1", "6", "0")
##insert_player(lasith)
muttiah=players()
muttiah.player("Muttiah", "Muralitharan", "Bowler", "350", "674", "7", "45", "0", "0", "22", "534", "23", "3", "10", "7", "0")
#insert_player(muttiah)


#def delet_player():
    #with  conn:
   #     conn.execute("DELETE from matches where player_name='Muttiah Muralitharan'")
#delet_player()

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext

def showframe(frame):
    frame.tkraise()

root =tk.Tk()
root.title("DREAM 11 KILLER ")
root.geometry("720x480")
root.configure(bg="#022ec6")
historic_matches=["2011 world cup final"]

def load_frame3():
   # print("hello world")
    curse.execute("select * from matches where the_game =:thegame", {'thegame': thegame})
    playernames = curse.fetchall()
    match_players = {}
    #for row in playernames:
    #    player_names = row[2]
   #     match_players.append(player_names)
   # print(match_players)
    #player_points(name,iruns, balls_faced, fours,sixes,wickets, economy_rate,catches, stumpings, run_outs):

    Sachin_Tendulkar=("Sachin Tendulkar",18,14,2,0,0,6,0,0,0)
    Virender_Sehwag=("Virender Sehwag", 0,2,0,0,0,0,0,0,0)
    Gautam_Gambhir = ("Gautam Gambhir", 97, 122, 9, 0, 0, 0, 0, 0, 0)
    Virat_Kohli = ("Virat Kohli", 35, 49, 4, 0, 0, 6, 0, 0, 0)
    Yuvraj_Singh = ("Yuvraj Singh", 21, 24, 2, 0, 0, 5, 0, 0, 0)
    MS_Dhoni = ("MS Dhoni", 91, 79, 8, 2, 0, 0, 0, 1, 1)
    Suresh_Raina = ("Suresh Raina", 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Harbhajan_Singh = ("Harbhajan Singh", 0, 0, 0, 0, 1, 5, 0, 0, 0)
    Zaheer_Khan = ("Zaheer Khan", 0, 0, 0, 0, 2, 6, 0, 0, 0)
    Munaf_Patel = ("Munaf Patel", 0, 0, 0, 0, 0, 4, 0, 0, 0)
    Sreesanth_Sreesanth = ("Sreesanth Sreesanth", 0, 0, 0, 0, 0, 7, 0, 0, 0)
    Tillakaratne_Dilshan = ("Tillakaratne Dilshan", 33, 49, 3, 0,1 , 5, 0, 0, 0)
    Upul_Tharanga = ("Upul Tharanga", 2, 20, 0, 0, 0, 0, 0, 0, 0)
    Kumar_Sangakkara = ("Kumar Sangakkara", 48, 67, 5, 0, 0, 0, 0, 1, 0)
    Mahela_Jayawardene = ("Mahela Jayawardene", 103, 88, 13, 0, 0, 0, 0, 0, 0)
    Thilan_Samaraweera = ("Thilan Samaraweera", 21, 34, 2, 0, 0, 0, 0, 0, 0)
    Chamara_Kapugedera = ("Chamara Kapugedera", 1, 5, 0, 0, 0, 0, 0, 0, 0)
    Thisara_Perera = ("Thisara Perera", 22, 9, 3, 1, 1, 6, 0, 0, 0)
    Nuwan_Kulasekara = ("Nuwan Kulasekara", 32, 30, 1, 1, 0, 8, 0, 0, 0)
    Suraj_Randiv = ("Suraj Randiv", 0, 0, 0, 0, 0, 5, 0, 0, 0)
    Lasith_Malinga = ("Lasith Malinga", 0, 0, 0, 0, 2, 5, 0, 0, 0)
    Muttiah_Muralitharan = ("Muttiah Muralitharan", 0, 0, 0, 0, 0, 4, 0, 0, 0)
    def player_points(name,runs, balls_faced, fours,sixes,wickets, economy_rate,catches, stumpings, run_outs):
        # Initialize total points
        total_points = 0

        # Calculate points for runs sc
        total_points += int(runs) // 2
        total_points+=int(fours)*1+int(sixes)*2

        # Check for half-century (50 runs)
        if int(runs) >= 50:
            total_points += 5

        # Check for century (100 runs)
        if int(runs) >= 100:
            total_points += 10

        # Calculate strike rate
        if int(balls_faced)==0:
            return
        else:
            strike_rate = (int(runs) / int(balls_faced)) * 100

        # Check for strike rate between 80 and 100
        if 80 <= strike_rate <= 100:
            total_points += 2

        # Check for strike rate greater than 100
        if strike_rate > 100:
            total_points += 4

        # Calculate points for hitting boundaries


        # Calculate points for each wicket
        total_points += int(wickets) * 10

        # Check for three wickets per innings
        if int(wickets) >= 3:
            total_points += 5

        # Check for five wickets or more in innings
        if int(wickets) >= 5:
            total_points += 10

        # Check for economy rate between 3.5 and 4.5
        if 3.5 <= int(economy_rate) <= 4.5:
            total_points += 4

        # Check for economy rate between 2 and 3.5
        if 2 <= int(economy_rate) < 3.5:
            total_points += 7

        # Check for economy rate less than 2
        if int(economy_rate) < 2:
            total_points += 10
        total_points += int(catches) * 10

        # Calculate points for stumpings
        total_points += int(stumpings) * 10

        # Calculate points for run-outs
        total_points += int(run_outs) * 10

        return total_points
    sachin_points=player_points("Sachin Tendulkar",18,14,2,0,0,6,0,0,0)
    #print(sachin_points)

    Virender_Sehwag = ("Virender Sehwag", 0, 2, 0, 0, 0, 0, 0, 0, 0)
    Virender_points = player_points("Virender Sehwag", 0, 2, 0, 0, 0, 0, 0, 0, 0)
    #print("Virender Sehwag Points:", Virender_points)

    Gautam_Gambhir = ("Gautam Gambhir", 97, 122, 9, 0, 0, 0, 0, 0, 0)
    Gautam_points = player_points("Gautam Gambhir", 97, 122, 9, 0, 0, 0, 0, 0, 0)
    #print("Gautam Gambhir Points:", Gautam_points)

    Virat_Kohli = ("Virat Kohli", 35, 49, 4, 0, 0, 6, 0, 0, 0)
    Virat_points = player_points("Virat Kohli", 35, 49, 4, 0, 0, 6, 0, 0, 0)
    #print("Virat Kohli Points:", Virat_points)

    Yuvraj_Singh = ("Yuvraj Singh", 21, 24, 2, 0, 0, 5, 0, 0, 0)
    Yuvraj_points = player_points("Yuvraj Singh", 21, 24, 2, 0, 0, 5, 0, 0, 0)
    #print("Yuvraj Singh Points:", Yuvraj_points)

    MS_Dhoni = ("MS Dhoni", 91, 79, 8, 2, 0, 0, 0, 1, 1)
    MS_Dhoni_points = player_points("MS Dhoni", 91, 79, 8, 2, 0, 0, 0, 1, 1)
    #print("MS Dhoni Points:", MS_Dhoni_points)

    Suresh_Raina = ("Suresh Raina", 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Suresh_Raina_points = player_points("Suresh Raina", 0, 0, 0, 0, 0, 0, 0, 0, 0)
    #print("Suresh Raina Points:", Suresh_Raina_points)

    Harbhajan_Singh = ("Harbhajan Singh", 0, 0, 0, 0, 1, 5, 0, 0, 0)
    Harbhajan_Singh_points = player_points("Harbhajan Singh", 0, 0, 0, 0, 1, 5, 0, 0, 0)
    #print("Harbhajan Singh Points:", Harbhajan_Singh_points)

    Zaheer_Khan = ("Zaheer Khan", 0, 0, 0, 0, 2, 6, 0, 0, 0)
    Zaheer_Khan_points = player_points("Zaheer Khan", 0, 0, 0, 0, 2, 6, 0, 0, 0)
    #print("Zaheer Khan Points:", Zaheer_Khan_points)

    Munaf_Patel = ("Munaf Patel", 0, 0, 0, 0, 0, 4, 0, 0, 0)
    Munaf_Patel_points = player_points("Munaf Patel", 0, 0, 0, 0, 0, 4, 0, 0, 0)
    #print("Munaf Patel Points:", Munaf_Patel_points)

    Sreesanth_Sreesanth = ("Sreesanth Sreesanth", 0, 0, 0, 0, 0, 7, 0, 0, 0)
    Sreesanth_Sreesanth_points = player_points("Sreesanth Sreesanth", 0, 0, 0, 0, 0, 7, 0, 0, 0)
    #print("Sreesanth Sreesanth Points:", Sreesanth_Sreesanth_points)

    Tillakaratne_Dilshan = ("Tillakaratne Dilshan", 33, 49, 3, 0, 1, 5, 0, 0, 0)
    Tillakaratne_Dilshan_points = player_points("Tillakaratne Dilshan", 33, 49, 3, 0, 1, 5, 0, 0, 0)
    #print("Tillakaratne Dilshan Points:", Tillakaratne_Dilshan_points)

    Upul_Tharanga = ("Upul Tharanga", 2, 20, 0, 0, 0, 0, 0, 0, 0)
    Upul_Tharanga_points = player_points("Upul Tharanga", 2, 20, 0, 0, 0, 0, 0, 0, 0)
    #print("Upul Tharanga Points:", Upul_Tharanga_points)

    Kumar_Sangakkara = ("Kumar Sangakkara", 48, 67, 5, 0, 0, 0, 0, 1, 0)
    Kumar_Sangakkara_points = player_points("Kumar Sangakkara", 48, 67, 5, 0, 0, 0, 0, 1, 0)
    #print("Kumar Sangakkara Points:", Kumar_Sangakkara_points)

    Mahela_Jayawardene = ("Mahela Jayawardene", 103, 88, 13, 0, 0, 0, 0, 0, 0)
    Mahela_Jayawardene_points = player_points("Mahela Jayawardene", 103, 88, 13, 0, 0, 0, 0, 0, 0)
    #print("Mahela Jayawardene Points:", Mahela_Jayawardene_points)

    Thilan_Samaraweera = ("Thilan Samaraweera", 21, 34, 2, 0, 0, 0, 0, 0, 0)
    Thilan_Samaraweera_points = player_points("Thilan Samaraweera", 21, 34, 2, 0, 0, 0, 0, 0, 0)
    #print("Thilan Samaraweera Points:", Thilan_Samaraweera_points)

    Chamara_Kapugedera = ("Chamara Kapugedera", 1, 5, 0, 0, 0, 0, 0, 0, 0)
    Chamara_Kapugedera_points = player_points("Chamara Kapugedera", 1, 5, 0, 0, 0, 0, 0, 0, 0)
    #print("Chamara Kapugedera Points:", Chamara_Kapugedera_points)

    Thisara_Perera = ("Thisara Perera", 22, 9, 3, 1, 1, 6, 0, 0, 0)
    Thisara_Perera_points = player_points("Thisara Perera", 22, 9, 3, 1, 1, 6, 0, 0, 0)
    #print("Thisara Perera Points:", Thisara_Perera_points)

    Nuwan_Kulasekara = ("Nuwan Kulasekara", 32, 30, 1, 1, 0, 8, 0, 0, 0)
    Nuwan_Kulasekara_points = player_points("Nuwan Kulasekara", 32, 30, 1, 1, 0, 8, 0, 0, 0)
    #print("Nuwan Kulasekara Points:", Nuwan_Kulasekara_points)

    Suraj_Randiv = ("Suraj Randiv", 0, 0, 0, 0, 0, 5, 0, 0, 0)
    Suraj_Randiv_points = player_points("Suraj Randiv", 0, 0, 0, 0, 0, 5, 0, 0, 0)
    #print("Suraj Randiv Points:", Suraj_Randiv_points)

    Lasith_Malinga = ("Lasith Malinga", 0, 0, 0, 0, 2, 5, 0, 0, 0)
    Lasith_Malinga_points = player_points("Lasith Malinga", 0, 0, 0, 0, 2, 5, 0, 0, 0)
    #print("Lasith Malinga Points:", Lasith_Malinga_points)

    Muttiah_Muralitharan = ("Muttiah Muralitharan", 0, 0, 0, 0, 0, 4, 0, 0, 0)
    Muttiah_Muralitharan_points = player_points("Muttiah Muralitharan", 0, 0, 0, 0, 0, 4, 0, 0, 0)
    #print("Muttiah Muralitharan Points:", Muttiah_Muralitharan_points)

    player_points_dict = {
        "Sachin Tendulkar":sachin_points,
        "Virender Sehwag": Virender_points,
        "Gautam Gambhir": Gautam_points,
        "Virat Kohli": Virat_points,
        "Yuvraj Singh": Yuvraj_points,
        "MS Dhoni": MS_Dhoni_points,
        "Suresh Raina": Suresh_Raina_points,
        "Harbhajan Singh": Harbhajan_Singh_points,
        "Zaheer Khan": Zaheer_Khan_points,
        "Munaf Patel": Munaf_Patel_points,
        "Sreesanth Sreesanth": Sreesanth_Sreesanth_points,
        "Tillakaratne Dilshan": Tillakaratne_Dilshan_points,
        "Upul Tharanga": Upul_Tharanga_points,
        "Kumar Sangakkara": Kumar_Sangakkara_points,
        "Mahela Jayawardene": Mahela_Jayawardene_points,
        "Thilan Samaraweera": Thilan_Samaraweera_points,
        "Chamara Kapugedera": Chamara_Kapugedera_points,
        "Thisara Perera": Thisara_Perera_points,
        "Nuwan Kulasekara": Nuwan_Kulasekara_points,
        "Suraj Randiv": Suraj_Randiv_points,
        "Lasith Malinga": Lasith_Malinga_points,
        "Muttiah Muralitharan": Muttiah_Muralitharan_points

    }


    total_points = 0


    for player_name in my_final_team:
        player_points = player_points_dict.get(player_name)
        if player_points is not None:
            total_points += player_points
        else:
            total_points += 0  # Handle the case where player_points is None (player name not found)


    # Create and configure a label to display total points
    total_points_label = tk.Label(frame3, text=f"Total Points: {total_points}", font=("Helvetica", 18))
    total_points_label.pack(pady=10)

# Create and configure a scrolled text widget to display selected players and their points
    player_details_text = scrolledtext.ScrolledText(frame3, wrap=tk.WORD, width=75, height=20)
    player_details_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Add player details to the scrolled text widget
    player_details_text.insert(tk.END, "Selected Players and Points:\n\n")
    for player_name in my_final_team:
        player_points = player_points_dict.get(player_name, 0)
        player_details_text.insert(tk.END, f"{player_name}: {player_points} points\n")

# Create a button to go back to frame2






    #print(playernames)
    #my_final_team



no_of_players=0
total_points=0
my_final_team=[]

player_type_all=()
def load_frame2():
    curse.execute("select * from matches where the_game =:thegame",{'thegame':thegame})
    #, playing_style =:theplayingstyle,,'theplayingstyle':theselectedtype
    playernames=curse.fetchall()
    print(playernames)
    for row in playernames:
        if row[1]==thegame:
            player_types=['Batsman','Wicket-Keeper','Bowler','All-Rounder']
            type_list=[]
            def player_selection():

                def style_selection(player_type):
                    selected_type=player_type.get()
                    if selected_type=='Batsman':
                       curse.execute("select * from matches where playing_style =:playing_style", {'playing_style': selected_type})
                    elif selected_type=='Bowler':
                       curse.execute("select * from matches where playing_style =:playing_style", {'playing_style': selected_type})
                    elif selected_type=='All-Rounder':
                       curse.execute("select * from matches where playing_style =:playing_style", {'playing_style': selected_type})
                    elif selected_type=='Wicket-Keeper':
                       curse.execute("select * from matches where playing_style =:playing_style", {'playing_style': selected_type})
                    typelist=curse.fetchall()
                    print(typelist)
                    player_with_points = {}
                    for row in typelist:
                        #global type_list
                        player_name=row[2]
                        player_points=row[4]
                        player_with_points[player_name]=player_points

                    global listbox
                    listbox = tk.Listbox(frame2, selectmode=tk.MULTIPLE, height=5)
                    listbox.pack(pady=10)

                    def select_player():
                        global my_final_team
                        my_team = player_type_all.get()

                        if my_team:
                            if my_team not in my_final_team and len(my_final_team) < 11:
                                my_final_team.append(my_team)
                                update_listbox()  # Don't pass the listbox widget here
                            else:
                                if my_team in my_final_team:
                                    messagebox.showinfo("Duplicate Player", f"{my_team} is already in your team.")
                                if len(my_final_team) >= 11:
                                    messagebox.showinfo("Team Full", "Your team is already full with 11 players.")

                    def update_listbox():
                        global listbox
                        listbox.delete(0, tk.END)  # Clear the listbox
                        for player in my_final_team:
                            listbox.insert(tk.END, player)

                    def show_selected_players():
                        selected_players_box = tk.Toplevel(root)
                        selected_players_box.title("Selected Players")

                        listbox = tk.Listbox(selected_players_box, selectmode=tk.SINGLE, width=40, height=10)
                        listbox.pack(padx=10, pady=20, fill=tk.BOTH, expand=True)

                        for player in my_final_team:
                            listbox.insert(tk.END, player)

                    def page3():
                        if len(my_final_team) == 11:
                           frame2.pack_forget()
                           load_frame3()  # Load frame3 content
                           showframe(frame3)  # Show frame3
                        else:
                           messagebox.showinfo("Team Full", "You need to select 11 players.")

                    # Rest of your code...

                    # Create the "Show Selected Players" button
                    show_players_button = tk.Button(frame2, text="Show Selected Players", command=show_selected_players)
                    show_players_button.pack(pady=5)

                    player_type_all = ttk.Combobox(frame2, values=list(player_with_points.keys()), width=20)
                    player_type_all.current(0)
                    player_type_all.pack(pady=2)

                    join_team = tk.Button(frame2, text="ADD IN TEAM", command=lambda: select_player())
                    join_team.pack(pady=2)



                    calculate_points=tk.Button(frame2,text="Calculate points",command=lambda : page3())
                    calculate_points.pack(pady=2)





                points_button = tk.Button(frame2, text="SHOW POINTS", command=lambda: show_points())
                points_button.pack(pady=2)

                player_type = ttk.Combobox(frame2, values=player_types, width=20)
                player_type.current(0)
                player_type.pack(pady=2)


                type_slection = tk.Button(frame2, text="Choose", command=lambda: style_selection(player_type))
                type_slection.pack(pady=2)




            def show_points():
                show_points_box = tk.Toplevel(frame2)
                show_points_box.title("THE POINTS EVERY PLAYER COST ")

                player_points=scrolledtext.ScrolledText(show_points_box,wrap=tk.WORD,width=75,height=35)
                player_points.pack(padx=10, pady=20, fill=tk.BOTH, expand=True)
                paragraph = """
Sachin Tendulkar:Batsman: 82
Virender Sehwag:Batsman:69
Gautam Gambhir:Batsman: 58
Virat Kohli:Batsman: 90 
Yuvraj Singh:All-Rounder: 90
MS Dhoni:Wicket-Keeper:90 
Suresh Raina:All-Rounder:90 
Harbhajan Singh:Bowler: 66 
Zaheer Khan:Bowler:67)
Munaf Patel:Bowler:49 
Sreesanth Sreesanth:Bowler:48 
Tillakaratne Dilshan:Batsman:74 
Upul Tharanga:Batsman:57 
Kumar Sangakkara:Wicket-Keeper: 73 
Mahela Jayawardene:Batsman:69
Thilan Samaraweera:Batsman: 65 
Chamara Kapugedera:All-Rounder:65 
Thisara Perera:All-Rounder:65 
Nuwan Kulasekara:Bowler: 52 
Suraj Randiv:Bowler:48 
Lasith Malinga:Bowler:67 
Muttiah Muralitharan:Bowler:81
                            """
                player_points.insert(tk.END, paragraph)









                #intro = tk.Label(frame2, text=" ",
               #                  fg="white",
                #                 bg="#022ec6",
                 #                font=('Ariel', 17)
                  #               )
                #intro.pack()
        else:
            return

    player_selection()



    #conn.close()

   # playerlist=[row[2] for row in playernames]


def load_frame1():
    def theteam():
        frame1.pack_forget()
        load_frame2()
        showframe(frame2)

    optins = tk.Label(frame1, text="SO YOU WANT TO PLAY :"+thegame,
                      fg="black",
                      bg="#022ec6",
                      font=('Ariel', 17)
                      )
    optins.pack()
    def show_rules():
        rulebox=tk.Toplevel(frame1)
        rulebox.title("RULES AND REWARDING SYSTEM")

        rules_and_rewarding=scrolledtext.ScrolledText(rulebox,wrap=tk.WORD,width=75,height=35)
        rules_and_rewarding.pack(padx=10,pady=20,fill=tk.BOTH,expand=True)

        paragraph = """
In your fantasy cricket app, you have 1000 points to create a team. Players have different point values. You must select:

1. 1-2 wicket-keepers
2. 2-5 batsmen
3. 1-3 all-rounders
4. 2-5 bowlers

Stay within the 1000-point limit while forming your team.

And you must select 11 players 

This is a pointing system 

Batting 
● 1 point for 2 runs scored
● Additional 5 points for half century
● Additional 10 points for century
● 2 points for strike rate (runs/balls faced) of 80-100
● Additional 4 points for strike rate>100
● 1 point for hitting a boundary (four) and 2 points for over boundary (six)

Bowling 
● 10 points for each wicket
● Additional 5 points for three wickets per innings
● Additional 10 points for 5 wickets or more in innings
● 4 points for economy rate (runs given per over) between 3.5 and 4.5
● 7 points for economy rate between 2 and 3.5
● 10 points for economy rate less than 2

Fielding
● 10 points each for catch
● 10 points each for stumping
● 10 points each for run-out

                           BEST OF LUCK
            """
        rules_and_rewarding.insert(tk.END, paragraph)

    rule_button=tk.Button(frame1,text="SHOW RULES",command=lambda :show_rules())
    rule_button.pack(pady=15)

    make_team=tk.Button(frame1,text="MAKE TEAM ",command=lambda :theteam())
    make_team.pack(pady=50)


def load_frame0():

    def thematch():
        global thegame
        thegame = select_match.get()
        print(thegame)
        takeaction = messagebox.askquestion("Confirmation", "DO YOU WANT TO PROCEED ")
        print(takeaction)
        if takeaction == "yes":
            frame0.pack_forget()
            showframe(frame1)
            load_frame1()
        else:
            showframe(frame0)
    intro = tk.Label(frame0, text="This app allows users to relive a historic cricket match",
                     fg="white",
                     bg="#022ec6",
                     font=('Ariel', 17)
                     )
    intro.pack()

    inst1 = tk.Label(frame0, text="Select the historic match ", fg="white", bg="#022ec6", font=("Ariel", 19))
    inst1.pack(pady=100)

    select_match = ttk.Combobox(frame0, values=historic_matches, width=30)
    select_match.pack(pady=15)
    select_match.set("2011 world cup final")

    choose = tk.Button(frame0, text="Choose", command=lambda: thematch())
    choose.pack(pady=10)





#frame0 code
frame0=tk.Frame(root,bg="#022ec6")
frame0.pack(pady=20)

frame1 = tk.Frame(root, bg="#022ec6")
frame1.pack(pady=20)
load_frame0()


frame2=tk.Frame(root,bg="#022ec6")
frame2.pack(pady=20)


frame3=tk.Frame(root,bg="#022ec6")
frame3.pack(pady=20)


root.mainloop()

