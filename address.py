import math
#when the variable have same data, they both will point to same box
#More memory efficient
a = 10
b = a
a = 5

print(b)
print(a)
print(id(a))
print(id(b))
print(id(10))
print(id(11))

#If we not using data it will be assign to garbage collector and it will be removed later

PI = math.pi
print(PI)

print(type(PI)) #Inbuild datatype = INT,FLOAT,STR 