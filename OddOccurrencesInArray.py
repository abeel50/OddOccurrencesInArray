def solution(A):
    set_A = set()
    # iterate through unique array
    for i in A:
            if i not in set_A:
                set_A.add(i)
            else:
                set_A.remove(i)
    return list(set_A)[0]
print(solution([9,9,9,9,1,1,3,3,7,7,7]))