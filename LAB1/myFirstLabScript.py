x= input ('What is your name?')
print('hello ' + x)

y= input ('What is your Student ID?')
print('Your ID is ' + y)

z= int (input ( ' input a large integer representing a total number of seconds ' ))

hours = z // 3600
remaining_seconds = z % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(z , 'seconds is' , hours , 'hours ,' , minutes , 'minutes, and ' , seconds , 'seconds.')

coordinate_x1 = float(input ('enter x1'))
coordinate_x2 = float(input ('enter x2'))
coordinate_y1 = float(input ('enter y1'))
coordinate_y2 = float(input ('enter y2'))

distance = (((coordinate_x2 - coordinate_x1)**2) + ((coordinate_y2 - coordinate_y1)**2)) ** 0.5


print("*******\n *****\n  ***\n   *")



