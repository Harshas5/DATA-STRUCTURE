class stack:
    def __init__(self):
        self.list = []

    def __str__(self) :
        values  = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def isempty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self,value):
        self.list.append(value)

    def pop(self):
        if self.isempty():
            return ' it is empty'
        else:
            return self.list.pop()


custom = stack()
custom.push(1)
custom.push(2)

custom.push(3)

custom.push(4)
print(custom)

print("       ")
print(custom.pop())
#print(custom.isempty())
#print(custom)

