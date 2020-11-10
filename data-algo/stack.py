class Node:

    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:

    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    
    def peek(self):
        #show top item
        return self.top.value

    def push(self, value):
        
        #if nothing is in the stack item being pushed is bottom and top
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        
        else:
            
            #new_node's next is current top
            new_node.next = self.top
            #add node to top of stack
            self.top = new_node

        self.length += 1
        

    def _pop(self):
        #if nothing is in the stack print(empty)
        if self.top == None:
            print("No Top")
        else:
       
            if self.top == self.bottom:
                self.bottom = None
            #get top 
            popped_node = self.top
            #set top to current self.top's next

            self.top = self.top.next
            self.length -= 1
            #if top is None then list is empty so reset bottom to None
            

            return popped_node.value


    def print_stack(self):
        ls = list()
        if self.top == None:
            print("Empty")
            return
       
        else:
            current_node = self.top
            while current_node != None:
                ls.append(current_node.value)
                current_node = current_node.next
        print(ls)

my_stack = Stack()

my_stack.push(5)
my_stack.push(7)
my_stack.push(8)
my_stack.push(9)
my_stack.push(10)
my_stack.push(20)

my_stack.print_stack()
print(my_stack.bottom.value)
print(my_stack.top.value)
print(my_stack.bottom.next, 'next')
print(my_stack.top.next.next, 'next')

print(my_stack._pop())
print(my_stack._pop())
print(my_stack._pop())
print(my_stack._pop())
print(my_stack._pop())
print(my_stack._pop())
print(my_stack.bottom)
my_stack.print_stack()
