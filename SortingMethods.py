"""Sorting Methods
   Including:
        Bubble Sort, Selection Sort,
        Insertion Sort, Merge Sort,
        and Quick Sort

"""

def bubble_sort(a_list):
    """Typical bubble sort algorithm
    O(n^2) time, O(1) space
    Also stops if passed w/o any swaps, ie sorted
    'Bubble' up the largest item in list
    """

    clean_pass = False
    num_items = len(a_list)    #num of items of list to sort
    while not clean_pass and num_items > 0:
        for i in range(num_items-1):
            #print("....", a_list)
            if a_list[i] > a_list[i+1]:
                temp = a_list[i]
                a_list[i] = a_list[i+1]
                a_list[i+1] = temp
                clean_pass = False
            else:
                clean_pass = True
        num_items -= 1
    return

def test_bubble_sort():
    alist = [54,26,93,17,77,31,44,55,20]
    bubble_sort(alist)
    print(alist)
    blist = []
    bubble_sort(blist)
    print(blist)
    return

def selection_sort(a_list):
    """Typical selection sort algorithm.
    O(n^2) time, O(1) space.
    Finds largest elem, puts it at end of
    the unsorted section.
    """
    num_items = len(a_list)
    while num_items > 0:
        max_index = 0
        for i in range(1, num_items):
            if a_list [i] > a_list[max_index]:
                max_index = i
        temp = a_list[max_index]
        a_list[max_index] = a_list[num_items - 1]
        a_list[num_items - 1] = temp
        num_items -= 1
    return

def test_selection_sort():
    alist = [54,26,93,17,77,31,44,55,20]
    selection_sort(alist)
    print(alist)
    blist = []
    selection_sort(blist)
    print(blist)
    return



