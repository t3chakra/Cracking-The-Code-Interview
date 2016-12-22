class element:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def push(self,data):
        node=element(data)
        if self.top==None:
            self.top=node
        else:
            node.next=self.top
            self.top=node
    def peck(self):
        if not self.isEmpty():
            return self.top.data
        else:
            return ' '
    def pop(self):
        if not self.isEmpty():
            data=self.top.data
            self.top=self.top.next
            return data
        else:
            return ' '
    def isEmpty(self):
        return self.top==None
    def printS(self):
        cur=self.top
        if not self.isEmpty():
            while cur.next!=None:
                print cur.data
                cur=cur.next
            print cur.data
stackTemp=Stack()
def balanced(bracket):
    br=['{','(','[','}',')',']']
    i=br.index(bracket)
    if i<3:
        return br[i+3]
    else:
        return br[i-3]
def check(stack):
    
    cur=stack.pop()
    exp=balanced(cur)
    if exp==stack.peck():
        stack.pop()
    else:
        if stackTemp.peck()==exp:
            stackTemp.pop()
        else:
            stackTemp.push(cur)
            
    #stack.printS()
    #print "current time stack"
    #stackTemp.printS()
    #print "current temporary stack"
    return stack
def is_matched(expression):
    while not stackTemp.isEmpty():
        stackTemp.pop()
    if len(expression)%2==0:
        stack =Stack()
        for i in xrange(len(expression)):
            stack.push(expression[i])
        #print "stack for first time"
        #stack.printS()
        #print "=========================="
        while not stack.isEmpty():
            stack=check(stack)
        #print stack.isEmpty()
        #print stackTemp.isEmpty()
        if stack.isEmpty() and stackTemp.isEmpty():
            return True
        else:
            return False            
    else:
        return False

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
