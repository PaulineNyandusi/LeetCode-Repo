# 27, Remove Element

# input = array, integer, value
# remove all occurrences of val in nums in-place
# output = no. of elements not equal to val, consider it to be k

# conditions
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. number of elements in nums which are not equal to val be k
# Return k.

# Example 1:
# Input: nums = [3,2,2,3], val = 3
# Output: k =2, nums = [2,2,_,_]

# Example 2:
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]


def removeElement(nums, val):
  i = 0  # iteration
  k = 0  # number of valid elements

  while i < len(nums):
    if val != nums[i]:
      nums[k] = nums[i]
      k = k + 1
    i = i + 1
  print(nums)
  return k


print([0, 1, 2, 2, 3, 0, 4, 2], 2)
