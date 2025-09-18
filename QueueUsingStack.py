from queue import LifoQueue

#LifoQueue is the stack in python

#I will need 2 stack to implement Queue using Stack

#For Push Operation
# 1. Stack1 to Stack2 2. Push X on Stack1 2. Take everything back from Stake2 to Stack1




class Queue:
  def __init__(self):
    self.st1 = LifoQueue()
    self.st2 = LifoQueue()

  def push(self,x):
    while not self.st1.empty():
      self.st2.put(self.st1.get())
    self.st1.put(x)
    while not self.st2.empty():
      self.st1.put(self.st2.get())      
 

  def pop(self):  
    p = self.st1.get()
    return p


  def top(self):
    return self.st1.top()
  


q1 = Queue()
q1.push(2)
q1.push(5)
q1.push(26)
q1.push(9)
q1.push(100)

print(q1.pop())