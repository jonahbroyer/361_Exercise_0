"""
Jonah Broyer

Show a list of Formula 1 drivers sorted by last name
and then sorted by their number (don't forget to display 'YEET! next to
Lewis Hamilton).
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


def alphabet_header():
    print("2021 F1 Drivers - Alphabetical\n"
          "==============================")


def numeric_header():
    print("2021 F1 Drivers - Numerical\n"
          "===========================")


def sort_lastname():
    drivers.sort(key=lambda x: x.split()[1])
    print('\n'.join(drivers) + '\n')


def sort_drivernum():
    # sorted function discovered on
    # https://stackoverflow.com/questions/49232823/python-sort-a-list-of-strings-composed-of-letters-and-numbers
    num_sort = sorted(drivers, key=lambda x: int(''.join([i for i in x if i.isdigit()])))
    print('\n'.join(num_sort))


if __name__ == '__main__':
    header()
    alphabet_header()
    sort_lastname()
    numeric_header()
    sort_drivernum()
