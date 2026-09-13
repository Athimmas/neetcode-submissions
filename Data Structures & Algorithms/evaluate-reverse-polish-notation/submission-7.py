class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        ans = 0
        Map = {'+','-','*','/'}

        for token in tokens:
            if token not in Map:
                stack.append(int(token))
                continue
            
            print(stack)

            op2 = stack.pop()
            op1 = stack.pop()

            if token == '+':
                ans = op1 + op2
            if token == '-':
                ans = op1 - op2
            if token == '*':
                ans = op1 * op2
            if token == '/':
                ans = int(float(op1)/op2)

            stack.append(ans)

        return stack[0]




            