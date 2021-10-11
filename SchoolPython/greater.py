first_number = input("Enter number 1: ")
second_number = input("Enter number 2: ")

if first_number > second_number:
    print("Number 1 is greater")
elif second_number > first_number:
    print("Second number is greater")
elif first_number == second_number:
    print('Both numbers are equal')
else:
    print("Invalid!")