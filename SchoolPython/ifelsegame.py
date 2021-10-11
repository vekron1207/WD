import random

name = input(str('Enter your name: '))
vowel = ['a','e','i','o','u']
print(f'Hello {name}')

if name[0] in vowel:
    print(f'Aha! Oho! Uhu! Ihi! etc", your name ({name}) begins with a vowel! {name[0]}')
else:
    print(f'{name} Please insert more funny joke here i cant think of one')


random_number = int(input('Enter a number from 1-10: '))
rndm_num = random.randint(0, 10)
print(f'Winning Number is:.... ' +str(rndm_num))

if rndm_num == random_number:
    print("U won my man")
elif random_number > 10:
    print("U can't read my man?")
else:
    print("Tough luck bro")