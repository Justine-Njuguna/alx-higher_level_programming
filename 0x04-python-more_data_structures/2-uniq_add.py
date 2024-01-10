#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set()
    result_sum = 0

    for num in my_list:
        if num not in unique_set:
            unique_set.add(num)
            result_sum += num

    return result_sum
