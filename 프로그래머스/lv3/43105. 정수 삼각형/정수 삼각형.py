def solution(triangle):
    answer = 0
#     거꾸로가면됨
    triangle.reverse()
    for k in range(len(triangle)):
        for u in range(len(triangle[k])-1):
            triangle[k+1][u] += max(triangle[k][u], triangle[k][u+1])
    answer = max(triangle[-1])
    return answer