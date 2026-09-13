class Solution:
    def isValid(self, s: str) -> bool:
        
        pars = ['(','{','[']
        stack = []

        for c in s:
            if c in pars:
                stack.append(c)
            else:
                if(len(stack) == 0):
                    return False
                top = stack.pop()
                if (top == '(' and c != ')'):
                    return False
                if (top == '{' and c != '}'):
                    return False
                if (top == '[' and c != ']'):
                    return False

        if len(stack) > 0:
            return False
        
        return True