import random; # This package is used for random numbers


def roll():
    min_value = 1;
    max_value = 6;
    # randint is a function that takes two arguments lower limit and upper limit
    roll = random.randint(min_value, max_value)

    return roll;


value = roll()

print(value)