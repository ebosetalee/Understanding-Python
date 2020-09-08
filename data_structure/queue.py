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
        print(self.head.value)
        return self.head

    def get_tail(self):
        print(self.tail.value)
        return self.tail

    def add(self, value):
        """
        Adds the value to the end of the list

        :param value: the value to be added
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
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
                return True
            current_node = current_node.next
        return False


class Queue(LinkedList):
    """
    The queue uses a LinkedList internally to manage the items
    """
    
    def __init__(self):
        """
        Initialize the Queue with an empty LinkedList
        """
        super().__init__()
        self.items = LinkedList()

    def is_empty(self):
        """
        :returns: True if the LinkedList is empty and False if it isn't
        """
        if self.items.head is None:
            print("empty")
            return True
        print("not empty")
        return False

    def enqueue(self, value):
        """
        Adds the value to the back of the LinkedList
        :param value: the value to be added
        """
        self.items.add(value)
        # self.items.walk()

    def dequeue(self):
        """
        Removes the value at the head
        :return: the value of the item at the head
        """
        current_node = self.items.head
        if not self.items.head:
            return self.items.head.value
        self.items.head = self.items.head.next
        # self.items.walk()
        return current_node.value

    def peek(self):
        """
        :returns: the value of the item at the head
        """
        return self.items.get_head()
        # OR
        # return self.items.head.value

queue = Queue()
queue.is_empty()

queue.items.walk()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(13)
queue.enqueue(31)
queue.items.walk()

# assert that the item dequeued was the item at the head
queue.dequeue() # 1
# assert that the item at the head of the linked list was removed
queue.items.walk() # [2, 13, 31]

queue.is_empty()

queue.peek()
