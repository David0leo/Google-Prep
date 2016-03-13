class MinBinaryHeap:
    def __init__(self):
        self.heap = [0]    #has zero for easier int division
        self.size = 0
    
    def percolate_up(self, i):
        """Maintains min heap property,
        helper function to insert to swap 
        smaller children with parents until min
        heap property restored.
        """
        while i//2 > 0:
            #i//2 gives 'parent'
            if self.heap[i] < self.heap[i//2]:
                temp = self.heap[i//2]
                #set parent to 'smaller' child
                self.heap[i//2] = self.heap[i]
                #set child to parent
                self.heap[i] = temp
            #move up to parent and repeat till at root
            i = i//2
    
    def percolate_down(self, i):
        """Maintains min heap property,
        helper fnct to delMin.
        """
        while (2*i) <= self.size:
            min_ind = self.min_child(i)
            if self.heap[i] > self.heap[min_ind]:
                temp = self.heap[i]
                self.heap[i] = self.heap[min_ind]
                self.heap[min_ind] = temp
            i = min_ind
    
    def min_child(self, i):
        """Gets index of the minimum child
        of 'node' at index i.
        Left child at 2*i
        Right child at 2*i + 1
        """
        if 2*i + 1 > self.size:
            return 2*i
        else:
            if self.heap[2*i] < self.heap[2*i+1]:
                return 2*i
            else:
                return 2*i + 1
    
    def insert(self, i):
        self.heap.append(i)
        self.size += 1
        self.percolate_up(self.size)
    
    def get_min(self):
        """Returns min, doesn't alter heap"""
        return self.heap[1]
    
    def extract_min(self):
        """Returns min, and removes it from heap"""
        ret = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.percolate_down(1)
        return ret
    
    def delete_min(self):
        """Returns nothing, and removes min from heap"""
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.percolate_down(1)
    
    def build_min_heap(self, a_list):
        """Builds a min heap from an unordered list.
        Requires initialized min heap
        """
        i = len(a_list)//2
        self.size = len(a_list)
        self.heap = [0] + alist[:]
        while i > 0:
            self.percolate_down(i)
            i -= 1

    
    