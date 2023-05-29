#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlisting = []
    for i in range(list_length):
        try:
            newlisting.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
            newlisting.append(0)
            continue
        except ArithmeticError:
            print("division by 0")
            newlisting.append(0)
            continue
        except IndexError:
            print("out of range")
            newlisting.append(0)
            continue
        finally:
            pass
    return newlisting
