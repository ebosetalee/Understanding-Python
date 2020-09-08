### __What is Data Structure?__

Data structure is a programmatic way of collecting, storing and organizing data. 
TYPES OF DATA STRUCTURE:
Anything that can store data can be called as a data structure, hence Integer, Float, Boolean, Char etc, all are data structures. They are known as Primitive Data Structures.
Abstract Data Structure are :
- Linked List
- Tree
- Graph
- Stack, Queue etc.

The data structures can also be classified on the basis of the following characteristics:
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

Need for Data Structure:
- Data Search
- Processor Speed
- Multiple Requests

Basic Terminology
Data − Data are values or set of values.
Data Item − Data item refers to single unit of values.
Group Items − Data items that are divided into sub items are called as Group Items.
Elementary Items − Data items that cannot be divided are called as Elementary Items.
Attribute and Entity − An entity is that which contains certain attributes or properties, which may be assigned values.
Entity Set − Entities of similar attributes form an entity set.
Field − Field is a single elementary unit of information representing an attribute of an entity.
Record − Record is a collection of field values of a given entity.
File − File is a collection of records of the entities in a given entity set.

Data Definition:
It defines a particular data with the following characteristics:
Atomic − a single concept.
Traceable − mapped to some data element.
Accurate − unambiguous.
Clear and Concise − understandable.

Data Type
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
1. Both Linked List and Array are used to store linear data of similar type.

2. __DIFFERENCES__
ARRAY | LINKED LIST
Array is a collection of elements of similar data type.	| Linked List is an ordered collection of elements of same type, which are connected to each other using pointers.

Array supports Random Access, which means elements can be accessed directly using their index, like arr[0] for 1st element etc. Hence, accessing elements in an array is fast with a constant time complexity of O(1). | Linked List supports Sequential Access, which means to access any element/node in a linked list, we have to sequentially traverse the complete linked list, upto that element. To access nth element of a linked list, time complexity is O(n).

In array, elements are stored in contiguous memory location or consecutive manner in the memory. | In a linked list, new elements can be stored anywhere in the memory.

In array, Insertion and Deletion operation takes more time, as the memory locations are consecutive and fixed. | In linked list, a new element is stored at the first free and available memory location Thus, Insertion and Deletion operations are fast in linked list.

Memory is allocated as soon as the array is declared, at compile time. It's also known as Static Memory Allocation.	| Memory is allocated at runtime, as and when a new node is added. It's also known as Dynamic Memory Allocation.

In array, each element is independent and can be accessed using it's index value. |	In case of a linked list, each node/element points to the next, previous, or maybe both nodes.

Array can single dimensional, two dimensional or multidimensional | Linked list can be Linear(Singly), Doubly or Circular linked list.

Size of the array must be specified at time of array decalaration | Size of a Linked list is variable. It grows at runtime, as more nodes are added to it.

Array gets memory allocated in the Stack section. |	Whereas, linked list gets memory allocated in Heap section.

__NODE__
A Node in a linked list holds the data value and the pointer which points to the location of the next node in the linked list. In other words, it is a data value and a pointer (pointing to the next node) put together.


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

The important categories of algorithms :
Search − search an item in a data structure.
Sort − sort items in a certain order.
Insert − insert item in a data structure.
Update − update an existing item in a data structure.
Delete − delete an existing item from a data structure.

Characteristics of an Algorithm:
Input- There should be 0 or more inputs supplied externally to the algorithm.
Output- There should be atleast 1 output obtained.
Definiteness- Every step of the algorithm should be clear and well defined.
Finiteness- The algorithm should have finite number of steps.
Correctness- Every step of the algorithm must generate a correct output.

Algorithm Analysis:
The efficiency of an algorithm can be analyzed at two different stages, before implementation and after implementation. 
They are the following −
- A Priori Analysis − This is a theoretical analysis of an algorithm where it is measured by assuming that all other factors, eg. processor speed, are constant and have no effect on the implementation.
- A Posterior Analysis − This is an empirical analysis of an algorithm whereby the selected algorithm is implemented using programming language. This is then executed on target computer machine. 
In this analysis, actual statistics like running time and space required, are collected.

An algorithm is said to be efficient and fast, if it takes less time to execute and consumes less memory space. The performance of an algorithm is measured on the basis of following properties :
- Time Complexity
- Space Complexity

Space Complexity:
Its the amount of memory space required by the algorithm life cycle, during the course of its execution. The space required by an algorithm is equal to the sum of the following two components:
- A fixed part that is a space required to store certain data and variables, that are independent of the size of the problem. Eg. simple variables and constants used, program size, etc.
- A variable part that is a space required by variables, whose size depends on the size of the problem. Eg. dynamic memory allocation, recursion stack space, etc.

Time Complexity:
Its a way to represent the amount of time required by the program to run till its completion. 
It's generally a good practice to try to keep the time required minimum, so that our algorithm completes it's execution in the minimum time possible.

When it comes to analysing the complexity of any algorithm in terms of time and space, we can never provide an exact number to define the time required and the space required by the algorithm, instead we express it using some standard notations, also known as Asymptotic Notations.
The word Asymptotic means approaching a value or curve arbitrarily closely (i.e., as some sort of limit is taken).
