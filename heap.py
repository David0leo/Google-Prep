def build_max_heap(unord_list):
    for i in range(len(unord_list)//2 + 1, -1, -1):
        max_heapify(unord_list, i, len(unord_list))
    return unord_list

def max_heapify(array, i, end):
    """Fixes a single violation of the
    heap property in an array visualized
    as a near complete binary tree.
    Args:
         array : array to be fixed
         i : index of 'node' which is
             root of 'subtree' to be fixed
        end: number of elements in array to be considered
    Returns nothing, just modifies array.
    """
    assert i < end, "Root out of index range"
    #check if root is leaf and return if it is
    #root is a leaf if its index > length//2 - 1
    #if i > (len(array)//2 - 1):
    if i > (end//2 - 1):
        return
    left = array[2*i+1]
    if 2*i + 2 == end:
        #swap left child and root
        if left > array[i]:
            to_swap = 2*i+1
        else:
            return
    else:
        #there is a right child, compare to left
        right = array[2*i + 2]
        if right > left:
            if right > array[i]:
                to_swap = 2*i + 2
            else:
                return
        else:
            if left > array[i]:
                to_swap = 2*i + 1
            else:
                return
    #print("before", array)
    temp = array[to_swap]
    array[to_swap] = array[i]
    array[i] = temp
    #print("swapped", array)
    #now need to check for possible new problems
    max_heapify(array, to_swap, end)

def get_max(max_heap):
    return max_heap[0]

def extract_max(heap):
    root = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    max_heapify(heap, 0, len(heap))
    return root

def delete_max(heap):
    heap[0] = heap[-1]
    heap.pop()
    max_heapify(heap, 0, len(heap))
    return

def insert(heap, new_key):
    heap.append(new_key)
    #make sure heap property is ok
    new_index = len(heap) - 1
    parent_index = (new_index-1)//2
    while parent_index >= 0:
        max_heapify(heap, parent_index, len(heap))
        #print("heapidied", heap)
        parent_index = (parent_index-1)//2
    return
    

def heap_sort(array):
    build_max_heap(array)
    num_elem = len(array)
    while num_elem > 1:
        #swap root with elem at (end = num_elem - 1)
        temp = get_max(array)
        array[0] = array[num_elem - 1]
        array[num_elem - 1] = temp
        #consider last elem sorted, and heapsort rest
        num_elem -= 1
        max_heapify(array, 0, num_elem)
    return array

def test():
    test_list = [1, 3, 5]
    print(build_max_heap(test_list))
    print(test_list)
    
    pi_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9]
    #print(heap_sort(pi_list))
    print(build_max_heap(pi_list))
    insert(pi_list, 7)
    print(pi_list)
    insert(pi_list, 10)
    print(pi_list)
    
    print("extracting max...", extract_max(pi_list), "...", pi_list)
    delete_max(pi_list)
    print("deleting max...", pi_list)
    
    return

test()
    