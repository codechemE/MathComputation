list_int = [1, 2, 3, 4, 5]
list_int.append(6)
list_int.pop(0)

print(list_int)

list_int_a = [1, 2, 3]
list_int_b = [4, 5, 6]

concatenated_list = list_int_a + list_int_b

print(concatenated_list)

rev_list = [1, 2, 3, 4, 5]
rev_list.reverse()

print(rev_list)

min_max_list = [1, 2, 3, 4, 5]

maximum = 0
minimum = 5

for i in min_max_list:
    if i > maximum:
        maximum = i

for i in min_max_list:
    if i < minimum:
        minimum = i

print(minimum, maximum)

even_odd_list = [1, 2, 3, 4, 5, 6, 7, 8]
even_list = []

for i in even_odd_list:
    if i % 2 == 0:
        even_list.append(i)

print(even_list)

new_list = even_odd_list[1:5]

print(new_list)

another_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

another_new_list = another_list[-3:]

print(another_new_list)

string_list = ["apple", "banana", "cherry", "date"]
string_sublist = [string_list[0], string_list[-1]]

print(string_sublist)