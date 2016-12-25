class Node:
    def __init__(self,id):
        self.id=id
        self.adjacent=[]
class Graph:
    def __init__(self,n):
        self.noOfVertices=n
        self.nodeList={}
        for i in xrange(1,self.noOfVertices+1):
            node=Node(i)
            self.nodeList[i]=node
    def getNode(self,id):
        if id in self.nodeList:
            return self.nodeList[id]
    def connect(self,src,dest):
        s=self.getNode(src)
        d=self.getNode(dest)
        s.adjacent.append(d)
        d.adjacent.append(s)
    def printGraph(self):
        for s in self.nodeList:
            print self.nodeList[s].id,
            for d in self.nodeList[s].adjacent:
                print d.id,
            print 
    def find_all_distances(self,s):
        src=self.getNode(s)
        for node in self.nodeList:
            dest=self.getNode(node)
            if dest!=src: 
                print self.hasPathBFS(src,dest),
        print
    def hasPathBFS(self,src,dest):
        visited=[]
        nextToVisit=[]
        parent={}
        distance={}
        nextToVisit.append(src)
        distance[src.id]=0
        #print src.id, dest.id
        while len(nextToVisit)>0:
            node=nextToVisit.pop(0)
            if node==dest:
                return distance[node.id]
                #return self.pathToParent(parent,src.id,dest.id)
            if node.id in visited:
                continue
            visited.append(node.id)    
               
            for child in node.adjacent:
                #if node.id in parent and parent[node.id]==child.id:
                 #   skip=1
                #else:
                 #   parent[child.id]=node.id
                distance[child.id]=distance[node.id]+6
                nextToVisit.append(child)
        return -1
    def pathToParent(self,parent,src,dest):
        path = [dest]
        #print parent
        while path[-1] != src:
            #print "parent of ",path[-1], "is", parent[path[-1]]
            path.append(parent[path[-1]])
        return 6*(len(path)-1)
            
t = input()
for i in range(t):
    n,m = [int(x) for x in raw_input().split()]
    graph = Graph(n)
    for i in xrange(m):
        x,y = [int(x) for x in raw_input().split()]
        graph.connect(x,y) 
    s = input()
    graph.find_all_distances(s)
    
