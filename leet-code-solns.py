"""Leetcode Questions"""

#169. Majority Element - 52ms
def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 1
    index = 0
    for i in range(0, len(nums)):
      if nums[index] == nums[i]:
        count += 1
      else:
        count -= 1
      if count == 0:
        count = 1
        index = i
    return nums[index]
  
#169v2. Majority Element - 48ms
def majorityElement(self, nums):
      """
      :type nums: List[int]
      :rtype: int
      """
      count = 1
      index = 0
      for i in range(0, len(nums)):
        if nums[index] == nums[i]:
          count += 1
        else:
          count -= 1
        if count == 0:
          count = 1
          index = i
      return nums[index]

#217. Contains Duplicate - 60ms
def containsDuplicate(self, nums):
      """
      :type nums: List[int]
      :rtype: bool
      """
      if len(nums) == 0:
        return False
    
      num_map = {}
      for number in nums:
        num_string = str(number)
        if num_map.get(num_string):
          return True
        else:
          num_map[num_string] = 1
      return False

#238. Product of Array Except Self - 196ms
def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    length = len(nums)
    
    if length <= 1:
      return nums
        
    new_nums = [1]*length
    holder = [1]*length
    
    for i in range(1, length):
      new_nums[i] *= new_nums[i-1]
      new_nums[i] *= nums[i-1]
        
      holder[length-1-i] *= holder[length-i]
      holder[length-1-i]
        
      holder *= nums[length - i]
        
    for j in range(length-1, 0, -1):
      holder *= nums[j]
      new_nums[j-1] *= holder
        
    return new_nums
  
#242. Valid Anagram - 88ms
def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    
    Check if they are permutations of each other.
    ie same # of elem and same length
    """
    
    if len(s) != len(t):
      return False
    
    count_map1 = {}
    count_map2 = {}
    for char in s:
      if count_map1.get(char):
        count_map1[char] += 1
      else:
        count_map1[char] = 1
    for char in t:
      if count_map2.get(char):
        count_map2[char] += 1
      else:
        count_map2[char] = 1
    return count_map1 == count_map2
