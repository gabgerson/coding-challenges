"""Create a function that reverses a string:
   'Hi my name is Gaby' should be 'ybaG si eman ym iH'
"""
#using str splicing
def reverse_str_splice(s):
    return s[::-1]

#using loop and swaping items using 1st and last indexes

def reverse_str(s):
    if s != str or len(s) < 2:
        return "please input a string longer that 1 character"
    #start index
    begin = 0
    #end index
    end = len(s) - 1
    #turn string into list
    s_lst = list(s)
    # loop as long as end index greater than begin index
    while end > begin:
        #begin ==end swap them
        s_lst[begin], s_lst[end] = s_lst[end], s_lst[begin]
        #increment and decrement indexes
        begin += 1
        end -= 1
    #turn list back to str
    return ''.join(s_lst)

def reverse_str2(s):
    r = ''
    for i in range(len(s)-1, 0 -1, -1):
        r += s[i]
    return r
    
def reverse_str3(s):
    r = ''
    i = len(s) - 1
    
    for char in s:
        r += s[i]
        i -= 1

        
    return r
print(reverse_str_splice('Hi my name is Gaby'))
print(reverse_str('Hi my name is Gaby'))
print(reverse_str2('Hi my name is Gaby'))
print(reverse_str3('Hi my name is Gaby'))

print(reverse_str(0))
print(reverse_str('H'))