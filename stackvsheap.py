"""
===========================
📚 STACK vs HEAP in Python
===========================

In Python, memory is divided into two main regions:
    - 🥞 Stack Memory: for function calls and local variables.
    - 🧠 Heap Memory: for dynamic (object) allocation.

⚠️ NOTE: Python manages memory differently than low-level languages like C/C++.
Everything in Python is an object, and most data lives on the heap.
"""

# we can pop last element form list like this
A = [1,2,3,4,6,5]
print(A.pop())

# we can push last elememt in list like this
A = [1,2,3,4,5,6]
A.append(9)
print(A)

#If we just want to check last element
print(A[-1])



from collections import deque
stack = deque()
for i in range(10):
  stack.append(i*23)

print(stack.pop())

#this is like peek
print(stack[-1])



#implement stack usign LL

class Node:
   def __init__(self,val=0,next=None):
      self.val = val
      self.next = next

#stack Class:

class stack:
   def __init__(self):
      self.top = None
    
   def push(self,val):
      temp = Node(val)
      temp.next = self.top
      self.top = temp

   def disply(self):
      temp = self.top
      while temp:
         print(temp.val, end="->")
         temp = temp.next
         
      
s1 = stack()
s1.push(3)
s1.push(13)
s1.push(33)
s1.push(23)

s1.disply()



    



