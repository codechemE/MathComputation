nums = range(0, 10)

odd = [num for num in nums if num % 2 == 1]
even = [num for num in nums if num % 2 == 0]
print(f'the odd numbers are : {odd}')
print(f'the even numbers are : {even}')
