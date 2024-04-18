div_7 = [num for num in range(0, 1001) if num % 7 == 0]
print(div_7)

numbers_odd_even = ["even" if num & 2 == 0 else "odd" for num in range(0, 20)]
print(numbers_odd_even)

contains_3 = [num for num in range(1, 1001) if '3' in str(num)]

test_string = "Practice Problems to Drill List Comprehensive in Your Head"

num_spaces = [letter for letter in test_string if letter == " "]
print(len(num_spaces))


