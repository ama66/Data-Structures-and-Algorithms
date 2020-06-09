class HeapEmptyError(Exception):
    pass

class Heap:
    def __init__(self,maxsize=50):
        self.a=[None]*maxsize
        self.n=0
        self.a[0]=float("inf")
        
    def insert(self,val):
        self.n+=1
        self.a[self.n]=val
        self.restore_up(self.n)
        
    def restore_up(self,i):
        val=self.a[i]
        i_par=i//2 
        
        while self.a[i_par]< val : 
            self.a[i]=self.a[i_par]
            i=i_par
            i_par=i//2 
        # once out of the while loop all parent nodes moved down where they should be 
        ## and now it's time to reinstate self.a[i]
        self.a[i]=val 
        
    def delete(self):
        if self.n==0:
            raise HeapEmptyError("Heap is Empty")
        maxval=self.a[1]  
        self.a[1]=self.a[self.n]
        self.a[self.n]=None
        self.n-=1
        self.restore_down(1) 
        return maxval 
    
    def restore_down(self,i):
        val=self.a[i]
        lchild=2*i
        rchild=lchild+1
        ## last possible position is self.n 
        while rchild < self.n: 
            if val > self.a[lchild] and val > self.a[rchild]:
                self.a[i]=val
                return 
            else:
                if self.a[lchild]> self.a[rchild]:
                    self.a[i]=self.a[lchild]
                    i=lchild
                else:
                    self.a[i]=self.a[rchild]
                    i=rchild
            lchild=2*i
            rchild=lchild+1
            
        ## If I exit while where n is odd that means a left child was not checked 
        if lchild==self.n and self.a[lchild] > val:
            self.a[i]=self.a[lchild]
            i=lchild 
            
        self.a[i]=val
        
    @staticmethod
    def heapify_top_down(H):
        ## H is an Array 
        n=len(H)
        x=Heap()
        for i in range(1,n+1):
            x.a[i]=H[i-1]
        x.n=n 
        
        ## Now heapify top down
        for i in range(2,n+1):
            x.restore_up(i)
            
        return x
    
    @staticmethod   
    def heapify_bottom_up(H):
        ## 
        n=len(H)
        x=Heap()
        for i in range(1,n+1):
            x.a[i]=H[i-1]
            
        x.n=n 
        # first non-leaf node   
        i=n//2
        while i >=1:
            x.restore_down(i)
            i-=1
        return x
    
    h=Heap()
h.insert(35)
h.insert(38)
h.insert(59)
h.delete()

59

H=[20,33,15,6,40,60,45,16,75,10,80,12]
x=Heap.heapify_top_down(H)
x.a
[inf,
 80,
 75,
 45,
 33,
 60,
 15,
 40,
 6,
 16,
 10,
 20,
 12,
 None,
 None,
 ...]

H=[20,33,15,6,40,60,45,16,75,10,80,12]
x=Heap.heapify_bottom_up(H)
x.a
[inf,
 80,
 75,
 60,
 20,
 40,
 15,
 45,
 16,
 6,
 10,
 33,
 12,
 None,
 None,
 None,
 ...]

## Note how non-unique the resulting heap is. We get different heaps but all properties are satisified in both cases

