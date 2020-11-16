def reverse_string_iterative(s):
    result_str = ""
    for i in range(len(s)):
       
        result_str += s[(len(s) - 1) - i]
    return result_str
    # swap letters 

def reverse_string_recursive(s):
    if s == "":
        return ""
    
    return reverse_string_recursive(s[1:]) + s[0]

print(reverse_string_iterative("yoyo mastery"))
print(reverse_string_iterative("canelita"))

print(reverse_string_recursive("yoyo mastery"))
print(reverse_string_recursive("canelita"))