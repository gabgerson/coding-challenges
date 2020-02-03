def roman_to_int(s):
        """
        :type s: str
        :rtype: int
        """
        #from https://leetcode.com/problems/roman-to-integer
        roman_int_dict = { 
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000   
        }        
        
        total = 0
        i = 0
        while i <= len(s) - 1:
        
            #if current index is the last in the string addd that to the total and return total
            if i == len(s) - 1:
                total += roman_int_dict[s[i]]
                return total
                
            #if current numeral's value is less than next numeral's value 
            #subtract current numeral from next numeral and add to total
            elif roman_int_dict[s[i]] < roman_int_dict[s[i + 1]]:
                total += (roman_int_dict[s[i + 1]] -  roman_int_dict[s[i]])
                i += 2
            else:
                total += roman_int_dict[s[i]]
                i += 1
        return total
