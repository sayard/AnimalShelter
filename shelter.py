from animal import Animal

currentCommand = ''
placesOccupied = 0
maxAvailablePlaces = 15
animals = []


def execute_command(command):
    if command == 'help':
        print("""
            Available commands:
            status - shows the current status of the shelter
            add - adds new animal
            remove [index] - removes animal at given index
            list_animals - lists all animals inside the shelter
            exit - exit shelter manager
        """)
    elif command == 'status':
        places_available = maxAvailablePlaces - placesOccupied
        print('Current status: {} places occupied, {} places available'.format(placesOccupied, places_available))
    elif command == 'add':
        if placesOccupied < maxAvailablePlaces:
            if add_animal():
                print('Adding successful')
            else:
                print('Could not add animal please try again')
        else:
            print('All places are filled!')
    elif command[0:6] == 'remove':
        index_to_delete = int(command.split(' ')[1]) - 1
        remove_animal(index_to_delete)
    elif command == 'list_animals':
        print_animals()
    else:
        print("Command not recognised try typing 'help' for available commands")


def add_animal():
    global placesOccupied
    species = input('Animal Species: ')
    color = input('Animal Color: ')
    name = input('Animal Name(Leave empty if none): ')
    if name == '':
        animals.append(Animal(species, color))
        placesOccupied += 1
        return True
    else:
        animals.append(Animal(species, color, name))
        placesOccupied += 1
        return True


def print_animals():
    if len(animals) > 0:
        print(40 * '-')
        for i, animal in enumerate(animals):
            print('[{}]'.format(i + 1), animal)
            print(20 * '*')
        print(40 * '-')
    else:
        print('The shelter is empty')


def remove_animal(index_to_delete):
    global placesOccupied
    try:
        del animals[index_to_delete]
        print('Removing successful')
        placesOccupied -= 1
    except ValueError:
        print('Index has to be a number')
    except IndexError:
        print('Animal with given index does not exist')


print("Welcome to animal shelter manager 2000. Type 'help' for help, type 'exit' to exit")

while currentCommand != 'exit':
    currentCommand = input()
    execute_command(currentCommand)
