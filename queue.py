class queue:
    def __init__(self):
        self.item = []

    def __str__(self):
        values = [str(x) for x in self.item]
        return ' '.join(values)

    def isemoty(self):
        if self.item == []:
            return True
        else:
            return False

    def enquee(self,values):
        self.item.append(values)
        return 'the item is inserted into queue'
        
        
        
qq = queue()
print(qq.isemoty())
print(qq.enquee(5))


        