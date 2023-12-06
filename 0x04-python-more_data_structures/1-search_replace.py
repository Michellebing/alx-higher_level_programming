#!/urs/bin/python3

def search_replace(my_list, search, replace):
    my = list(my_list)
    for i in range(len(my)):
        if my[i] == search:
            my[i] = replace
            return my
