from classes.animal import Dog, Cat, Penguin

def main():
    doug = Dog("Doug", True, 3)
    smokey = Cat("Smokey", True, 4)
    tux = Penguin("Tux", False,  29)

    doug.info()
    print("-------")
    smokey.info()
    print("-------")
    tux.info()

if __name__ == "__main__":
    main()



