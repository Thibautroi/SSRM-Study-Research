import random

def random_person_in_house():
    while True:
        num_people = input("Please enter the total number of people: ")
        num_people = int(num_people)
        personnumber = random.randint(1, num_people)
        print(f"Selected person: {personnumber}")

random_person_in_house()
