"""
Show a list of Formula 1 drivers sorted by last name
and sorted by their number
"""

drivers = ["Max Verstappen 33 Red Bull", "Lewis Hamilton 44 Mercedes YEET!", "Valtteri Bottas 77 Mercedes",
           "Lando Norris 4 McLaren", "Sergio Perez 11 Red Bull", "Charles Leclerc 16 Ferrari",
           "Carlos Sainz 55 Ferrari", "Daniel Ricciardo 3 McLaren", "Pierre Gasly 10 AlphaTauri",
           "Fernando Alonso 14 Alpine", "Esteban Ocon 31 Alpine", "Sebastian Vettel 5 Aston Martin",
           "Lance Stroll 18 Aston Martin", "Yuki Sonoda 22 AlphaTauri", "George Russell 63 Williams",
           "Nicholas Latifi 6 Williams", "Kimi Raikkonen 7 Alfa Romeo", "Antonio Giovinazzi 99 Alfa Romeo",
           "Mick Schumacher 47 Haas", "Nikita Mazepin 9 Haas"]


def header():
    print("2021 F1 Drivers\n"
          "===============\n")


def print_lastname():
    drivers.sort()
    print('\n'.join(drivers))


def print_drivernum():
    # sorted function discovered on
    # https://stackoverflow.com/questions/49232823/python-sort-a-list-of-strings-composed-of-letters-and-numbers
    num_sort = sorted(drivers, key=lambda x: int(''.join([i for i in x if i.isdigit()])))
    print('\n' + '\n'.join(num_sort))


if __name__ == '__main__':
    header()
    print_lastname()
    print_drivernum()
