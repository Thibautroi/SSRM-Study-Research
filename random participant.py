import random

def random_person_in_house():
    while True:
        x = input("Please enter the total number of people: ")
        x = int(x)
        personnumber = random.randint(1, x)
        print(f"Selected person: {personnumber}")

random_person_in_house()
