class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def insert(self,data):
        if self.data==data:
            return False
        elif data<self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left=Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right=Node(data)
                return True
    def find(self,data):
        if self.data==data:
            return True
        elif data<self.data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False
    def inOrder(self):
        if self:
            if self.left:
                self.left.inOrder()
            print self.data
            if self.right:
                self.right.inOrder()

    def preOrder(self):
        if self:
            print self.data
            if self.left:
                self.left.preOrder()
            if self.right:
                self.right.preOrder()

    def postOrder(self):
        if self:
            if self.left:
                self.left.postOrder()
            if self.right:
                self.right.postOrder()
            print self.data

class Tree:
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root=Node(data)

    def find(self,data):
        if self.root:
            return self.root.find(data)
        else:
            return False
    def inOrder(self):
        print "inorder"
        self.root.inOrder()
    def preOrder(self):
        print "preorder"
        self.root.preOrder()
    def postOrder(self):
        print "postorder"
        self.root.postOrder()
bst=Tree()
bst.insert(14)
bst.insert(16)
bst.insert(12)
bst.insert(15)
bst.insert(11)
bst.insert(10)
bst.preOrder()
bst.inOrder()
bst.postOrder()