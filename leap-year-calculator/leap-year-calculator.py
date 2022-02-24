# A simple calculation used to determine if it's a leap year.

yearInput = int(input('Input the year: '))

if yearInput % 4 != 0:
    if yearInput % 100 == 0:
        if yearInput % 400 == 0:
            print(f'{yearInput} is a leap year')
        else:
            print(f'{yearInput} is not a leap year')
    else:
        print(f'{yearInput} is a leap year!')
print(f'{yearInput} is not a leap year!')   