number = int (input ('first: '))
numbert = int (input ('second: '))
numberf = int (input ('third: '))
if number == numbert and number == numberf:
    print('3')
elif number == numbert or number == numberf:
    print ('2')
elif number != numbert and number != numberf:
    print ('0')