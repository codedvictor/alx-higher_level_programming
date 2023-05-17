#!/usr/bin/python3
def search_replace(my_list, search, replace):
    update_list = my_list[:]
    for x in range(len(update_list)):
        if update_list[x] == search:
            update_list[x] = replace
    return (update_list)
