class Node(object):

    def __init__(self, other=None):
        self.other = other
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.other)


class List(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode

    def __str__(self):
        someString = ""
        current = self.head
        while current != None:
            someString = someString + " " + str(current.other)
            current = current.next
        return someString


class Queue(List):
    def enqueue(self, value):
        self.append(value)

    def dequeue(self):
        self.temp = self.head
        self.head = self.head.next
        return self.temp

class Child():
    def __init__(self, name):
        self.name = name


class Student(Child):
    def __init__(self, name):
        Child.__init__(self,name)
    def rolls(self, roll):
        self.roll = roll
        return roll

a = Child("xyz")
print(a.name)
b = Student()
print(b.name("abc"))
print(b.rolls(12))
class Student(Child):
    def __init__(self, name):
        Child.__init__(self,name)
    def roll(self, roll):
        self.roll = roll