class Queue:
    def __init__(self):
        self.items = []
        self.size = 0
    
    def enqueue(self, item):
        self.size = self.size + 1
        return self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            self.size = self.size - 1
            return self.items.pop(0)
    
    def is_empty(self):
        return self.size == 0

    def first(self):
        if not self.is_empty():
            return self.items[0]
    
    def get_queue(self):
        return self.items

    def __len__(self):
        return self.size

#Zavrsni ispit

#3)

    def brisi_svaki_drugi(self,R):
        
        rez=[]
        while not R.is_empty():
            rez.append(R.dequeue())
            R.dequeue()

            
        return rez
        


Q=Queue()
q=Queue()
q.enqueue(1)
q.enqueue(5)
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)

print(Q.brisi_svaki_drugi(q))
