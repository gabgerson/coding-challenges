def is_happy(n):

       #from https://leetcode.com/problems/happy-number
        visited = set()
    
        s = None
    
        while s is not 1:
            
            visited.add(s)
            
            s = sum(int(i) ** 2 for i in str(n))
            n = s
    
            if s in visited:
                return False
            
            
            if s == 1: 
                return True
