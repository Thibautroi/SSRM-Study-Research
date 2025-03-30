import random

def random_person_in_house():
    num_people = int(input("Please enter the total number of people: "))
    person_number = random.randint(1, num_people)
    print(f"Selected person: {person_number}")

def random_person_in_house():
    while True:
        num_people = input("Please enter the total number of people: ")
        num_people = int(num_people)
        person_number = random.randint(1, num_people)
        print(f"Selected person: {person_number}")

random_person_in_house()
