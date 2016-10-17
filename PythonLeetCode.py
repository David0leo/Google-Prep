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
    S = set(A)
    for n in S:
        if k - n in S:
            return [n, k-n]
    # not necessary, but feels bad leaving
    # no return value on no sol'n found.
    return []    
