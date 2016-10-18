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
    
def addTwoNumbers(l1, l2):
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
