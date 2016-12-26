class element:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
        self.size=0
    def push(self,data):
        node=element(data)
        if self.top==None:
            self.top=node
        else:
            node.next=self.top
            self.top=node
        self.size+=1
    def pop(self):
        if self.top!=None:
            data=self.top.data
            self.top=self.top.next
            self.size-=1
            return data
    def peck(self):
        if self.top!=None:
            return self.top.data

class MyQueue(object):
    def __init__(self):
        self.first = Stack()
        self.second = Stack()
    
    def peek(self):
        if self.second.size==0:
            while self.first.size>0:
                self.second.push(self.first.pop())
        data =self.second.peck()
        return data
    def pop(self):
        if self.second.size==0:
            while self.first.size>0:
                self.second.push(self.first.pop())
        data= self.second.pop()
        return data
    def put(self, value):
        self.first.push(value)
queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
        
