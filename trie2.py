class node:
    def __init__(self,char):
        self.children=[]
	self.char=char
	self.count=1
        self.endofWord=False
    def getChild(self,char):
	for child in self.children:
		if child.char==char:
			return child
	return None           
class tri:
    def __init__(self):
        self.root=node('*');
    

    def addWord(self,word):
        current=self.root
        for w in word:
            child=current.getChild(w)
            if child is None:
                #print w,
               	child=node(w)
		current.children.append(child)
            else:
		current.count+=1
            current=child
        current.endofWord=True

    def searchPrefix(self,word):
        current=self.root
        for w in word:
	    child=current.getChild(w)
	    if child is None:
		print 0
		return 
	    else:
		current=child
	print current.count
		
    
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
    
