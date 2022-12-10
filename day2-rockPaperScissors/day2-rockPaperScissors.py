file = open("day2-input.txt", "r");

total_score = 0
round_score = 0
for line in file:
    x, y = line.split(" ");
    oppononents_move , my_move = x.strip(), y.strip()
    if my_move == "X":
        round_score += 1
        if oppononents_move == "A":
            round_score += 3
        if oppononents_move == "C":
            round_score += 6
            
    elif my_move == "Y":
        round_score += 2
        if oppononents_move == "A":
            round_score += 6
        if oppononents_move == "B":
            round_score += 3

    elif my_move == "Z":
        round_score += 3
        if oppononents_move == "B":
            round_score += 6
        if oppononents_move == "C":
            round_score += 3
    print("round score", round_score)
    total_score += round_score
    round_score = 0

print(total_score)
    
