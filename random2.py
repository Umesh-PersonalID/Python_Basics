import random
#sudo random number

a = random.randint(0,10) # a and b both included
print(a)

print(random.randrange(2,6)) # b is not included
print(random.random()) #return floating point number but 0,0 to 1.0


print(random.uniform(3,7)) # float in range

list = [1,2,3,4,'apple',True,6.5]
print(random.choice(list))

random.shuffle(list)

print(list)


print(random.getrandbits(4)) # k is bits # return integer value from 0000 to 1111 bits