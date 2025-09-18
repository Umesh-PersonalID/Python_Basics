from queue import Queue

class stack:
  def __init__(self):
    self.q = Queue()


  def push(self,x):
    s = self.q.qsize()
    self.q.put(x)
    for i in range(s):
      self.q.put(self.q.get())
  
  def top(self):
    return self.q.queue[0]
  
  def pop(self):
    self.q.get()
    pass

  def size(self):
    return len(self.q)
  
st = stack()
st.push(2)
st.push(3)
st.push(4)
st.push(5)
st.push(8)
st.pop()
st.pop()
print(st.top())