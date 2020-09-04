class Node:
    def __init__(self, value):
        """
        Initialize the Node here
        """
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        """
        Initialize the LinkedList here
        """
        self.head = None
        self.tail = self.head

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def add(self, value):
        """
        Adds the value to the end of the list

        :param value: the value to be added
        """
        new_node = Node(value)
        # if self.head is None: OR
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            # previous_node = self.head
            # while previous_node.next:
            # # is the same as while previous_node.next is not None:
            #     previous_node = previous_node.next
            # previous_node.next = new_node
            # self.tail = previous_node.next
            # # OR
            current_node = self.tail
            current_node.next = new_node
            self.tail = current_node.next

    def prepend(self, value):
        """
        Adds the value to the start of the list

        :param value: the value to be added
        """
        new_node = Node(value)
        current_node = self.head
        new_node.next = current_node
        self.head = new_node
        
    def display(self):
        """ This display the contents of the list"""
        elements = []
        cur_node = self.head
        while cur_node is not None:
            elements.append(cur_node.value)
            cur_node = cur_node.next
        print(elements)

    def remove(self, value):
        """
        Finds the vales and removes it

        :param value: the value to be removed
        :return: True if the value was removed, or False if the value isn't in the list
        """
        current_node = self.head
        previous_node = None
        while current_node:
            if current_node.value == value:
                if previous_node:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                return True
            else:
                previous_node = current_node
                current_node = current_node.next
        return False

    def walk(self):
        """
        Prints out all the items in the list starting from the head

        :rtype: collections.Iterable[Node]
        :returns: An array of the items in the list
        """
        elements = []
        current_node = self.head
        while current_node:
        # is the same as while current_node.next != None: or is not None
            elements.append(current_node.value)
            current_node = current_node.next
        print(elements)
        return elements

    def search(self, value):
        """
        Searches the list to see if an item is inside

        :param value: The item searched for
        :returns: True if the value was found, or False if the value was not found 
        """
        current_node = self.head
        while current_node:
            if current_node.value == value:
                print("found {}".format(value))
                return value
            else: # else isn't necessary
                current_node = current_node.next
        return None

# This is a subclass of LinkedList
class DoublyLinkedList(LinkedList):
    def add(self, value):
        """
        Adds the value to the end of the list

        :param value: the value to be added
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = self.head
            self.head.previous = None
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, value):
        """
        Adds the value to the start of the list

        :param value: the value to be added
        """
        new_node = Node(value)
        self.head.previous = new_node
        new_node.next = self.head
        self.head = new_node

    def remove(self, value):
        """
        Finds the vales and removes it

        :param value: the value to be removed
        :return: True if the value was removed, or False if the value isn't in the list
        """
        current_node = self.head
        previous_node = None
        while current_node:
            if current_node.value == value:
                if previous_node is None:
                    self.head = current_node.next
                    self.head.previous = None
                    print("done1")
                else:
                    if current_node == self.tail:
                        previous_node.next = None
                        self.tail = previous_node
                        print("done2")
                    else:
                        previous_node.next = current_node.next
                        current_node = current_node.next
                        current_node.previous = previous_node
                        print("done3")
                return True
            else:
                previous_node = current_node
                current_node = current_node.next
        return False

    def walk_reverse(self):
        """
        Prints out all the items in the list starting from the tail to the head

        :rtype: collections.Iterable[Node]
        :returns: A reversed array of the items in the list
        """
        elements = []
        current_node = self.head
        while current_node:
            # is the same as while current_node.next != None: or is not None
            elements.append(current_node.value)
            current_node = current_node.next
        print(elements[::-1])
        return elements[::-1]

my_list = DoublyLinkedList()
my_list.walk()

my_list.add(0)
my_list.add(1)
my_list.add(2)
my_list.add(3)
my_list.add(4)

my_list.walk()
my_list.walk_reverse()

my_list.prepend(5)
my_list.prepend(6)
my_list.prepend(7)
my_list.walk()
my_list.walk_reverse()

my_list.remove(4)
my_list.walk()
