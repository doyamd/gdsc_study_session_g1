found = False
patt = ''
while not found:
    print('Please Enter the patter to be printed: ',end='')
    patt = input()
    if patt.isdigit() or patt in ['a','e','i','o','u']:
        print('Vowels and digits not allowed\n')
    elif len(patt) > 1:
        print('Length should not exceed 1')
    else:
        found = True
for i in range(5):
    print(patt*((i*2)+1))
