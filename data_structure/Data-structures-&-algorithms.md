### __What is Data Structure?__
[study tonight](https://www.studytonight.com/data-structures/)
[tutorials point](www.tutorialspoint.com/data_structures_algorithms)

Data structure is a programmatic way of collecting, storing and organizing data. 

__TYPES OF DATA STRUCTURE:__
Anything that can store data can be called as a data structure, hence Integer, Float, Boolean, Char etc, all are data structures. They are known as Primitive Data Structures.
Abstract Data Structure are :
- Linked List
- Tree
- Graph
- Stack, Queue etc.

__The data structures can also be classified on the basis of the following characteristics:__
Characterstic |	Description
Linear |	In Linear data structures,the data items are arranged in a linear sequence. Example: Array
Non-Linear |	In Non-Linear data structures,the data items are not in sequence. Example: Tree, Graph
Homogeneous |	In homogeneous data structures,all the elements are of same type. Example: Array
Non-Homogeneous	| In Non-Homogeneous data structure, the elements may or may not be of the same type. Example: Structures
Static |	Static data structures are those whose sizes and structures associated memory locations are fixed, at compile time. Example: Array
Dynamic | Dynamic structures are those which expands or shrinks depending upon the program need and its execution. 
|Also, their associated memory locations changes. Example: Linked List created using pointers

Following terms are the foundation terms of a data structure:
- Interface − Each data structure has an interface. Interface represents the set of operations that a data structure supports. An interface only provides the list of supported operations, type of parameters they can accept and return type of these operations.
- Implementation − Implementation provides the internal representation of a data structure. Implementation also provides the definition of the algorithms used in the operations of the data structure.

__Need for Data Structure:__
- Data Search
- Processor Speed
- Multiple Requests

__Basic Terminology__
Data − Data are values or set of values.
Data Item − Data item refers to single unit of values.
Group Items − Data items that are divided into sub items are called as Group Items.
Elementary Items − Data items that cannot be divided are called as Elementary Items.
Attribute and Entity − An entity is that which contains certain attributes or properties, which may be assigned values.
Entity Set − Entities of similar attributes form an entity set.
Field − Field is a single elementary unit of information representing an attribute of an entity.
Record − Record is a collection of field values of a given entity.
File − File is a collection of records of the entities in a given entity set.

__Data Definition:__
It defines a particular data with the following characteristics:
Atomic − a single concept.
Traceable − mapped to some data element.
Accurate − unambiguous.
Clear and Concise − understandable.

__Data Type__
This classifies various types of data such as integer, string, etc. There are two data types −
- Built-in Data Type
- Derived Data Type

Built-in Data Type:
Those data types for which a language has built-in support are known as Built-in Data types. For example, most of the languages provide the following built-in data types; Integers; Boolean (true, false); Floating (Decimal numbers); Character and Strings. 

Derived Data Type:
Those data types that are implementation independent as they can be implemented in one or the other way are known as derived data types. These data types are normally built by the combination of primary or built-in data types and associated operations on them. For example − List; Array; Stack; Queue.

Basic Operations:
The data in the data structures are processed by certain operations. The particular data structure chosen largely depends on the frequency of the operation that needs to be performed on the data structure - Traversing; Searching; Insertion; Deletion; Sorting; Merging.

##### ARRAY

Array is a container holding a fix number of similiar items. i.e items of the same data type. The important terms to understand the concept of Array are:
- Element − Each item stored in an array is called an element.
- Index − Each location of an element in an array has a numerical index, which is used to identify the element.

__Basic Operations__
The basic operations supported by an array are:
1. Traverse − print all the array elements one by one.
2. Insertion − Adds an element at the given index.
3. Deletion − Deletes an element at the given index.
4. Search − Searches an element using the given index or by the value.
5. Update − Updates an element at the given index.

##### Linked List
A linked list is a sequence of data structures, which are connected together via links.
Linked List is a sequence of links which contains items. Each link contains a connection to another link. The important terms to understand the concept of Linked List are:
- Link − Each link of a linked list can store a data called an element.
- Next − Each link of a linked list contains a link to the next link called Next.
- LinkedList − A Linked List contains the connection link to the first link called First.

__Types of Linked List__
1. Simple Linked List − Item navigation is forward only.
2. Doubly Linked List − Items can be navigated forward and backward.
3. Circular Linked List − Last item contains link of the first element as next and the first element has a link to the last element as previous.

__Basic Operations__
1. Insertion − Adds an element at the beginning of the list.
2. Deletion − Deletes an element at the beginning of the list.
3. Display − Displays the complete list.
4. Search − Searches an element using the given key.
5. Delete − Deletes an element using the given key.
6. Reverse - Moves the head list to the last node.

###### SIMPLE / LINEAR LINKED LIST
[git hub tutorial](https://github.com/vprusso/youtube_tutorials/blob/master/data_structures/linked_list/singularly_linked_list/linked_list_insertion.py)
Linear Linked list is the default linked list and a linear data structure in which data is not stored in contiguous memory locations but each data node is connected to the next data node via a pointer, hence forming a chain.

The element in such a linked list can be inserted in 2 ways:
Insertion at beginning of the list.
Insertion at the end of the list.

###### DOUBLY LINKED LIST
Doubly Linked List is a variation of Linked list whereby navigation is possible in both ways, either forward and backward easily as compared to Single Linked List. The important terms to understand the concept of doubly linked list are:
1. Link − Each link of a linked list can store a data called an element.
2. Next − Each link of a linked list contains a link to the next link called Next.
3. Prev − Each link of a linked list contains a link to the previous link called Prev.
4. LinkedList − A Linked List contains the connection link to the first link called First and to the last link called Last.

__Basic Operations__
1. Insertion − Adds an element at the beginning of the list.
2. Deletion − Deletes an element at the beginning of the list.
3. Insert Last − Adds an element at the end of the list.
4. Delete Last − Deletes an element from the end of the list.
5. Insert After − Adds an element after an item of the list.
6. Delete − Deletes an element from the list using the given key.
7. Display forward − Displays the complete list in a forward manner.
8. Display backward − Displays the complete list in a backward manner.

###### CIRCULAR LINKED LIST
Circular Linked List is a variation of Linked list in which the first element points to the last element and the last element points to the first element. Both Singly Linked List and Doubly Linked List can be made into a circular linked list.

__Basic Operations__
1. Insert − Adds an element at the start of the list.
2. Delete − Deletes an element at the start of the list.
3. Display - Displays the list.

__SIMILAARITIES__
- Both Linked List and Array are used to store linear data of similar type.

__DIFFERENCES__
ARRAY | LINKED LIST
- Array is a collection of elements of similar data type.	| Linked List is an ordered collection of elements of same type, which are connected to each other using pointers.

- Array supports Random Access, which means elements can be accessed directly using their index, like arr[0] for 1st element etc. Hence, accessing elements in an array is fast with a constant time complexity of O(1). | Linked List supports Sequential Access, which means to access any element/node in a linked list, we have to sequentially traverse the complete linked list, upto that element. To access nth element of a linked list, time complexity is O(n).

- In array, elements are stored in contiguous memory location or consecutive manner in the memory. | In a linked list, new elements can be stored anywhere in the memory.

- In array, Insertion and Deletion operation takes more time, as the memory locations are consecutive and fixed. | In linked list, a new element is stored at the first free and available memory location Thus, Insertion and Deletion operations are fast in linked list.

- Memory is allocated as soon as the array is declared, at compile time. It's also known as Static Memory Allocation.	| Memory is allocated at runtime, as and when a new node is added. It's also known as Dynamic Memory Allocation.

- In array, each element is independent and can be accessed using it's index value. |	In case of a linked list, each node/element points to the next, previous, or maybe both nodes.

- Array can single dimensional, two dimensional or multidimensional | Linked list can be Linear(Singly), Doubly or Circular linked list.

- Size of the array must be specified at time of array decalaration | Size of a Linked list is variable. It grows at runtime, as more nodes are added to it.

- Array gets memory allocated in the Stack section. |	Whereas, linked list gets memory allocated in Heap section.

__NODE__
A Node in a linked list holds the data value and the pointer which points to the location of the next node in the linked list. In other words, it is a data value and a pointer (pointing to the next node) put together.

##### __QUEUE__
Queue is an abstract data structure, somewhat similar to Stacks. Unlike stacks, a queue is open at both its ends. One end is always used to insert data (enqueue) and the other is used to remove data (dequeue). 
Queue follows First-In-First-Out methodology, i.e., the data item stored first will be accessed first.
In computer science, a queue is a particular kind of abstract data type or collection in which the entities in the collection are kept in order and the principle (or only) operations on the collection are the addition of entities to the rear terminal position, known as enqueue, and removal of entities from the front terminal position, known as dequeue. 
This makes the queue a First-In-First-Out (FIFO) data structure. In a FIFO data structure, the first element added to the queue will be the first one to be removed.

__Basic Operations__
1. enqueue() − add (store) an item to the queue.
2. dequeue() − remove (access) an item from the queue.
3. peek() − Gets the element at the front of the queue without removing it.
4. isfull() − Checks if the queue is full.
5. isempty() − Checks if the queue is empty.

__Applications of Queue__
Queue, as the name suggests is used when we need to manage any group of objects in an order in which the first one coming in, also gets out first while the others wait for their turn, like in the following scenarios:
1. Serving requests on a single shared resource, like a printer, CPU task scheduling etc.
2. In real life scenario, Call Center phone systems uses Queues to hold people calling them in an order, until a service representative is free.
3. Handling of interrupts in real-time systems. The interrupts are handled in the same order as they arrive i.e First come first served.

__Implementation of Queue__
[git hub tutorial](https://github.com/joeyajames/Python/blob/master/Queues%20implementaion.py)
Queue can be implemented using an Array, Stack or Linked List. The easiest way of implementing a queue is by using an Array.
Initially the head(FRONT) and the tail(REAR) of the queue points at the first index of the array (starting the index of array from 0). As we add elements to the queue, the tail keeps on moving ahead, always pointing to the position where the next element will be inserted, while the head remains at the first index.

__Types of Queues in Data Structure__
Queue in data structure is of the following types:
1. Simple Queue
2. Circular Queue
3. Priority Queue
4. Dequeue (Double Ended Queue)

###### __Simple Queue__
The simple queue is a normal queue where insertion takes place at the FRONT of the queue and deletion takes place at the END of the queue.

###### __Circular Queue__
In a circular queue, the last node is connected to the first node to make a circle. 
Circular queue is also called as Ring Buffer.
This can use an array or circular Linked list.
Insertion in a circular queue happens at the END and deletion at the FRONT of the queue.

###### __Priority Queue__
In a priority queue, the nodes will have some predefined priority.
Insertion in a priority queue is performed in the order of arrival of the nodes.
The node having the least priority will be the first to be removed from the priority queue.

###### __Dequeue (Doubly Ended Queue)__
In a Double Ended Queue, insertion and deletion operations can be done at both FRONT and END of the queue.

- __Implementation of Double ended Queue:__
Here we will implement a double ended queue using a circular array. It will have the following methods:
- push_back : inserts element at back
- push_front : inserts element at front
- pop_back : removes last element
- pop_front : removes first element
- get_back : returns last element
- get_front : returns first element
- empty : returns true if queue is empty
- full : returns true if queue is full

##### __Stack__
__Stack__ is an abstract data type with a bounded(predefined) capacity. 
It is a simple data structure that allows adding and removing elements in a particular order.

- __Basic features of Stack:__
1. Stack is an ordered list of similar data type.
2. Stack is a __LIFO(Last in First out)__ structure or we can say FILO(First in Last out).
3. `push()` function is used to insert new elements into the Stack and `pop()` function is used to remove an element from the stack. Both insertion and removal are allowed at only one end of Stack called __Top__.
4. Stack is said to be in Overflow state when it is completely full and is said to be in Underflow state if it is completely empty.

- __Implementation of Stack using Linked List:__
It has the following operations :
- push: push an element into the stack
- pop: remove the last element added
- top(peek): returns the element at top of stack.

##### __Hash Table__



### __What is an Algorithm ?__

Algorithm is a finite step-by-step procedure, which defines a set of instructions to be executed in a certain order to get the desired output. Algorithm is not the complete code or program, as it is independent from any language; It is just the core logic(solution) of a problem.
There are no well-defined standards for writing algorithms. Rather, it is problem and resource dependent.

Example:
Problem − Design an algorithm to add two numbers and display the result.
Step 1 − START ADD
Step 2 − get values of a & b
Step 3 − c ← a + b
Step 4 − display c
Step 5 − STOP

Writing step numbers, is optional

__The important categories of algorithms:__
Search − search an item in a data structure.
Sort − sort items in a certain order.
Insert − insert item in a data structure.
Update − update an existing item in a data structure.
Delete − delete an existing item from a data structure.

__Characteristics of an Algorithm:__
Input- There should be 0 or more inputs supplied externally to the algorithm.
Output- There should be atleast 1 output obtained.
Definiteness- Every step of the algorithm should be clear and well defined.
Finiteness- The algorithm should have finite number of steps.
Correctness- Every step of the algorithm must generate a correct output.

__Algorithm Analysis:__
The efficiency of an algorithm can be analyzed at two different stages, before implementation and after implementation. 
They are the following −
- A Priori Analysis − This is a theoretical analysis of an algorithm where it is measured by assuming that all other factors, eg. processor speed, are constant and have no effect on the implementation.
- A Posterior Analysis − This is an empirical analysis of an algorithm whereby the selected algorithm is implemented using programming language. This is then executed on target computer machine. 
In this analysis, actual statistics like running time and space required, are collected.

An algorithm is said to be efficient and fast, if it takes less time to execute and consumes less memory space. The performance of an algorithm is measured on the basis of following properties :
- Time Complexity
- Space Complexity

__Space Complexity:__
Its the amount of memory space required by the algorithm life cycle, during the course of its execution. The space required by an algorithm is equal to the sum of the following two components:
- A fixed part that is a space required to store certain data and variables, that are independent of the size of the problem. Eg. simple variables and constants used, program size, etc.
- A variable part that is a space required by variables, whose size depends on the size of the problem. Eg. dynamic memory allocation, recursion stack space, etc.

__Time Complexity:__
Its a way to represent the amount of time required by the program to run till its completion. 
It's generally a good practice to try to keep the time required minimum, so that our algorithm completes it's execution in the minimum time possible.

When it comes to analysing the complexity of any algorithm in terms of time and space, we can never provide an exact number to define the time required and the space required by the algorithm, instead we express it using some standard notations, also known as Asymptotic Notations.
The word Asymptotic means approaching a value or curve arbitrarily closely (i.e., as some sort of limit is taken).
