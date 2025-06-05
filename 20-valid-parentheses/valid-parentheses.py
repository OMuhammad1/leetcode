class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if not stack:
                    return False
                pop = stack.pop()
                if char == ')' and pop != '(':
                    return False 
                if char == '}' and pop != '{':
                    return False
                if char == ']' and pop != '[':
                    return False
                    
        if not stack:
            return True
        return False


                    
            
        