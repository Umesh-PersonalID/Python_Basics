A = [-4,3,-7,1,2,6,2,3,4,9,10]

import heapq
heapq.heapify(A)

print(A)

#heappush insert o(logn)

heapq.heappush(A,40)

print(A)

minn = heapq.heappop(A)
print(minn)
minn = heapq.heappop(A)
print(minn)
minn = heapq.heappop(A)
print(minn)
minn = heapq.heappop(A)
print(minn)
minn = heapq.heappop(A)
print(minn)

def heapsort(A):
  new_lst = [0]*len(A)
  heapq.heapify(A)
  for i in range(len(A)):
    minn = heapq.heappop(A)
    new_lst[i] = minn
  return new_lst

print(heapsort(A))
