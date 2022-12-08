# https://www.codewars.com/kata/554ca54ffa7d91b236000023/

# delete element if count of specific element exceeds n
# strange solution but it works
def deleteNth(lst,n):
    for i,j in enumerate(lst):
        for k in range(len(lst)):
            if lst.count(j) > n:
                lst.pop(max(idx for idx,elm in enumerate(lst) if elm == j))
    return lst


