class Node:
    def __init__(self,data):
        self.data=data
        self.child1=None
        self.child2=None

    def get_data(self):
        return self.data

    def get_Child_One(self):
        return self.child1
    
    def get_Child_Two(self):
        return self.child2



# root=Node("parent")
# c1=Node("1")
# root.child1=c1
# c2=Node("2")
# root.child2=c2
# c11=Node("3")
# c1.child1=c11

# p=root
# while p is not None:
    # print(p.child1.data)
    # print(p.child2.data)
    # p=p.child1
    # print(p.data)