


class node():
    def __init__(self,value = None,next=None):
        self.value= value
        self.next=next

    def __str__(self):
        string = self.value
        if self.next:
            string += ',' + str(self.next)

        return string
    
class stack():
    def __init__(self):
        self.top= None
        self.minnode = None 

    def min(self):
        if not self.minnode:
            return None
        return self.minnode.value

    def push(self,item):
        if self.minnode and (self.minnode.value < item):
            self.minnode=node(value = self.minnode.value,next=self.minnode)
        else:
            self.minnode = node(value=item,next = self.minnode)
        self.top = node(value=item,next = self.top)

    def pop(self):
        if not self.top:
            return None
        self.minnode=self.minnode.next
        item = self.top
        self.top = self.top.next
        return item


customst = stack()
customst.push(5)
customst.push(4)
customst.push(3)
print(customst.min())
customst.pop()
nd = node()
print(nd)



