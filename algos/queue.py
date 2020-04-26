from stack import Stack

class queue(Stack):
    def pop(self):
        if len(self.stack) <=0:
            return "queue empty"
        else:
            return self.stack[1:]