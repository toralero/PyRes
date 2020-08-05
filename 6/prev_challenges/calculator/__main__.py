import calculator

def main():
    print("calculator.calculate('+', 20, 10, 10, 30) =", calculator.calculate('+', 20, 10, 10, 30))
    print("calculator.calculate('-', 300, 100, 50, 125) =", calculator.calculate('-', 300, 100, 50, 125))
    print("calculator.calculate('*', 1, 2, 6, 10) =", calculator.calculate('*', 1, 2, 6, 10))
    print("calculator.calculate('/', 1000, 5, 2, 10) =", calculator.calculate('/', 1000, 5, 2, 10))

if __name__ == "__main__":
    main()
