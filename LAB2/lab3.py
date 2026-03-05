#TASK1
x = int(input('Enter a positive integer greater than 1: '))

if x <= 1:
    print('You entered an invalid value.')
else:
    count = 0

    print(x, end=' → ')

    while x != 1:
        if x % 2 == 0:
            x //= 2
        else:
            x = x * 3 + 1
        
        print(x, end=' → ')
        count += 1

    print('\nTotal steps:', count)

#TASK2  

