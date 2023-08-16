#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for i in my_list:
        new.append(i if i != search else replace)
    return new
