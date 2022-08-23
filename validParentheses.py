class Solution(object):
    def isValid(self, s):
        # return false if odd number of characters
        if len(s) % 2 != 0:
            return false
        dict = { ')' : '(', ']' : '[', '}' : '{' }
        stack = []
        for x in s:
            if x in dict:
                if stack and stack[-1] == dict[x]:
                    stack.pop() # if first and last values match parentheses, pop from stack
                else: # false if empty stack/parentheses don't match
                    return False
            else: # if open parentheses, add to stack
                stack.append(x)
            
        return True if not stack else False
                
