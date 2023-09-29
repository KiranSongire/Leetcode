'''
1. check the binary conversion of integer
2. calculate number of 1's in their binary format
    if binformats have equal ones:
        sort into thier actual integer ascending order
    else:
        sort into ascending of count of 1's
3. return the array of sorting.
'''

def sortByBits(arr):

    binary = 0
    sum = []
    result = []

    for i in range(0,len(arr)):
        binary = bin(arr[i]).count("1")
        sum.append([binary, arr[i]])

    sum.sort(key= lambda m:m[0])
    print(sum)

    m = sum[0][0]
    empty_array = []
    for x,y in sum: 
        if m!=x:
            m = x
            empty_array.sort()
            result = result + empty_array
            print(result)
            empty_array = []
        empty_array.append(y)
    empty_array.sort()
    result = result + empty_array

    return result





    # for temp in range(len(sum)):
    #     result.append(sum[temp][1])
    # return result



print(sortByBits([0,1,2,3,4,5,6,7,8]))

# c = [1024,512,256,128,64,32,16,8,4,2,1,15,15,15]


# print(bin(15))
# print(sortByBits(c))

