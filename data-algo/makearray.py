class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}
    
    def _get_(self, index):
        return self.data[index]


new_arr = MyArray()
print(new_arr.data, new_arr.length)