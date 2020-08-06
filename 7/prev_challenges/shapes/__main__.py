from shapes import Square, Triangle

def main():
    s1 = Square(4)
    s2 = Square(7)
    t1 = Triangle(3, 5)
    t2 = Triangle(7, 8)

    shape_list = s1, s2, t1, t2

    for n, shape in enumerate(shape_list):
        print("Shape", n, "is a", shape.shape_type, "with an area of", shape.area())

if __name__ == "__main__":
    main()
