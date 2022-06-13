def solution(A):
    # if array has single element 
    if len(A) == 1 or len(A) == A.count(A[0]):
        return A[0]
    new_A = list(set(A))

    # iterate through unique array
    for i in new_A:
            if A.count(i) % 2 != 0:
                return i
print(solution([9,9,9,9,1,1,3,3,7,7,7]))