# rotating an array
# Brute Force approach
"""
def rotate(array, k):
    new_array = []
    
    for i in range(1,k+1):
        new_array.append(array[-i])
        array.pop(-i)
    print(new_array + array)
"""
def rotate(array, k):
    array[:] = array[-k:] + array[:-k]
    
    return array
nums = [1,2,3,4,5,6,7]
k = 3

rotate(nums,k)