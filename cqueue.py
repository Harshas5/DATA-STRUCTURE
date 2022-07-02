class ccque:
    def __init__(self,maxSize):
        self.item = maxSize* [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self):
        value = [str(x) for x in self.item]
        return (" ").join(value)

    def isfull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top +1 == self.maxSize:
            return True
        else:
            return False

    def isempty(self):
        if self.top == -1:
            return True
        else:
            return False

    def enque(self,value):
        if self.top+1 == self.maxSize:
            self.top =0

        else:
            self.top+=1
            if self.start == -1:
                self.start=0
        self.item[self.top] = value
        return 'added to list'
        


Cq = ccque(3)
print(Cq.isempty())
Cq.enque(1)
Cq.enque(2)
Cq.enque(3)
print(Cq)


    