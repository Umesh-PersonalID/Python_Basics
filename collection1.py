# =====================================================================
# Python Tutorial: Advanced Data Structures & Utilities from collections, heapq, bisect, queue, and frozenset
# =====================================================================

# -------------------------------
# 1. collections.deque
# -------------------------------
from collections import deque

# Summary:
# deque is a double-ended queue optimized for O(1) append/pop from both ends

dq = deque([1, 2, 3])
dq.append(4)          # Append to right
dq.appendleft(0)      # Append to left
dq.pop()              # Remove from right (returns 4)
dq.popleft()          # Remove from left (returns 0)
dq.extend([5, 6])     # Extend right
dq.extendleft([-1, -2])  # Extend left (note: elements are added in reverse order)
dq.rotate(1)          # Rotate right by 1
dq.rotate(-1)         # Rotate left by 1

print("Deque:", dq)

# Tip: Use deque instead of list when you frequently append/pop from both ends.


# -------------------------------
# 2. collections.defaultdict
# -------------------------------
from collections import defaultdict

# Summary:
# defaultdict returns a default value when accessing a missing key

dd = defaultdict(int)  # Default value is 0
dd['apple'] += 1
dd['banana'] += 2

# Can use any factory function: list, set, custom lambda, etc.
words_by_length = defaultdict(list)
words_by_length[4].append('word')
words_by_length[3].append('cat')

print("DefaultDict:", dict(dd))
print("Words by length:", dict(words_by_length))

# Tip: Avoid KeyError by automatically initializing new keys.


# -------------------------------
# 3. collections.Counter
# -------------------------------
from collections import Counter

# Summary:
# Counter counts hashable items and returns a dict-like object

c = Counter('banana')
print("Counter:", c)

c.update('apple')  # Adds counts
print("Updated Counter:", c)

print("Most common:", c.most_common(2))  # Top 2 items

# Subtract, arithmetic, set-like operations:
a = Counter('aaabbc')
b = Counter('abc')
print("Subtract:", a - b)  # Only positive counts kept

# Tip: Useful for frequency analysis, word counts, etc.


# -------------------------------
# 4. collections.OrderedDict (Only relevant < Python 3.7)
# -------------------------------
from collections import OrderedDict

# Summary:
# OrderedDict remembers the insertion order of keys (same as dict in Python 3.7+)

od = OrderedDict()
od['first'] = 1
od['second'] = 2
od['third'] = 3

print("OrderedDict:", od)

# Method: move_to_end
od.move_to_end('first')  # Moves key to end
print("Moved key:", od)

# Tip: Only use if you need compatibility with Python < 3.7.


# -------------------------------
# 5. heapq (min-heap priority queue)
# -------------------------------
import heapq

# Summary:
# heapq provides a min-heap implementation using a list

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)

print("Heap:", heap)
print("Min item:", heapq.heappop(heap))  # Returns 1 (smallest)

# Convert existing list to heap
nums = [5, 1, 7, 3]
heapq.heapify(nums)
print("Heapified list:", nums)

# Get n smallest/largest
print("3 smallest:", heapq.nsmallest(3, nums))
print("2 largest:", heapq.nlargest(2, nums))

# Tip: Use tuples (priority, item) for complex sorting.


# -------------------------------
# 6. bisect (Binary search in sorted list)
# -------------------------------
import bisect

# Summary:
# bisect is used to insert/search in a sorted list in O(log n) time

arr = [1, 3, 4, 4, 6, 8]

# bisect_right: insert to the right of duplicates
index = bisect.bisect_right(arr, 4)  # returns 4
bisect.insort_right(arr, 5)

# bisect_left: insert to the left of duplicates
index2 = bisect.bisect_left(arr, 4)  # returns 2
bisect.insort_left(arr, 4)

print("Bisected List:", arr)

# Tip: Use bisect for maintaining sorted lists without sorting every time.


# -------------------------------
# 7. queue.Queue, LifoQueue, PriorityQueue
# -------------------------------
import queue

# Summary:
# Thread-safe queues for multi-threaded applications

# FIFO Queue
q = queue.Queue()
q.put(10)
q.put(20)
print("Queue get:", q.get())  # returns 10

# LIFO Queue (stack)
lq = queue.LifoQueue()
lq.put('a')
lq.put('b')
print("LifoQueue get:", lq.get())  # returns 'b'

# PriorityQueue
pq = queue.PriorityQueue()
pq.put((2, "medium"))
pq.put((1, "high"))
pq.put((3, "low"))
print("PriorityQueue get:", pq.get())  # returns (1, "high")

# Tip: Designed for thread safety, but slower than heapq in single-threaded code.


# -------------------------------
# 8. frozenset
# -------------------------------

# Summary:
# frozenset is an immutable set, can be used as dict keys or set elements

fs = frozenset([1, 2, 3])
print("Frozenset:", fs)

# Can't add/remove elements
# fs.add(4)  # ❌ Will raise AttributeError

# Set operations still work
other = frozenset([2, 3, 4])
print("Union:", fs | other)
print("Intersection:", fs & other)

# Use-case: as keys in a dict or elements in a set
my_dict = {frozenset([1, 2]): "hello"}
print("Dict with frozenset key:", my_dict)

# Tip: Use frozenset for caching, memoization, graph edges, etc.

# =====================================================================
# END OF TUTORIAL
# =====================================================================
