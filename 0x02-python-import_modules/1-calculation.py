#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as mycal
    a = 10
    b = 5
    print("{} + {} = {}".format(int(a), int(b), mycal.add(a, b)))
    print("{} - {} = {}".format(int(a), int(b), mycal.sub(a, b)))
    print("{} * {} = {}".format(int(a), int(b), mycal.mul(a, b)))
    print("{} / {} = {}".format(int(a), int(b), mycal.div(a, b)))
