#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        my_set = set()
        for items in my_list:
            my_set.add(items)
        return sum(my_set)
