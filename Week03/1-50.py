total = 0
three_five = 0
count = 0
for i in range(1,51):
    if i%3 == 0:
        three_five += i
        count += 1
        print('Three')
    elif i%5 == 0:
        three_five += i
        count += 1
        print('Five')
    elif i%2 == 0:
        total += i
print('Total even: ', str(total))
print('Three and five divisible count: '+str(count))
print('Three and five divisible sum: '+str(three_five))
