class MinStack:

    def __init__(self):
        self.stack=[] #stores all
        self.min_stack =[] #stores min values
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack or val<=self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            top = self.stack.pop()
        if top==self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None
        
