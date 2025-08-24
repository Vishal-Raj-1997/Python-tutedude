# Task 1.

num = int(input("Enter a number : "))
if num % 2 == 0:
    print(num, "is Even Number")
else:
    print(num, "is Odd number")
print()
print()

#  Task 2.
sum = 0
for i in range(1, 51):
    sum += i
print("The sum of numbers from 1 to 50: ", sum)