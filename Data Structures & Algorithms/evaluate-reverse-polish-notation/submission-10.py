class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

        stack = []
        operators = ['+','-','*','/']

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                res = 0

                if token == "+":
                    res = op1 + op2
                elif token == "-":
                    res = op1 - op2
                elif token == "*":
                    res = op1 * op2
                elif token == "/":
                    res = int(float(op1) / op2)

                stack.append(res)

        return stack[-1]