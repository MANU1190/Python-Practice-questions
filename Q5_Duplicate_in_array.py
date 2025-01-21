"""
def duplicate(nums):
    seen = []
    for i in range(len(nums)):
        if nums[i] not in seen:
            seen.append(nums[i])
        else:
            return False
    
    return True
nums = [1,1,1,3,3,4,3,2,4,2]
print(duplicate(nums))

"""
#Need to reduce the time complexity
def duplicate(nums):
    seen = set()  # we can make use of list as well, but the time complexity is higher for that, where in set it takes the 
                    # average time complexity
    for num in nums:
        if num in seen:
            return True
        seen.add
    return False
    
    return True
nums = [1,1,1,3,3,4,3,2,4,2]
print(duplicate(nums))