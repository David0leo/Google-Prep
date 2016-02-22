class SinglyLinkedListNode:
    
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, new_data):
        self.data = new_data
    
    def set_next(self, new_next):
        #new_next should be a node
        self.next = new_next
    
    def __str__(self):
        return str(self.data)
    

class SinglyLinkedList:
    
    def __init__(self, head = None):
        self.length = 0
        self.head = head
    
    def get_length(self):
        return self.length
    
    def get_head(self):
        return self.head
    
    def set_head(self, new_head):
        self.head = new_head
    
    def fetch_node(self, index):
        """Helper method used to access node
           at a given index.
           O(n) time, O(1) space.
        """
        current = self.head
        count = 0
        while count < index and current.get_next() != None:
            current = current.get_next()
            count += 1
        return current
    
    def find_first(self, some_data, get_prev=False):
        """Helper method used to find first
           node containing some_data as its data
           Returns a SinglyLinkedListNode
        """
        current = self.head
        if get_prev:
            prev = None
        found = False
        while not found and current != None:
            if current.get_data() == some_data:
                found = True
                break
            else:
                if get_prev:
                    prev = current
                current = current.get_next()
        if not found:
            print("No item:", some_data, "found")
            raise ValueError("No item:", some_data, "found in list")
        else:
            if get_prev:
                return prev
            else:
                return current
    
    def append(self, new_data):
        """Creates a new node using new_data
           and adds the new node to the end of
           the list incrementing length. 
           Fetching end node takes O(n) time.
           Overall O(n) time O(1) space.
        """
        new_node = SinglyLinkedListNode(new_data)
        if self.head == None:
            self.head = new_node
            self.length += 1
        else:
            end = self.fetch_node(self.length - 1)
            end.set_next(new_node)
            self.length += 1
    
    def extend(self, linked_list):
        """Extends list by the elements
           of the passed list in order.
           
           Implementation allows for extension
           by self.
           ie) my_ll.extend(my_ll) works.
           Fixed from just appending to make it
           O(n) time, O(n) space as we duplicate 
           linked_list passed.
        """
        current = linked_list.get_head()
        if self.length == 0:
            self.head = current
            self.length = linked_list.get_length()
        else:
            end = self.fetch_node(self.length - 1)
            count = 0
            length = linked_list.get_length()
            while current != None and count < length:
                count += 1
                temp = SinglyLinkedListNode(current.get_data())
                end.set_next(temp)
                end = temp
                current = current.get_next()
                self.length += 1
    
    def insert(self, i, new_data):
        """Inserts new data member at a given index.
           Creates a new node, and finds insertion pt
           in O(n) time. O(1) space.
        """
        if i >= self.length:
            self.append(new_data)
        elif i == 0:
            new_node = SinglyLinkedListNode(new_data, self.head)
            self.head = new_node
            self.length += 1
        else:
            new_node = SinglyLinkedListNode(new_data)
            count = 0
            current = self.head
            prev = None
            while (count < i ) and (current != None):
                prev = current
                current = current.get_next()
                count += 1
            if current == None:
                print("Error with insert, current node None")
                return
            #passed through and current should be at given index
            prev.set_next(new_node)
            new_node.set_next(current)
            self.length += 1
    
    def remove(self, some_data):
        #get node whose next is to be removed
        before_remove = self.find_first(some_data, True)
        if before_remove == None:
            #we are at head of list
            self.head = self.head.get_next()
        else:
            to_remove = before_remove.get_next()
            before_remove.set_next(to_remove.get_next())
        self.length -= 1
        
    
    def pop(self, index = None):
        """Removes node and returns data
           of last item from the list or 
           at index if given.
           Fetch takes O(n) time, then just O(1)
           to assign stuff.
           Space is O(1).
        """
        if index == None:
            index = self.length - 1

        if index == 0:
            #just set new head if popping from front
            to_pop = self.head
            self.head = self.head.get_next()
        else:
            before_pop = self.fetch_node(index - 1)
            to_pop = before_pop.get_next()
            before_pop.set_next(to_pop.get_next())
            
        self.length -= 1
        return to_pop.get_data()
        
    
    #def index(some_data):
    
    #def count(some_data):
    
    #def sort(cmp = None, key = None, reverse = False):
    
    def reverse(self):
        """Reverses list in place
           O(n) time, O(1) space
        """
        new = None
        current = self.head
        while current != None:
            temp = current
            current = current.get_next()
            temp.set_next(new)
            new = temp
        self.head = new
    
    def __str__(self):
        list_string = "["
        current = self.head
        while current != None:
            list_string += str(current)
            current = current.get_next()
            if current != None:
                list_string += ", "
        list_string +="]"
        return list_string