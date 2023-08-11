#!/usr/bin/python3

if __name__ == "__main__":
    from importlib import import_module

    dlib = import_module('hidden_4')
    # method 1
    for i in list(m for m in dir(dlib) if m[:2] != "__"):
        print(i)

    # metho 2
    for i in dir(dlib):
        if i[:2] != "__":
            # print("{}".format(i))
            pass  # to be romoved together with the comment on
        # print function in line 14
