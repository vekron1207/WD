number = int(input('Enter number here: '))


for counter in range(number+1):

    if counter % 3 == 0 and counter % 5 == 0:
        print(f'Fizzbuzz: {counter}')
        continue
    # to check if program running correctly

    elif counter % 5 == 0:
        print(f'Buzz: {counter}')
        continue
    elif counter % 3 == 0: 
        print(f'Fizz: {counter}')
        continue
    print(counter)
