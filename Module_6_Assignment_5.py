#    ........Task 1 .........

# Create a Dictionary of Student Marks


student_marks = { "Sujit": 85,"Sonu": 78, "Manish": 92,"Vikash": 88,"Mohit": 95}

name = input("Enter the student's name: ")

if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found")
print("================")
print("\n\n\n")


# ..........Task 2 ..........

#  Demonstrate List Slicing

# Step 1: Create a list of numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Step 2: Extract the first five elements using slicing
first_five = numbers[:5]

# Step 3: Reverse the extracted elements
reversed_list = first_five[::-1]

# Step 4: Print both lists
print("Original list:", numbers)
print("Extracted first five elements:", first_five)
print("Reversed extracted elements:", reversed_list)


