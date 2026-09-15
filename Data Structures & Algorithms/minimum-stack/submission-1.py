# try storing a tuple instead of one single value so that we also have the second value in the tuple representing the minimum val !!!!

class MinStack:

    def __init__(self):
        self.st=[]
        

    def push(self, val: int) -> None:
        if not self.st:
            self.st.append((val,val))
        else:
            curr_min=self.st[-1][1]
            new_min=min(curr_min,val) 
            self.st.append((val,new_min))     

    def pop(self) -> None:
        self.st.pop()
        

    def top(self) -> int:
        return self.st[-1][0]
        

    def getMin(self) -> int:
        return self.st[-1][1]
        
