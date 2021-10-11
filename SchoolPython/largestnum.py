num_one = int(input('Enter no. 1: '))
num_two = int(input('Enter no. 2: '))
num_three = int(input('Enter no. 3: '))
num_four = int(input('Enter no. 4: '))

if num_one > num_two:
    print("one is greater")
elif num_two > num_three:
    print('second is greater')
elif num_three > num_four:
    print('three is greater')
elif num_one == num_two == num_three == num_four:
    print('All number are equal')
else:
    print('Four is greater')