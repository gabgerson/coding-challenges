def twoStrings(s1, s2):
    #store chars from s1 in set
    seen_s1 = set()

    #loop though s1 and add chars to set

    for char in s1:
        seen_s1.add(char)
    #loop through s2 and compare chars to chars in seen set
    #if an s2 char is in seen set return YES
    for char in s2:
        if char in seen_s1:
            return "YES"
    return "NO"
