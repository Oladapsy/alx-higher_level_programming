#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """ print x element of a list
        
        Args: 
        my_list (list): list to print elements from
        x: the number of element to print 

        Return: the number of element printed 
    """
    num = 0
    try:
        for item in range(x):
            print("{}".format(my_list[item]), end='')
            num += 1
    except IndexError:
        pass
    print()
    return num
