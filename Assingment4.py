# .....Task 01 ......

try:

    with open("sample.txt", "r") as file:
        # Print each line
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
print("\n\n\n")


#  ...........Task 02 ...........


data = input("Write something here : ")

with open("output.txt", "w") as file:
    file.write("Hello Python\n")

with open("output.txt", "a") as file:
    file.write("Learning file handling in Python.\n")

print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
