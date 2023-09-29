import secrets


def reverseVowels(s):
    vowels = 'aeiouAEIOU'

    #Define Pointers:
    start = 0
    stop = len(s) - 1

    s= list(s)

    while start < stop:
        if s[start] in vowels and s[stop] in vowels:
            s[start], s[stop] = s[stop], s[start]

            start += start
            stop -= stop

        elif s[start] in vowels:
            stop -= 1
        else:
            start +=1
            
    s = ''.join(s)
    print(s)
    
    


print(reverseVowels("hello"))