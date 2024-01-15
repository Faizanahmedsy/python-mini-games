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

# print(players)
# value = roll()
# print(value)


