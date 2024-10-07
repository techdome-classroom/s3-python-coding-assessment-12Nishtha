class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        # Dictionary to map each closing bracket to its corresponding opening bracket
        matching_brackets = {')': '(', '}': '{', ']': '['}
        
        # Iterate through the characters in the string
        for char in s:
            if char in matching_brackets:
                # If the stack is empty, we use '#' as a dummy value for comparison
                top_element = stack.pop() if stack else '#'
                
                # Check if the top element matches the current closing bracket
                if matching_brackets[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push onto the stack
                stack.append(char)
        
        # Return True if the stack is empty, meaning all brackets are matched correctly
        return not stack
        pass







    



  

