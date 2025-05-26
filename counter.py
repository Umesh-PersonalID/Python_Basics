arr = ["lc", "bb", "ac", "dd", "cc" , "aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "ii", "jj", "kk", "ll", "mm"]
arr2 = ["aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "ii", "jj", "kk", "ll", "mm"]
arr3 = ["aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "ii", "jj", "kk", "ll", "mm"]

from collections import Counter


hash_map = Counter(arr)
hash_map2 = Counter(arr2)       
hash_map3 = Counter(arr3)
print(hash_map)
print(hash_map2)
print(hash_map3)



print(hash_map["aa"])
print(hash_map["bb"])