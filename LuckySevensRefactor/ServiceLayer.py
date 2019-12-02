from RollDie import roll_die

#this is the main controller that handles the win/lose logic
def run_program():
    roll_count = 0
    roll_max = 0
#user inputs imaginary money
    user_money = input("Enter money you'd like to waste\n")
    max_dollars = user_money
#the script continues to run until you run out of money
    while user_money > 0:
        roll_die()
        roll_count += 1
        if roll_die == 7:
            user_money += 4
            roll_count += 1
        else:
            user_money -= 1
            roll_count += 1

        if user_money > max_dollars:
            max_dollars = user_money
            roll_max = roll_count

#after you go broke, you are told how many rolls you lasted and when you should have quit
    print("You went broke after %i rolls." % roll_count)
    print("You should have stopped at %i rolls when you had %i dollars." %(roll_max, max_dollars))