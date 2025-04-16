from queue import PriorityQueue


for i in range(4):
    for j in range(4):
        print("# ",end=" ")
    print("\n")

for i in range(4):
    for j in range(4-i):
        print("# ",end="")
    print("\n")
    
for i in range(5):
    for j in range(5-i):
        print(j+1,end="")
    print("\n")


for i in range(5):
    for j in range(5 - i):
        print(" ", end="")
    for j in range(2*i + 1):
        print("*",end="")
    for j in range(5 - i):
        print(" ",end="")
    print("\n")
    
for i in range(1,6):
    for j in range(i):
        print(" ", end="")
    for j in range(2*(6-i-1) + 1):
        print("*",end="")
    for j in range(i):
        print("",end="")
    print("\n")
    
    
for i in range(10):
    star = i
    if(i > 5):
        star = 10-i
    for p in range(star):
        print("*",end=" ")
    print("\n")
    


for i in range(1, 6):
    if (i) & 1:
        start = True
    else:
        start = False
    for j in range(i):
        print(int(start), end=" ")
        start = not start
    print(end="\n")
    
    
for i in range(4):
    for j in range(i+1 ):
        print(j+1,end=" ")
    for j in range(8 - 2*(i + 1)):
        print(" ",end=" ")
    for j in range(i,-1,-1):
        print(j+1,end=" ")
    print("\n")
        
    
count = 1
        
for i in range(5):
    for j in range(i+1):
        print(count, end=" ")
        count += 1
    print("\n")
  
  
for i in range(6):
    count2 = 65   
    for j in range(i):
        print(chr(count2),end=" ")
        count2 += 1
    print("\n")
    
    
N = int(input("Give me layer number : "))

for i in range(2*N - 1):
    if i >= N:
        i = 2*N-2- i
    count  = (2*N - 1) - 2*(i)
    raw = N
    for j in range(i):
        print(raw,end=" ")
        raw -= 1
    for j in range(count):
        print(N - i,end=" ")
    raw+=1
    for j in range(i):
        print(raw,end=" ")
        raw += 1
    print(end="\n")