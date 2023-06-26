#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    list_length = min(len(my_list_1), len(my_list_2))
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return new_list
