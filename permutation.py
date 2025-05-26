ls = [1,2,3]

ans = []
ds = []
used = [0]*len(ls)



def permute(ls, ds, ans, used):
    if len(ds) == len(ls):
        ans.append(ds.copy()) #make sure we are doing copy here
        return 

    for i in range(len(used)):
        if used[i] == 0:
            used[i] = 1
            ds.append(ls[i])
            print(f"Current ds: {ds}, used: {used}")
            permute(ls, ds, ans, used)
            ds.pop()
            used[i] = 0
    return


permute(ls, ds, ans, used)
print(ans)