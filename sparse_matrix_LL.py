class List:
    def __init__(self, ind, val):
        self.ind = ind
        self.val = val
        self.next = None

mat = [[0, 0, 3, 0],
       [0, 5, 0, 0],
       [2, 0, 4, 0],
       [0, 0, 6, 6]]

ll = [None]*len(mat)

for i in range(len(mat)):
    head = None
    tail = None
    for j in range(len(mat[0])):
        if mat[i][j] != 0:
            node = List(j, mat[i][j])
            if head is None:
                head = tail = node
            else:
                tail.next = node
                tail = node
    ll[i] = head 

for i in range(len(mat)):
    print(f"Row {i}:", end=" ")
    curr = ll[i]
    while curr:
        print(f"[{curr.ind},{curr.val}]", end=" -> ")
        curr = curr.next
    print("None")
