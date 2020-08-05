def check_if_numbers(n_list):
    for n in n_list:
        if isinstance(n, int):
            continue
        else:
            return False
    return True

def calculate(op, init, *n_list):
    if isinstance(op, str) and isinstance(init, int) and check_if_numbers(n_list):
        total = init
        if op == '+':
            for n in n_list:
                total += n
            return total
        elif op == '-':
            for n in n_list:
                total -= n
            return total
        elif op == '*':
            for n in n_list:
                total *= n
            return total
        elif op == '/':
            for n in n_list:
                total /= n
            return total
        else:
            raise ValueError("The first argument should be a +, -, * or /")
    else:
        raise TypeError("Please check that all your inputs afterwards are integers.")
