# Singly Linked List
# 1. Define a class Node to define a node of a Singly Linked List.
# 2. Define a class SLL to implement Singly Linked List with __init__() method to create and initialize start reference variable.
# 3. Define a method is_empty() to check if the linked list is empty in SLL class.
# 4. In class SLL, define a method insert_at_start() to insert an element at the starting of the list.
# 5. In class SLL, define a method insert_at_last() to insert an element at the end of the list.
# 6. In class SLL, define a method search() to find the node with specified element value.
# 7. In class SLL, define a method insert_after() to insert a new node after a given node of the list.
# 8. In class SLL, define a method to print all the elements of the list.
# 9. In class SLL, implement iterator for SLL to access all the elements of the list in a sequence.
# 10. In class SLL, define a method delete_first() to delete first element from the list.
# 10. In class SLL, define a method delete_last() to delete last element from the list.
# 11. In class SLL, define a methos delete_item() to delete specified element from the list.

# Singly Linked List Implementation

class Node:
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self, start = None):
        self.start = start

    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self, data):
        node = Node(data, self.start)
        self.start = node
    
    def insert_at_last(self, data):
        node = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = node
        else:
            self.start = node

    def search(self, data):
        temp = self.start;
        while temp.next is not None:
            if(temp.item == data):
                return temp
            temp = temp.next
        return None
    
    def insert_after(self, targetNode, data):
            if targetNode is not None:
                newNode = Node(data, targetNode.next)
                targetNode.next = newNode

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end = '->')
            temp = temp.next


# Driver Code

myList = SLL();
myList.insert_at_start(10) 
myList.insert_at_start(20)
myList.insert_at_last(40)
myList.insert_at_last(30)
myList.print_list()
    