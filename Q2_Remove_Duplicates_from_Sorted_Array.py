#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
"""
def remove_duplicate_sorted(array):
    count = 1
    seen = []
    for i in range(len(array)):
        if array[i] not in seen:
            seen.append(array[i])
    
    return seen

array = [0,0,1,1,1,2,2,3,3,4]
print(remove_duplicate_sorted(array))
    
    """

# expected output Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# according to the problem statement, we need to alter the same array, and the output should be array and not the count 
# the above approach works well for simple problem 

# actual approach -> we need to alter the List as well, so that in the code from the editor in leetcode will take the input
# as array and will give the elements of the array

def removeDuplicates(self, nums) -> int:
    if not nums :
        return 0        
    index = 0
    for i in range (1,len(nums)):
        if(nums[i] != nums[index]):
            index += 1
            nums[index] = nums[i]

    return index + 1