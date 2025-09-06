#  ..........Task 1 ..........

def factorial(n):
    if(n == 1):
        return 1

    return n * factorial(n - 1)


n = int(input("Enter a number: "))
factorial(5)
print(f"factorial of {5} is ", factorial(5))




# ..............Task 2 .........

import math

num = float(input("Enter a number: "))

square_root = math.sqrt(num)
natural_log = math.log(num)
sine_value = math.sin(num)

print("Square root of", num, "is:", square_root)
print("Natural log of", num, "is:", natural_log)
print("Sine of", num, "is:", sine_value)
