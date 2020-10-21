class Node:

    def __init__(self, value):
        self.value = value #nodes value
        self.next = None #node's next on instantiation is none
        self.prev = None

class DoublyLinkedList:

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
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def print_list(self):
        ls = list()
        if self.head == None:
            print("Empty")
           
        else:
            current_node = self.head

            while current_node != None:
                ls.append(current_node.value)
                current_node = current_node.next
        print(ls)
        

    def _insert(self, index, value):
        if index == 0:
            self.prepend(value)
            return self.print_list()
        elif index >= self.length:
            self._append(value)
            return self.print_list()
        else:
            current_node = self.head
            new_node = Node(value)
            i = 0

            while i <= index:

                if i == index - 1:
                    new_node.prev = current_node
                    new_node.next = current_node.next
                    current_node.next = new_node
                    new_node.next.prev = new_node
                    self.length += 1
                    return self.print_list()
                    
                current_node = current_node.next
                i +=1
            
    def _remove(self,index):
        # if index = 0 make self.head current self.head.next

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return self.print_list()

        elif index >= self.length:
            print(" No Node at Index ")
            return self.print_list()
        else:

            current_node = self.head

            
            i = 0

            while i <= index:

                if i == index - 1:
                    if current_node.next.next == None:
                        self.tail = current_node

                    current_node.next = current_node.next.next

                    if current_node.next != None:

                        current_node.next.prev = current_node

                    self.length -= 1

                    return self.print_list()
                    
                current_node = current_node.next
                i +=1


my_linked_list = DoublyLinkedList()
my_linked_list.prepend(20)
my_linked_list._append(10)
my_linked_list._append(15)
my_linked_list._append(14)
my_linked_list.print_list()
my_linked_list._insert(3, 50)
my_linked_list._remove(4)
print(my_linked_list.tail.prev.prev.prev.value)
print(my_linked_list.tail.value)
print(my_linked_list.head.next.value)
print(my_linked_list.length)