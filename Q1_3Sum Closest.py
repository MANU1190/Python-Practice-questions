""" 
def threeSumClosest(nums, target) -> int:
    nums.sort()
    closest_sum = float('inf')
    
    for i in range(len(nums)-2):
        current_sum = nums[i] + nums[i+1] + nums[i+2]
        
        if abs(current_sum - target) < abs(closest_sum - target):
            closest_sum = current_sum
        
    return closest_sum

nums = [-1,2,1,-4]
target = 1
print(threeSumClosest(nums, target))

This solution is only partially correct
because there are chances that the shortest value can be found by take values i, i+1, i+4 
so better we go with 2 point approach 
"""

def threeSumClosest(nums, target) -> int:
    nums.sort()
    closest_sum = float('inf')
    
    for i in range(len(nums)-2):
        left = i+1
        right = len(nums)-1 
        
        while (left < right): 
            current_sum = nums[i] + nums[i+1] + nums[i+2]
        
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
                
            if current_sum < target:
                left +=1
            elif current_sum > target: 
                right -=1
            else :
                return current_sum 
        
    return closest_sum

nums = [-1,2,1,-4]
target = 1
print(threeSumClosest(nums, target))