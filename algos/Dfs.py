from stack import Stack
from path import root
from Tree import Node
from check import checker

start=root
end=str(input("between b-f"))

s=Stack()

count=1


s.append(root)
x=s.print()
while len(x) !=0:
    if len(x) == 0:
        print("no Solution")
    else:
        

        y=s.stack[-1]
        print(y.data)
        result=checker(y.data,end)
        print(result)
        if result is True:
            print(f"element found at {count}")
            exit()
        else:
            s.pop()
            if y.child1 is not None:
                s.append(y.child1)
            if y.child2 is not None:
                s.append(y.child2)
            count+=1
        

    

    







