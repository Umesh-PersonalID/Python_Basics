from collections import Counter
import collections
class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        cache = dict(Counter(s))
        ram = collections.defaultdict(list)
        ans = 0
        count = 0
        for i,j in cache.items():
            ram[j].append(i)

        cache = dict(ram)
        cache =  dict(sorted(cache.items(),reverse = True))
        
        cache =  dict(sorted(cache.items(),reverse = True, key = lambda item : len(item[1])))
        res = next(iter(cache))
        return "".join(cache[res])
    
    
