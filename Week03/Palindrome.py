def solve():
    print('Please Enter the word to be checked: ',end='')
    word = input()
    size = len(word)//2
    j = len(word)-1
    for i in range(size):
        if word[i] == word[j]:
            j-=1
        else:
            print('The word '+word+' is not a palindrome.')
            return
    print('The word '+word+' is palindrome.')
    return
solve()
            