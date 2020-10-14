class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}
    def __repr__(self):
        return f'{self.data}'
    
    def _get_(self, index):
        return self.data[index]
    
    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length

    def _pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def shift_items(self, index):
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length -= 1


    def delete(self, index):
        item = self.data[index]
        self.shift_items(index)
        return self.data[self.length - 1]


new_arr = MyArray()
new_arr.push('hi')
new_arr.push('you')
new_arr.push('!')
new_arr.delete(0)
new_arr.push('are')
new_arr.push('nice')
new_arr.delete(1)
print(new_arr)
