class Queue:
    def __init__(self):
        self.queue=[]
    def enQueue(self,item):
        self.queue.append(item)
    def deQueue(self):
        if len(self.queue)<1:
            return None
        self.queue.pop()
    def display(self):
        print("The Queue is :",self.queue)
    def size(self):
        return len(self.queue)
    def search(self,item):
        flag=False
        if (item in self.queue):
            return True
        else:
            return False
            
Q=Queue()
Q.enQueue(1)
Q.enQueue(2)
Q.enQueue(3)
Q.enQueue(4)
Q.enQueue(5)
Q.enQueue(123)
Q.display()
Q.deQueue()
Q.display()

itemNum=int(input("Enter a number :"))
if(Q.search(itemNum)):
    print("Value Exist")
else:
    print("Value do not Exist")