
def solution(numbers, target):
    answer = 0
#     가지치기 해도 되고
#     아니면 그냥 모든 경우의 수 구해도 됨
# 같은말이지;
# 이건 한 가지 쭉 내려가야하니. DFS
    tmp = [0]
    for k in numbers:
        tmp2 = []
        for q in tmp:
            tmp2.append(q+k)
            tmp2.append(q-k)
        tmp = tmp2
    return tmp.count(target)