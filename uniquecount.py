from collections import Counter
def findLeastNumOfUniqueInts(arr, remove):
    print (arr)
    dict = {}
    for k in arr:
        if k in dict:
            dict[k]+=1 
        else:
            dict[k] = 1
    
    print(dict)
    two_d_array = []
    for k in dict:
        print(k)
        two_d_array.append([k,dict[k]])
    
    print(two_d_array)
    two_d_array.sort(key=lambda i:i[1])

    print(two_d_array)

    for element in two_d_array:
        while(element[1] > 0 and remove > 0):
            element[1] -= 1
            remove -=1
    
    result = []

    for ele in two_d_array:
        print(ele)
        if ele[1] > 0:
            result.append(ele)
    return len(result)


        # print(element)
        # if element[1]>0:
        #     element[1] -= 1

    #for i in range(remove):








print(findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3))
