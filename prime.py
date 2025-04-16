num = 37

for i in range(1,num+1):
    if(num % i == 0 and i != 1 and i!=num):
        print("this is not prime number")
        print(i)
        break
    if(i == num):
        print("This is a prime number")



#more efficient way

import math

num = 37

if num <= 1:
    print("Not a prime number")
else:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            print("This is not a prime number")
            print(f"Divisible by: {i}")
            break
    else:
        print("This is a prime number")
