


def ddt(input_num = 1):
    try:
        if (input_num <= 0):
            raise("Please provide a positive decimal number less than 10")
        elif (input_num > 9):
            raise("Digit should be less than 9.")    
        else:
            final_number = calculate(input_num)
            return final_number
    except ValueError as err:
        print(f"Error {err}")


def calculate(x):
    result = 0
    for i in range(1, 5):
        num = int(str(x) * i)
        result += num
    return result

print(ddt(2))
print(ddt(3))

    


