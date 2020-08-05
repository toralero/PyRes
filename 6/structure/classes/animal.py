class Animal:

    def __init__(self, name = None, species=None, is_pet = False, age = -1):
        self.name = name
        self.species = species
        self.is_pet = is_pet
        self.age = age

    def cry(self):
        raise NotImplementedError

    def info(self):
        if self.name != None:
            print("Name:", self.name)
        if self.species != None:
            print("Species:", self.species)
        if self.is_pet:
            print("This is someone's pet.")
        else:
            print("This is a wild animal.")
        if self.age >= 0:
            print("Age", self.age)
        print("Let's hear its cry!")
        self.cry()

class Dog(Animal):
    
    def __init__(self, name = None, is_pet = False, age = -1):
        Animal.__init__(self, name, "Dog", is_pet, age)

    def cry(self):
        print("WOOF!")

class Cat(Animal):
    
    def __init__(self, name = None, is_pet = False, age = -1):
        Animal.__init__(self, name, "Cat", is_pet, age)

    def cry(self):
        print("MEOW!")

class Penguin(Animal):
    
    def __init__(self, name = None, is_pet = False, age = -1):
        Animal.__init__(self, name, "Penguin", is_pet, age)

    def cry(self):
        print("PONK!")

