class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'{self.value}'

class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    
 

    def peek(self):
        return self.first

    def enqueue(self, value):
        new_node = Node(value)
        if self.last == None:
            self.last = new_node
            self.first = self.last

       
        
        else:
            self.last.next = new_node
            self.last = new_node

            
        self.length += 1
       

    def dequeue(self):
        if self.length == 0:
            return "Empty"
        if self.last == self.first:
            self.last = None
        
        first_node = self.first

        self.first = self.first.next

        self.length -= 1
        return first_node




my_queue = Queue()
my_queue.enqueue('Joy')
my_queue.enqueue('Matt')
my_queue.enqueue('Pavel')
my_queue.enqueue('Samir')
print(my_queue.length)
print(my_queue.peek())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.first, my_queue.last)
