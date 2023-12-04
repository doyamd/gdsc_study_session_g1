for i in range(1,100):
    if i < 10:
        print(', 0'+str(i) if i!= 1 else '0'+str(i), end='')
    else:
        print(', '+str(i), end='')
