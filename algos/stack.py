class Stack:
    def __init__(self):
        self.stack=[]

    def append(self,val):
        if val not in self.stack:
            self.stack.append(val)
            return True
        else:
            return False
    
    def first_ele(self):
        return self.stack[-1]
    
    def pop(self):
        if len(self.stack) <=0:
            return "stack empty"
        else:
            return self.stack.pop()
    
    def print(self):
        return self.stack



# s=Stack()

# s.append(1)
# s.append(2)
# s.append(3)
# print(s.print())
# s.pop()
# print(s.print())


# s.first_ele()
# s.pop()