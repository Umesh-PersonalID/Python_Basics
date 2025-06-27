dic = {1 : 3, 2: 2, 3:10}
list1 = [[1,3],[10,2],[3,10]]

list1.sort()
print(list1)

dic = (sorted(dic.items(), key = lambda x : x[1]))
list1 = sorted(list1, key=lambda x : x[1])
print(dic)
print(list1)