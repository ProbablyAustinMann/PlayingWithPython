import random
#this is an early Software Guild project rewritten in Python
dog_name = raw_input("What is your dog's name?\n")
breeds = []
for i in range(5):
    breeds.append(i)


for x in breeds:
    if x == 0:
        breeds[0] = random.randint(1, 100)
    elif x == 1:
        breeds[1] = random.randint(1, 100 - (breeds[0]))
    elif x == 2:
        breeds[2] = random.randint(1, 100 - (breeds[0] + breeds[1]))
    elif x == 3:
        breeds[3] = random.randint(1, 100 - (breeds[0] + breeds[1] + breeds[2]))
    elif x == 4:
        breeds[4] = (100 - (breeds[0] + breeds[1] + breeds[2] + breeds[3]))
        break

breed_one = str(breeds[0])
breed_two = str(breeds[1])
breed_three = str(breeds[2])
breed_four = str(breeds[3])
breed_five = str(breeds[4])

print("I have a highly reliable report on " + dog_name + "'s genetic origin.")
print(breed_one + " percent Bull Terrier.")
print(breed_two + " percent Akita Inu.")
print(breed_three + " percent Labrador.")
print(breed_four + " percent Beagle.")
print (breed_five + " percent Greyhound.")
print("That's quite the dog!")