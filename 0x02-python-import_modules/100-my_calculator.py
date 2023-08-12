#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as mycal
    v = sys.argv
    if len(v) != 4:
        print("Usage: {} <a> <operator> <b>".format(v[0]))
        sys.exit(1)
    if v[2] == '+':
        sol = mycal.add(int(v[1]), int(v[3]))
    elif v[2] == '-':
        sol = mycal.sub(int(v[1]), int(v[3]))
    elif v[2] == '*':
        sol = mycal.mul(int(v[1]), int(v[3]))
    elif v[2] == '/':
        sol = mycal.div(int(v[1]), int(v[3]))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print(f"{v[1]} {v[2]:s} {v[3]} = {sol}")
    sys.exit(0)
