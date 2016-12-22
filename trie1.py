class node:
    def __init__(self):
        self.children={}
        self.endofWord=False
               
class tri:
    def __init__(self):
        self.root=node();
    def addWord(self,word):
        current=self.root
        for w in word:
            child=node()
            if w not in current.children:
                #print w,
                current.children[w]={'child':child,'count':1}
                current=child
            else:
                current.children[w]['count']=current.children[w]['count']+1
                #print w,current.children[w]['count']
                current=current.children[w]['child']
               
        current.endofWord=True
        #print
        
    def printTri(self):
        current=self.root
        for key in current.children:
            print key
            self.printKey(current.children[key])
    def printKey(self,child):
        for key in child.children:
            print key,len(child.children)
            self.printKey(child.children[key])
            
    def searchPrefix(self,word):
        current=self.root
        count=0
        for i in xrange(len(word)):
            if word[i] not in current.children:
                print 0
                return
            else:
                #print "before",word[i],current.children[word[i]]['count']
                if i!=len(word)-1:
                    current=current.children[word[i]]['child']
                
        print current.children[word[i]]['count']
        
    
'''
Tri=tri()
Tri.addWord('tandra')
print "added tandra"
Tri.addWord('tabkal')
print "added tabkal"
Tri.addWord('tadl')
print "added tadl"
Tri.addWord('tapq')
print "added tapq"
Tri.addWord('yuo')
print "added yuo"
Tri.addWord('Hel')
print "added Hel"
#Tri.printTri()
Tri.searchPrefix('ta')
Tri.searchPrefix('tal')'''
Tri=None
n = int(raw_input().strip())
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    if op=='add':
        if not Tri:
            Tri=tri()
        Tri.addWord(contact)
    elif op=='find':
        if not Tri:
            print 0
        else:
            Tri.searchPrefix(contact)
    
