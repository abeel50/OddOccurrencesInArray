from multiprocessing.spawn import _main
from pip import main


def solution(A):
    # if array has single element 
    if len(A) == 1 or len(A) == A.count(A[0]):
        return A[0]
    count_dict = {}
    # iterate through array
    for i in A:
        if A.count(i) == 1:
            return i
        else:
            if i not in count_dict.keys():
                count_dict[i] = A.count(i)
    for (k,v) in count_dict.items():
        if v % 2 !=0:
            return k
  