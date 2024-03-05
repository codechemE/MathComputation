def sum_of_list(alist):
    initial_sum = 0

    for i in alist:
        initial_sum += i
    print(initial_sum)
    return initial_sum


sum_of_list([1, 3, 5, -5])
