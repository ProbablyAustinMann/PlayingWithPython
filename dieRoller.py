import random


def roll_die():
    x = random.randint(1, 6)
    y = random.randint(1, 6)
    return x + y

roll_count = 0
roll_max = 0
user_money = input("Enter money you'd like to waste\n")
max_dollars = user_money
while user_money > 0:
    roll_die()
    roll_count += 1
    if roll_die() == 7:
        user_money += 4
        roll_count += 1
    else:
        user_money -= 1
        roll_count += 1

    if user_money > max_dollars:
        max_dollars = user_money
        roll_max = roll_count

print("You went broke after %i rolls." % roll_count)
print("You should have stopped at %i rolls when you had %i dollars." %(roll_max, max_dollars))
