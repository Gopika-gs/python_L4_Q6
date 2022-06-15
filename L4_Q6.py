def sum_of_list(my_list):
    if not my_list:
        return 0
    elif len(my_list) == 1:
        return my_list[0]
    else:
        return my_list[0] + sum_of_list(my_list[1:])

print(sum_of_list([1,2,3,4,5,6,7]))