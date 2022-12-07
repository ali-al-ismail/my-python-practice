# https://www.codewars.com/kata/514b92a657cdc65150000006
# returns sum of all mults of 3 and 5 
def getMults(n):
    return sum([i for i in range(1,n) if i % 3 == 0 or i % 5 == 0])

