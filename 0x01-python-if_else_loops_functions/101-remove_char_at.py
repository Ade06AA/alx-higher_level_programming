#!/usr/bin/python3
def remove_char_at(str, n):
    for i in range(str):
        if i == n:
            continue;
        new += str[i]
    return new
print(remove_char_at("ADENOWO", 2))
print(remove_char_at("ADENOWO", -2))
