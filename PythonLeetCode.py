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

def
