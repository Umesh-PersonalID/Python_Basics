arr = [6,3,8,10,16,7,5,2,9,14]

Hasharr = [0]*(max(arr)+1)

key = 10

for i in arr:
    if(key-i > 0 and Hasharr[key - i] == 1):
        print("Pair found: ", i, key - i)
    Hasharr[i] = 1
    
    
    
#Find sum in sorted array
#Two pointers

arr = [2,3,5,6,7,8,9,10,14,16]
l = 0
r = len(arr) - 1
while l < r:
    if arr[l] + arr[r] == key:
        print("Pair found in sorted array: ", arr[l], arr[r])
        break
    elif arr[l] + arr[r] < key:
        l += 1
    else:
        r -= 1
