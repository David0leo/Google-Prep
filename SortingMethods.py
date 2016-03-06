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


def insertion_sort(a_list):
    """Insertion sort algorithm
    O(n^2) time, O(1)-O(n) space
    """

    for i in range(1, len(a_list)):
        sorting = a_list[i]
        sorting_ind = i
        while sorting_ind > 0 and a_list[sorting_ind - 1] > sorting:
            a_list[sorting_ind] = a_list[sorting_ind - 1]
            sorting_ind -= 1
        a_list[sorting_ind] = sorting
    return

def merge_sort(a_list):
    """Merge sort algorithm
    O(nlgn) time, O() space
    """
    if len(a_list) > 1:
        mid_ind = len(a_list)//2
        #split list into two parts
        left = a_list[:mid_ind]
        right = a_list[mid_ind:]
        #recursively sort two halves
        merge_sort(left)
        merge_sort(right)
        #begin merge sequence
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            #fill a_list from smallest to largest (left to right)
            if left[i] < right[j]:
                a_list[k] = left[i]
                i += 1
            else:
                a_list[k] = right[j]
                j += 1
            k += 1
        #take care of merging elem from longer half
        while i < len(left):
            a_list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            a_list[k] = right[j]
            j += 1
            k += 1
            
        return
    
#################################################################
#quicksort from 
#http://interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html
def quick_sort(a_list):
    _quick_sort(a_list, 0, len(a_list) - 1)

def _quick_sort(a_list, first_ind, last_ind):
    if first_ind < last_ind:
        #get partition
        split_ind = partition(a_list, first_ind, last_ind)
        #recursively call helper funcion _quick_sort() on
        #the two halves
        _quick_sort(a_list, first_ind, split_ind - 1)
        _quick_sort(a_list, split_ind + 1, last_ind)

def partition(a_list, first_ind, last_ind):
    #get pivot value as median of three
    first = a_list[first_ind]
    last = a_list[last_ind]
    middle = a_list[last_ind//2]
    if first <= last:
        if last <= middle:
            pivot_ind = last_ind
        elif middle <= last and middle >=first:
            pivot_ind = last_ind//2
        else:
            pivot_ind = first_ind
    else:
        if first <= middle:
            pivot_ind = first_ind
        elif middle <= first and middle >= last:
            pivot_ind = last_ind//2
        else:
            pivot_ind = last_ind
    #end get pivot value
    #swap pivot and first
    temp = a_list[first_ind]
    a_list[first_ind] = a_list[pivot_ind]
    a_list[pivot_ind] = temp
    #end swap
    pivot = a_list[first_ind]
    
    left_ind = first_ind + 1
    right_ind = last_ind
    
    done = False
    while not done:
        while left_ind <= right_ind and a_list[left_ind] <= pivot:
            left_ind += 1
        while left_ind <= right_ind and a_list[right_ind] >= pivot:
            right_ind -= 1

        if right_ind < left_ind:
            done = True
        else:
            #swap left and right out of pos. w.r.t. pivot
            temp = a_list[left_ind]
            a_list[left_ind] = a_list[right_ind]
            a_list[right_ind] = temp
    #left and right crossed, swap first with right wall
    temp = a_list[first_ind]
    a_list[first_ind] = a_list[right_ind]
    a_list[right_ind] = temp
    
    return right_ind
    