import random; # This package is used for random numbers


def roll():
    min_value = 1;
    max_value = 6;
    # randint is a function that takes two arguments lower limit and upper limit
    roll = random.randint(min_value, max_value)

    return roll;





while True:
    players = input("Enter the number of players (2-4): ")
    # isdigit is used to check weather the input is a number or not 
    if players.isdigit(): 
        # this will convert the string (which is a digit) in to a integer data type
        players = int(players) 
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 to 4 players")


    else: 
        print("Input must be a number, please try again")



max_score = 50;
# This list will store the scores of players
player_scores = [0 for _ in range(players)]


while max(player_scores) < max_score: 


    for player_idx in range(players):
        print("\nPlayer number", player_idx +  1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
        
            should_roll = input("Would you like to roll (y)?")
            if should_roll.lower() != "y":
                break
            value = roll()
            if value == 1:
                print("Your value is 1, Turn Done!")
                current_score = 0
                break
            else: 
                current_score += value
                print("You rolled a", value)
            
        
            print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:" , player_scores[player_idx])



max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1 , "is the winner with the score of:", max_score)