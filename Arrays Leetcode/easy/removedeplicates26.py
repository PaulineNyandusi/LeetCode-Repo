# input = integer array nums sorted in non-decreasing order
# output = the number of unique elements, k
# remove the duplicates in-place such that each unique element appears only once. T

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]


def removeDuplicates(nums):
    # two pointers

    k = 1
    # i = 0
    for ele in range(1,len(nums)):
        if nums[ele] != nums[ele - 1]:
            nums[k] = nums[ele]
            k = k + 1
        # i = i + 1
    return k    
