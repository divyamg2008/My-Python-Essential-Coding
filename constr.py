class Animals:
    def __init__(self, name, food, colour):
        self._name = name
        self._food = food
        self._colour = colour

    def name(self):
        return "the name is: " + self._name

    def food(self):
        return "the food is: " + self._food

    def colour(self):
        return "the colour is: " + self._colour


dog = Animals("kukru", "egg", "brown")
cat = Animals("mili", "milk", "white")
cow = Animals("malu", "grass", "black")

print(dog.name(), dog.food(), dog.colour())
print(cow.name(), cow.food(), cow.colour())
print(cat.name(), cat.food(), cat.colour())

print(isinstance(dog, Animals))
