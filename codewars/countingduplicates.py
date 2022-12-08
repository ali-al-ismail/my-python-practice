# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
# last test case incorrectly states that the output should be 16 rather than 8


def countDuplicates(str):
    lst = [i for i in str.upper() if str.upper().count(i) > 1]
    return sum([1 for i in set(lst)])