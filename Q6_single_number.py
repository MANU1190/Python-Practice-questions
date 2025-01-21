"""
Better solution is to use XOR funtion 

def singleNumber(nums):
    if len(nums) == 1:
        return nums[0]
    seen = set()
    for i in range (len(nums)):
        if (nums[i] in seen or nums[i] in nums[i+1:]):
            seen.add(nums[i])
        else:
            return nums[i]

nums2 = [2,2,1]
print(singleNumber(nums2))

""" 
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
        
    return result

nums = [4,1,2,1,2]
print(singleNumber(nums))