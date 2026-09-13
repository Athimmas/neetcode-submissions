class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minstack:
            self.minstack.append(val)
        elif val <= self.minstack[-1]:
            self.minstack.append(val)

    def pop(self) -> None:

        if self.stack:
            val = self.stack.pop()
        else:
            return None

        if val == self.minstack[-1]:
            self.minstack.pop()

        return

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.minstack:
            return

        return self.minstack[-1]