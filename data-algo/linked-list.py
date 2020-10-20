#define Node class so we can initialize nodes that will go
#into linkedlist
class Node:
    def __init__(self, value):
        self.value = value #nodes value
        self.next = None #node's next on instantiation is none

class LinkedList:
    def __init__(self):
        self.head = None #store linked list head
        self.tail = None#store tail
        self.length = 0 #store length

    def _append(self, value):

        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

my_linked_list = LinkedList()
my_linked_list.prepend(20)
# my_linked_list._append(10)
# my_linked_list._append(15)
# my_linked_list._append(14)

print(my_linked_list.head.next)