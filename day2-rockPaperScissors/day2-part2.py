file = open("day2-input.txt", "r");

moves = {"Rock" : "A", "Paper": "B", "Scissor": "C"}
outcomes = {"Lose": "X", "Draw": "Y", "Win": "Z"}
my_points = {"Rock": 1, "Paper": 2, "Scissor": 3}

total_score = 0
round_score = 0
for line in file:
    x, y = line.split(" ");
    oppononents_move , outcome = x.strip(), y.strip()
    if outcome == outcomes["Lose"]:
        if oppononents_move == moves["Rock"]:
            round_score += my_points["Scissor"]
        elif oppononents_move == moves["Paper"]:
            round_score += my_points["Rock"]
        else:
            round_score += my_points["Paper"]
            
    elif outcome == outcomes["Draw"]:
        round_score += 3
        if oppononents_move == moves["Rock"]:
            round_score += my_points["Rock"]
        elif oppononents_move == moves["Paper"]:
            round_score += my_points["Paper"]
        else:
            round_score += my_points["Scissor"]

    elif outcome == outcomes["Win"]:
        round_score += 6
        if oppononents_move == moves["Rock"]:
            round_score += my_points["Paper"]
        elif oppononents_move == moves["Paper"]:
            round_score += my_points["Scissor"]
        else:
            round_score += my_points["Rock"]

    total_score += round_score
    round_score = 0

print(total_score)
    
