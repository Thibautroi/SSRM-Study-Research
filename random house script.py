import random

# Islands and Cities with max house numbers
Ironbard = {"Vardo": 724, "Hofn": 1038, "Helvig": 557, "Bjurholm": 467, "Blonduos": 456, "Helluland": 440}
Providence = {"Hayarano": 438, "Akkeshi": 469, "Reading": 857, "Nelson": 470, "Arcadia": 1693, "Kiyobico": 616, "Takazaki": 581, "Biruwa": 547, "Shinobi": 529}
BonneSante = {"Nidoma": 492, "Talu": 398, "Pauma": 455, "Riroua": 538, "Valais": 526, "Maeva": 585, "Gordes": 507, "Kinsale": 353, "Colmar": 2075, "Vaiku": 478, "Mahuti": 1064, "Eden": 614}

# Island
islands = {"Ironbard": Ironbard, "Providence": Providence, "BonneSante": BonneSante}

def randomfunc():
    island_name = random.choice(list(islands.keys())) 
    city_name, max_houses = random.choice(list(islands[island_name].items()))
    house_number = random.randint(1, max_houses) 
    
    return island_name, city_name, house_number

def generate_random_houses(n=60, filename="random_houses.txt"):
    houses = [randomfunc() for _ in range(n)]
    
    with open(filename, "w") as file:
        for island, city, house in houses:
            line = f"Island: {island}, City: {city}, House Number: {house}\n"
            print(line.strip())  # Print to console
            file.write(line)  # Write to file

# Generate 60 random houses
generate_random_houses()
