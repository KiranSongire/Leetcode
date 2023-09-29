# from collections import Counter
# def majorityElement(nums):
#     temp = {}
#     for i in range(len(nums)):
#        Counter(nums)
#     print(max(Counter(nums)))

 

# majorityElement([3,2,3])

def majorityElement(nums):
    temp = {}
    for value in nums:
        # value = input(f'The iteration is:{iteration}')
        if value in temp:
            temp[value] += 1
        else:
            temp[value] = 1
            
    # for key, value in temp.items():
    #     print("% d : % d" % (key, value))
        maxvalue = max(temp, key = temp.get)

    print(maxvalue)
    
# Driver function
if __name__ == "__main__":
    my_list = [3,3,4]
 
    majorityElement(my_list)