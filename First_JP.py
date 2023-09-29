'''
With Recursion 

'''

'''
def isHappy(n,d):
    print(d)
    n = str(n)
    sum = 0
    for c in n:
        sum += int(c) * int (c)
    
    if sum == 1:
        return True
    elif sum in d:
        return False
    else:
        d[sum]=True
        return isHappy(sum, d)

'''


# a = isHappy(19,{})
# print(a)

# a = isHappy(16,{})
# print(a)


def isHappy_iter(n):
    dict = {}
    n = str(n)

    while(1):
        print(n)
        sum = 0
        for c in n:
            sum += int(c) * int(c)
        if(sum == 1):
            return True
        elif sum in dict:
            return False
        else:
            n = str(sum)
            dict[sum] = True

a = isHappy_iter(19)
print(a)

