class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
         # Step 1: Mapping of Roman symbols to integers
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Step 2: Initialize total and get the length of the string
        total = 0
        n = len(s)
        
        # Step 3: Traverse the string from left to right
        for i in range(n):
            # If the current value is less than the next value, subtract it
            if i < n - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                # Otherwise, add it to the total
                total += roman_map[s[i]]
        
        return total
        pass



