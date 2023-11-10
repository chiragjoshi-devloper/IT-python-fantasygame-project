pts = 0
name = " "
gameid=1
thematch="2011 world cup final"
class players:

    def player(self, first, last, playingstyle, matches, career_runs, batting_avarage, strikerate, fifties, hundreds,
               batting_best, career_wickets, bowling_avarage , economy , fifer , bowling_best , stumpings):

        self.first = first
        self.last = last
        self.stumpings = stumpings
        self.playingstyle = playingstyle
        self.matches = matches
        self.career_runs = career_runs
        self.batting_avarage = batting_avarage
        self.strikerate = strikerate
        self.fifties = fifties
        self.hundreds = hundreds
        self.batting_best = batting_best
        self.career_wickets = career_wickets
        self.bowling_avarage = bowling_avarage
        self.economy = economy
        self.fifer = fifer
        self.bowling_best = bowling_best
        points=0
        global name
        global pts
        name=self.first+" "+self.last


        if self.playingstyle=="Batsman":
            if(int(self.matches)>=200):
                points+=5
            elif(int(self.matches)>=100):
                points+=4
            elif(int(self.matches)>=50):
                points+=3
            elif(int(self.matches)<50):
                points+=2
            if (int(self.batting_avarage) >= 50):
                points+=30
            elif(int(self.batting_avarage)>=45):
                points+=25
            elif(int(self.batting_avarage)>=40):
                points+=20
            elif (int(self.batting_avarage)>=30):
                points+=17
            elif(int(self.batting_avarage)<30):
                points+=15
            if(int(self.career_runs)>=10000):
                points+=30
            elif(int(self.career_runs)>=7500):
                points+=25
            elif (int(self.career_runs) >= 5000):
                points += 20
            elif (int(self.career_runs) >= 2500):
                points += 17
            elif(int(self.career_runs)<2500):
                points+=15
            if(int(self.strikerate)>=120):
                points+=20
            elif(int(self.strikerate)>=100):
                points+=18
            elif (int(self.strikerate) >= 90):
                points += 15
            elif (int(self.strikerate) >= 80):
                points += 12
            elif (int(self.strikerate) < 80):
                points += 10
            if(int(self.hundreds)>=40):
                points+=5
            elif(int(self.hundreds)>=30):
                points+=4
            elif (int(self.hundreds) >= 20):
                points += 3
            elif (int(self.hundreds) >= 10):
                points += 2
            elif (int(self.hundreds) >= 5):
                points += 1
            elif (int(self.hundreds) <5):
                points += 1
            if (int(self.fifties) >= 60):
                points += 5
            elif (int(self.fifties) >= 40):
                points += 4
            elif (int(self.fifties) >= 30):
                points += 3
            elif (int(self.fifties) >= 20):
                points += 2
            elif (int(self.fifties) >= 10):
                points += 1
            elif (int(self.fifties) < 10):
                points += 1
            #global pts
            pts=points

            #print(pts)
        if self.playingstyle == "Wicket-keeper":
            if (int(self.matches) >= 200):
                points += 5
            elif (int(self.matches) >= 100):
                points += 4
            elif (int(self.matches) >= 50):
                points += 3
            elif (int(self.matches) < 50):
                points += 2
            if (int(self.batting_avarage) >= 50):
                points += 30
            elif (int(self.batting_avarage) >= 45):
                points += 25
            elif (int(self.batting_avarage) >= 40):
                points += 20
            elif (int(self.batting_avarage) >= 30):
                points += 17
            elif (int(self.batting_avarage) < 30):
                points += 15
            if (int(self.career_runs) >= 10000):
                points += 30
            elif (int(self.career_runs) >= 7500):
                points += 25
            elif (int(self.career_runs) >= 5000):
                points += 20
            elif (int(self.career_runs) >= 2500):
                points += 17
            elif (int(self.career_runs) < 2500):
                points += 15
            if (int(self.strikerate) >= 120):
                points += 20
            elif (int(self.strikerate) >= 100):
                points += 18
            elif (int(self.strikerate) >= 90):
                points += 15
            elif (int(self.strikerate) >= 80):
                points += 12
            elif (int(self.strikerate) < 80):
                points += 10
            if (int(self.hundreds) >= 40):
                points += 5
            elif (int(self.hundreds) >= 30):
                points += 4
            elif (int(self.hundreds) >= 20):
                points += 3
            elif (int(self.hundreds) >= 10):
                points += 2
            elif (int(self.hundreds) >= 5):
                points += 1
            elif (int(self.hundreds) < 5):
                points += 1
            if (int(self.fifties) >= 60):
                points += 5
            elif (int(self.fifties) >= 40):
                points += 4
            elif (int(self.fifties) >= 30):
                points += 3
            elif (int(self.fifties) >= 20):
                points += 2
            elif (int(self.fifties) >= 10):
                points += 1
            elif (int(self.fifties) < 10):
                points += 1
            if(int(self.stumpings)>=50):
                points+=5
            elif(int(self.stumpings)>=30):
                points+=3
            elif(int(self.stumpings)>=10):
                points+=2
            elif(int(self.stumpings)<10):
                points+=1
            #global pts
            pts = points
        if self.playingstyle == "Bowler":
            if (int(self.matches) >= 200):
                points += 5
            elif (int(self.matches) >= 100):
                points += 4
            elif (int(self.matches) >= 50):
                points += 3
            elif (int(self.matches) < 50):
                points += 2
            if(int(self.career_wickets)>400):
                points+=30
            elif(int(self.career_wickets)>300):
                points+=25
            elif (int(self.career_wickets) > 200):
                points += 20
            elif (int(self.career_wickets) > 100):
                points += 17
            elif (int(self.career_wickets) <= 100):
                points += 15
            if (int(self.bowling_avarage)>38.0):
                points+=15
            elif(int(self.bowling_avarage)<=38.0):
                points+=17
            elif (int(self.bowling_avarage) <= 32.0):
                points += 20
            elif (int(self.bowling_avarage) <= 28.0):
                points += 25
            elif (int(self.bowling_avarage) <= 25.0):
                points += 30
            if (int(self.economy)>9):
                points+=12
            elif(int(self.economy)<=9):
                points+=14
            elif (int(self.economy) <= 8):
                points += 16
            elif (int(self.economy) <= 7):
                points += 18
            elif (int(self.economy) <= 6):
                points += 20
            if int(self.fifer)>6:
                points+=15
            elif int(self.fifer)>=4:
                points+=12
            elif int(self.fifer) >= 3:
                points += 10
            elif int(self.fifer) >= 2:
                points += 8
            elif int(self.fifer) >= 1:
                points += 6
            #global pts
            pts = points

        if self.playingstyle=="All-rounder":
            if (int(self.matches) >= 200):
                points += 5
            elif (int(self.matches) >= 100):
                points += 4
            elif (int(self.matches) >= 50):
                points += 3
            elif (int(self.matches) < 50):
                points += 2
            if (int(self.batting_avarage) >= 45):
                points += 20
            elif (int(self.batting_avarage) >= 38):
                points += 15
            elif (int(self.batting_avarage) >= 35):
                points += 12
            elif (int(self.batting_avarage) < 35):
                points += 10
            if (int(self.career_runs) >= 10000):
                points += 20
            elif (int(self.career_runs) >= 7500):
                points += 15
            elif (int(self.career_runs) >= 5000):
                points += 12
            elif (int(self.career_runs) >= 2500):
                points += 10
            elif (int(self.career_runs) < 2500):
                points += 8
            if (int(self.strikerate) >= 120):
                points += 10
            elif (int(self.strikerate) >= 100):
                points += 8
            elif (int(self.strikerate) >= 90):
                points += 6
            elif (int(self.strikerate) >= 80):
                points += 5
            elif (int(self.strikerate) < 80):
                points += 4
            if (int(self.hundreds) >= 40):
                points += 5
            elif (int(self.hundreds) >= 30):
                points += 4
            elif (int(self.hundreds) >= 20):
                points += 3
            elif (int(self.hundreds) >= 10):
                points += 2
            elif (int(self.hundreds) >= 5):
                points += 1
            elif (int(self.hundreds) < 5):
                points += 1
            if (int(self.fifties) >= 60):
                points += 5
            elif (int(self.fifties) >= 40):
                points += 4
            elif (int(self.fifties) >= 30):
                points += 3
            elif (int(self.fifties) >= 20):
                points += 2
            elif (int(self.fifties) >= 10):
                points += 1
            elif (int(self.fifties) < 10):
                points += 1
            if (int(self.career_wickets) > 400):
                points += 15
            elif (int(self.career_wickets) > 300):
                points += 12
            elif (int(self.career_wickets) > 200):
                points += 10
            elif (int(self.career_wickets) > 100):
                points += 8
            elif (int(self.career_wickets) <= 100):
                points += 8
            if (int(self.bowling_avarage) > 38.0):
                points += 8
            elif (int(self.bowling_avarage) <= 38.0):
                points += 10
            elif (int(self.bowling_avarage) <= 32.0):
                points += 12
            elif (int(self.bowling_avarage) <= 28.0):
                points += 15
            elif (int(self.bowling_avarage) <= 25.0):
                points += 17
            if (int(self.economy) > 9):
                points += 4
            elif (int(self.economy) <= 9):
                points += 5
            elif (int(self.economy) <= 8):
                points += 6
            elif (int(self.economy) <= 7):
                points += 7
            elif (int(self.economy) <= 6):
                points += 7
            if int(self.fifer) > 6:
                points += 8
            elif int(self.fifer) >= 4:
                points += 6
            elif int(self.fifer) >= 3:
                points += 4
            elif int(self.fifer) >= 2:
                points += 3
            elif int(self.fifer) >= 1:
                points +=2
            #global pts
            pts = points

muttiah=players()
muttiah.player("Muttiah", "Muralitharan", "Bowler", "350", "674", "7", "45", "0", "0", "22", "534", "23", "3", "10", "7", "0")
gameid+=1

sachin=players()
sachin.player("Sachin","Tendulkar", "Batsman", "463", "18426", "45", "87", "96", "49", "200", "154", "45", "5.1", "0", "0", "0")
gameid+=1
virender=players()
virender.player("Virender", "Sehwag", "Batsman", "104", "8273", "35", "104", "38", "15", "219", "40", "47", "6", "1", "5", "0")
gameid+=1
gautam=players()
gautam.player("Gautam", "Gambhir", "Batsman", "147", "5238", "39", "85", "37", "11", "150", "0", "0", "0", "0", "0","0")
gameid+=1
virat=players()
virat.player("Virat", "Kohli", "Batsman", "254", "12169", "59", "93", "62", "43", "183", "4", "166", "5", "0", "1", "0")
gameid+=1
yuvraj=players()
yuvraj.player( "Yuvraj", "Singh", "All-Rounder", "304", "8701", "36", "87", "52", "14", "150", "111", "38", "5", "1", "5", "0")
gameid+=1
msd=players()
msd.player("MS", "Dhoni", "Wicket-Keeper", "350", "10773", "50", "87", "73", "10", "183", "0", "0", "0", "0", "0", "256")
gameid+=1
suresh=players()
suresh.player("Suresh", "Raina", "All-Rounder", "226", "5615", "35", "93", "36", "5", "116", "36", "46", "5", "0", "3", "0")
gameid+=1
harbhajan=players()
harbhajan.player("Harbhajan", "Singh", "Bowler", "236", "1237", "12", "78", "0", "0", "37", "269", "33", "4", "3", "5", "0")
gameid+=1
zaheer=players()
zaheer.player("Zaheer", "Khan", "Bowler", "200", "792", "11", "66", "0", "0", "34", "311", "29", "4", "1", "5", "0")
gameid+=1
munaf=players()
munaf.player("Munaf", "Patel", "Bowler", "70", "88", "4", "63", "0", "0", "13", "86", "34", "5", "0", "5", "0")
gameid+=1
sreesanth=players()
sreesanth.player("Sreesanth", "Sreesanth", "Bowler", "27", "41", "5", "59", "0", "0", "6", "27", "33", "6", "0", "3", "0")

gameid+=1
tillakaratne=players()
tillakaratne.player("Tillakaratne", "Dilshan", "Batsman", "330", "10290", "40", "87", "47", "22", "161", "68", "52", "5", "0", "4", "0")
gameid+=1
upul=players()
upul.player("Upul", "Tharanga", "Batsman", "235", "6951", "34", "75", "37", "15", "174", "0", "0", "0", "0", "0","0")
gameid+=1
kumar=players()
kumar.player("Kumar", "Sangakkara", "Batsman", "404", "14234", "42", "79", "93", "25", "169", "0", "0", "0", "0", "0","99")
gameid+=1
mahela=players()
mahela.player("Mahela", "Jayawardene", "Batsman", "652", "14912", "34", "79", "77", "19", "144", "8", "44", "4", "1", "6", "0")
gameid+=1
thilan=players()
thilan.player("Thilan", "Samaraweera", "Batsman", "81", "5462", "49", "80", "38", "14", "231", "0", "0", "0", "0", "0","0")
gameid+=1
chamara=players()
chamara.player("Chamara", "Kapugedera", "All-Rounder", "126", "1945", "21", "75", "7", "0", "67", "18", "39", "5", "0", "4", "0")
gameid+=1
thisara=players()
thisara.player("Thisara", "Perera", "All-Rounder", "166", "2338", "18", "93", "6", "0", "80", "169", "30", "5", "1", "5", "0")
gameid+=1
nuwan=players()
nuwan.player("Nuwan", "Kulasekara", "Bowler", "184", "1352", "10", "67", "2", "0", "73", "199", "37", "4", "0", "5", "0")
gameid+=1
suraj=players()
suraj.player("Suraj", "Randiv", "Bowler", "12", "108", "21", "57", "0", "0", "20", "15", "35", "4", "0", "3", "0")
gameid+=1
lasith=players()
lasith.player("Lasith", "Malinga", "Bowler", "226", "1083", "9", "36", "0", "0", "56", "338", "28", "5", "1", "6", "0")
gameid+=1

#print(pts)
#print(name)