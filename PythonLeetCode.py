############## 1. Two Sum ##############
# -- Given an array of integers A and
#    integer k, return indices of the 
#    two integers s.t. their sum is k
# -- Assume there exists a unique sol'n.

def twoSum(A, k):
    # finds two elements a, b s.t. a+b=k
    # O(|A|) time and space. 
    # Can reduce space at cost of time.
    # O(|A|lg(|A|)) sol'n using binary
    # search on sorted A can do O(1) space.
    D = {}
    for i, n in enumerate(A):
        if k - n in D:
            return([ D[k-n] , i] )
        D[n] = i

########### 2. Add Two Numbers ###########
# -- Given two linked list representations
#    of integers a, b >= 0 stored in 
#    reverse order, return a+b as a linked
#    list in the same form as a and b.
# -- Ex. 1024 represented as follows:
#    |4| -> |2| -> |0| -> |1|

def addTwoNumbers(l1, l2):
    # Space saving, but slower
    # Modifies list l1 and sort of
    # merges the lists in some cases
    carry = 0
        front = l1
        back = l1.next
        while l1 and l2:
            l1.val += l2.val + carry
            if l1.val > 9:
                carry = 1
                l1.val -= 10
            else:
                carry = 0
            back = l1
            l1 = l1.next
            l2 = l2.next
        #now l2 could be longer than l1
        if l2:
            back.next = l2
            while carry and l2:
                l2.val += carry
                if l2.val > 9:
                    carry = 1
                    l2.val -= 10
                else:
                    carry = 0
                back = l2
                l2 = l2.next
        else:
            while carry and l1:
                l1.val += carry
                if l1.val > 9:
                    carry = 1
                    l1.val -= 10
                else:
                    carry = 0
                back = l1
                l1 = l1.next
        if carry:
            back.next = ListNode(1)
        return(front)
    
def addTwoNumbers2(l1, l2):
    #faster, creates new list
    head = ListNode(None)
    cur = None
    carry = 0
    while l1 or l2 or carry:
        sum = carry
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next
        carry = sum/10
        if cur == None:
            head.val = sum%10
            cur = head
        else:
            cur.next = ListNode(sum%10)
            cur = cur.next
    return(head)

######### 3. Longest Substring Without #########
#########    Repeating Characters      #########
# -- Given string s, find the length of the
#    longest substring w/o repeating characters

def lengthOfLongestSubstring(s):
    cur_front = 0
        max_so_far = 0
        D = {}
        for i, char in enumerate(s):
            if char in D:
                cur_front = max(cur_front, D[char] + 1)
            D[char] = i
            max_so_far = max(max_so_far, i - cur_front + 1)
        return max_so_far
    
######## 5. Longest Palindromic Substring ########
# -- Given string s, find the longest palindromic
#    substring in s.
# -- Assume max len of s is 1000, and soln is unique

def longestPalindrome(s):
    T = '^#' + '#'.join(s) + '#&'
    P = [0] + [1]*(len(T) - 2) + [0]
    center = 1
    for i in range(1, len(T) - 1):
        if P[center] + center > i:
            P[i] = min(P[2*center - i], P[center] + center - i)
        while i - P[i] >= 0 and i + P[i] < len(T) and T[i - P[i]] == T[i + P[i]]:
            P[i] += 1
        if P[i] > P[center]:
            center = i
    return T[center - P[center] + 2: center + P[center] : 2]

############## 6. ZigZag Conversion ##############
# - Word written in zig-zag pattern on numRows rows
# EX: "PAYPALISHIRING" with numRows = 3 becomes:
#     P   A   H   N
#     A P L S I I G
#     Y   I   R
def convertZigZag(s, numRows):
    if numRows <= 1:
            return s
        ret = []
        inc = 2*numRows - 2
        n = len(s)
        for i in range(numRows):
            for j in range(i, n, inc):
                ret.append(s[j])
                k = j + inc - 2*i
                if i != 0 and i != numRows - 1 and k < n:
                    ret.append(s[k])
        return ''.join(ret)
