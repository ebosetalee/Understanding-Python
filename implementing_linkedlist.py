
class node:
    """ Class to contain the data and the next node"""
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next 

class Linkedlist:
    def __init__(self):
        self.head = node()

    def add(self, data):
        """ append function to add a new data point to the end 
        of the list"""
        new_node = node(data)
        current_node = self.head
        while current_node.next:
        # is the same as while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node
    
    def length(self):
        """ This function gets the length of the linkedlist
        used in managing the nodes in the list or to figure how 
        large the data structure is. """
        current_node = self.head
        total = 0
        while current_node.next:
        # is the same as while current_node.next != None:
            total += 1
            current_node = current_node.next
        return total
    
    def display(self):
        """ This display the contents of the list"""
        elements = []
        current_node = self.head
        while current_node.next !=None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)
    
    def get(self, index):
        """ This function extracts a data point from a certain 
        index from the linkedlist"""
        if index >= self.length():
            print("ERROR: 'Get' Index out of range!")
            return None

        current_index = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_index == index:
                return current_node.data
            else:
                current_index += 1
    
    def delete(self, index):
        """ This function erases a node at a certain index 
        provided"""
        if index>= self.length():
            # this checks the index provided is not longer than the linkedlist
            print("ERROR: 'delete' Index out of range")
            return
        current_index = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                # check to see if we are at the index the user provided
                # to delete, we change the pointer from the last node 
                # to be the one skipped past the current node.
                last_node.next = current_node.next
                return
            current_index += 1


my_list = Linkedlist()
my_list.display()

my_list.add(0)
my_list.add(1)
my_list.add(2)
my_list.add(3)
my_list.add(4)

my_list.display()
print("Element at 2nd index {}".format(my_list.get(2)))
        
my_list.delete(1)
my_list.display()