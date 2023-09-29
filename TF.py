def containsDuplicate(nums):
    hashSet = set()
    for num in nums:
        if num in hashSet:
            return("True")
        else:
            hashSet.add(num)
            
    return("False")
        

nums = [1,2,3,1]
containsDuplicate(nums)