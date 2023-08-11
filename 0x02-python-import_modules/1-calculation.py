#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as mycal
    a = 10
    b = 5
    print(f"{a:d} + {b:d} = {mycal.add(a, b):d}")
    print(f"{a:d} - {b:d} = {mycal.sub(a, b):d}")
    print(f"{a:d} * {b:d} = {mycal.mul(a, b):d}")
    print(f"{a:d} / {b:d} = {mycal.div(a, b):d}")
