import baseball

team1Score = [0,0,0,0,0,0,0,0,0]
team2Score = [0,0,0,0,0,0,0,0,0]
lound = 1

for lound in range(9):
    team1Score[lound] = baseball.attack()
    print("攻守交代")
    