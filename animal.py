
class Animal:
    def __init__(self, species, color, name='None'):
        self.species = species
        self.color = color
        self.name = name

    def __str__(self):
        return 'Name: {}, Color: {}, Species: {}'.format(self.name, self.color, self.species)