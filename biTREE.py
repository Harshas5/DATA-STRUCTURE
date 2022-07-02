class treenode:
    def __init__(self,data):
        self.data = data
        self.leftchild=None
        self.rightchild =None

btree=treenode("drinks")
leftchild = treenode('hot')
rightchild=treenode('cold')
btree.leftchild=leftchild
btree.rightchild=rightchild
tea = treenode('tea')
cfe=treenode('cfe')
juice = treenode('juice')
leftchild.leftchild=tea
leftchild.rightchild=cfe
rightchild.leftchild=juice




def preeordertrv(rootnode):
    if not rootnode:
        return
    print(rootnode.data)
    preeordertrv(rootnode.leftchild)
    preeordertrv(rootnode.rightchild)

#preeordertrv(btree)

def inordertrv(rootnode):
    if not rootnode:
        return
    
    preeordertrv(rootnode.leftchild)
    print(rootnode.data)
    preeordertrv(rootnode.rightchild)

#inordertrv(btree)

def postordertrv(rootnode):
    if not rootnode:
        return
    
    preeordertrv(rootnode.leftchild)
    
    preeordertrv(rootnode.rightchild)
    print(rootnode.data)

postordertrv(btree)

