#!/bin/python
import sys
import math
class heap:
    def __init__(self):
        self.size=0
        self.items=[]
    def getLeftChildIndex(self,index):
        return 2*index+1
    def getRightChildIndex(self,index):
        return 2*index+2
    def parentIndex(self,index):
        return (index-1)/2
    def hasLeftChild(self,index):
        return self.getLeftChildIndex(index) < self.size
    def hasRightChild(self,index):
        return self.getRightChildIndex(index) < self.size
    def hasParent(self,index):
        return self.parentIndex(index)>=0
    def leftChild(self,index):
        return self.items[self.getLeftChildIndex(index)]
    def rightChild(self,index):
        return self.items[self.getRightChildIndex(index)]
    def parent(self,index):
        return self.items[self.parentIndex(index)]
    def peck(self):
        if self.size>0:
            return self.items[0]
        else:
            return None
    def swap(self,index1,index2):
        temp=self.items[index1]
        self.items[index1]=self.items[index2]
        self.items[index2]=temp
class maxHeap:
    def __init__(self):
        self.root=heap()
    def insertMax(self,data):
        self.root.items.append(data)
        self.root.size+=1
        if self.root.size>1:
            self.heapifyUp()
    
    def heapifyUp(self):
        index=self.root.size-1
        while self.root.hasParent(index) and self.root.parent(index)<self.root.items[index]:
                self.root.swap(self.root.parentIndex(index),index)
                index=self.root.parentIndex(index)
    def delMax(self):
        if self.root.size>0:
            data=self.root.items[0]
            self.root.swap(self.root.size-1,0)
            self.root.items.pop()
            self.root.size-=1
            self.heapifyDown()
            return data
    def heapifyDown(self):
        index=0
        while self.root.hasLeftChild(index):
            maxChildIndex=self.root.getLeftChildIndex(index)
            if self.root.hasRightChild(index) and self.root.rightChild(index)>self.root.leftChild(index):
                maxChildIndex=self.root.getRightChildIndex(index)
            if self.root.items[index]>self.root.items[maxChildIndex]:
                break
            else:
                self.root.swap(index,maxChildIndex)
            index=maxChildIndex
            
      
        
class minHeap:
    def __init__(self):
        self.root=heap()
    def insertMin(self,data):
        self.root.items.append(data)
        self.root.size+=1
        #print self.root.size
        if self.root.size>1:
            self.heapifyUp()
    def heapifyUp(self):
        index=self.root.size-1
        while self.root.hasParent(index) and self.root.parent(index)>self.root.items[index]:
                   self.root.swap(self.root.parentIndex(index),index)
                   index=self.root.parentIndex(index)
        #print self.root.items
    def delMin(self):
        if self.root.size>0:
            data=self.root.items[0]
            self.root.swap(self.root.size-1,0)
            self.root.items.pop()
            self.root.size-=1
            self.heapifyDown()
            return data
    def heapifyDown(self):
        index=0
        while self.root.hasLeftChild(index):
            minChildIndex=self.root.getLeftChildIndex(index)
            if self.root.hasRightChild(index) and self.root.rightChild(index)<self.root.leftChild(index):
                minChildIndex=self.root.getRightChildIndex(index)
            if self.root.items[index]<self.root.items[minChildIndex]:
                break
            else:
                self.root.swap(index,minChildIndex)
            index=minChildIndex

maxH=maxHeap()
minH=minHeap()        
def sortIt(key):
        #print t
        
        if key<maxH.root.peck():
            maxH.insertMax(key)
        else:
            minH.insertMin(key)
                #print "done"
        if  maxH.root.size>1 and maxH.root.size>minH.root.size:
            data=maxH.delMax()
            minH.insertMin(data)
        elif minH.root.size>1 and maxH.root.size<minH.root.size:
             data=minH.delMin()
             maxH.insertMax(data)
        #print "maxHeap",maxH.root.items
        #print "minHeap",minH.root.items
        if minH.root.size==maxH.root.size:
            #print "balanced"
            median=(float(minH.root.peck())+float(maxH.root.peck()))/2
            return median
        else:
            #print "imbalanced"
            if minH.root.size>maxH.root.size:
                return minH.root.peck()
            else:
                return maxH.root.peck()
    
n = int(raw_input().strip())
#print n
a = []
a_i = 0
for a_i in xrange(n):
    a_t = int(raw_input().strip())
    #a.append(a_t)
    median=sortIt(a_t)
    print '%.1f' % median
   
