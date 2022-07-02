class Treenode:
    def __init__(self,data,children =[]):
        self.data = data
        self.children = children

    def __str__(self,level=0):
        ret = " "*level+str(self.data)+"\n"
        for child in self.children:
            ret+=child.__str__(level+1)
        return ret

    def addchild(self,node):
        self.children.append(node)

tree =Treenode('drinks',[])
cold =Treenode('cold',[])
hot =Treenode('hot',[])
tree.addchild(cold)
tree.addchild(hot)
print(tree)
tea =Treenode('tea',[])
wiski =Treenode('wiski',[])
bear =Treenode('bear',[])
cold.addchild(bear)
hot.addchild(tea)
print(tree)

