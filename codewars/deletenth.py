def deleteNth(lst,n):
    for i,j in enumerate(lst):
        for k in range(len(lst)):
            if lst.count(j) > n:
                lst.pop(max(idx for idx,elm in enumerate(lst) if elm == j))
    return lst




print(deleteNth([1,1,3,3,7,2,2,2,2], 3))