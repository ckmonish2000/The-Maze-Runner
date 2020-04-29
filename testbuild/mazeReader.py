class Maze:
    def __init__(self,maze):
        with open(maze) as f:
            x=f.read()
            split=x.splitlines()
            self.start=None
            self.end=None
            self.initstate=None
            self.row=len(split)
            self.col=max(len(x) for x in split)
            self.wall=[]
            for i in range(self.row):
                       
                for j in range(self.col):
                    if(split[i][j]=='A'):
                        self.start=(i,j)
                        self.initstate=self.start
                        self.wall.append(False)
                    elif(split[i][j]=='B'):
                        self.end=(i,j)
                        self.wall.append(False)
                    elif(split[i][j]==''):
                        self.wall.append(False)
                    else:
                        self.wall.append(True)

    
    def print(self):
        print(f"start={self.start}")
        print(f"end={self.end}")
        print(f"initstate={self.initstate}")
        print(f"{self.wall}")

    def action(self):
        r,c=self.initstate
        moves=[
            ('up',(r-1,c)),
            ('down',(r+1,c)),
            ('left',(r,c-1)),
            ('right',(r,c+1))
            ]
        result=[]
        for action,(r,c) in moves:
            if (0 <= r >=self.row and 0 <= c < self.col and not self.walls[r][c]):
                result.append((action,(r,c)))
        return result