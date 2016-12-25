class Graph:
    def __init__(self,n):
        self.noOfVertices=n
        self.nodeList=[[] for x in xrange(n)]
    def connect(self,src,dest):
        self.nodeList[src].append(dest)
        self.nodeList[dest].append(src)
    def find_all_distances(self,src):
        distances=[-1 for x in xrange(self.noOfVertices)]
        nextToVisit=[]
        nextToVisit.append(src)
        distances[src]=0
        while len(nextToVisit)>0:
            node=nextToVisit.pop(0)
            for child in self.nodeList[node]:
                if child!=None and distances[child]==-1:
                    distances[child]=distances[node]+6
                    nextToVisit.append(child)
        for i in xrange(len(distances)):
            if distances[i]!=0:
                print distances[i],
        print
            
t = input()
for i in range(t):
    n,m = [int(x) for x in raw_input().split()]
    graph = Graph(n)
    for i in xrange(m):
        x,y = [int(x) for x in raw_input().split()]
        graph.connect(x-1,y-1) 
    s = input()
    graph.find_all_distances(s-1)
