def user_input():
    try:
        value = eval(input("Input anything "))
        print(f"You have inputted: {value} of {type(value)}")
    except TypeError as str:
        raise TypeError("Gotta be a float man")



user_input()
