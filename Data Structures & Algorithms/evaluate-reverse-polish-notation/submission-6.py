class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:
            
            if token.lstrip("+-").isdigit():
                stack.append(int(token))
                print(stack)
                continue

            operand2 = stack.pop()
            operand1 = stack.pop()

            ans = 0

            if(token == '+'):
                ans = operand1 + operand2
            if(token == '-'):
                ans = operand1 - operand2
            if(token == '*'):
                ans = operand1 * operand2
            if(token == '/'):
                ans = int(float(operand1) / operand2)

            stack.append(ans)
            print(stack)

        return stack[0]

            