#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    operators = ['+', '-', '*', '/']

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = sys.argv[2]

    if op not in operators:
        print("Unknow operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = sub(a, b)
    elif op == '*':
        result = mul(a, b)
    else:
        result = div(a, b)

    print("{} {} {} = {}".format(a, op, b, result))
