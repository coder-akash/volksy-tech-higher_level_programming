#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    args = argv[1:]
    if len(args) == 3:
        a, b, c = args
        if b == '+':
            res = add(int(a), int(c))
        elif b == '-':
            res = sub(int(a), int(c))
        elif b == '*':
            res = mul(int(a), int(c))
        elif b == '/':
            res = div(int(a), int(c))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        print('{} {} {} = {}'.format(a, b, c, res))
        exit()
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
