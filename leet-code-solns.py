"""Leetcode Questions"""

#100. Same Tree - 40ms
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def isSameTree(self, p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    Iterative Solution
    """
    p_stack = [p]
    q_stack = [q]
    
    while p_stack:
        p_next = []
        q_next = []
        while p_stack:
            current_p = p_stack.pop()
            current_q = q_stack.pop()
            if current_p == None or current_q == None:
                if current_p != current_q:
                    return False
            elif current_p.val != current_q.val:
                return False
            else:
                p_next.append(current_p.left)
                p_next.append(current_p.right)
                q_next.append(current_q.left)
                q_next.append(current_q.right)
            p_stack = p_next
            q_stack = q_next
            if len(p_stack) != len(q_stack):
                return False
                
    return True


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

#237. Delete Node in a Linked List - 64ms
"""Got 2 different values when run 2times"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def deleteNode(self, node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    if node.next:
        node.val = node.next.val
        node.next = node.next.next
    else:
        node = None

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

#260. Single Number III - 48ms
def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    Working with Bits
    """
    sum = 0
    first = 0
    second = 0
    for number in nums:
        sum ^= number
    
    mask = 1
    while sum & mask == 0:
        mask = mask << 1
    
    for number in nums:
        if number & mask:
            first ^= number
        else:
            second ^= number
    return [first, second]

#283. Move Zeros - 64ms
def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    
    Visualize a moving sequence of zeros, swap with head of sequence if
    we find a non-zero while scanning list
    """
    zeros_len = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            zeros_len += 1
        else:
            nums[i - zeros_len] = nums[i]
            if zeros_len != 0:
                nums[i] = 0
