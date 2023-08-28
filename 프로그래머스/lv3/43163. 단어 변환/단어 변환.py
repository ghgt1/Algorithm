from collections import deque

def solution(begin, target, words):
    answer = 0
    #visited를 갖고있어야한다. 즉 한번 거쳐온 단어는 다시 못감
    #비교함수를 통해 한가지 글자만 다른지확인해야한다
    visited = {}
    visited[begin] = False
    for k in words:
        visited[k] = False
    
    def comp(a,b):
        count = 0
        for k in range(len(a)):
            if a[k] != b[k]:
                count+=1
        if count == 1:
            return True
        else:
            return False
    
    def bfs(v,visited):
        queue = deque([(v,0)])
        while queue:
            node, count = queue.popleft()
            visited[node] = True
            if node == target:
                return count
            for k in words:
                if comp(k,node) and not visited[k]:
                    queue.append((k,count+1))
    answer = bfs(begin,visited)
    if answer == None:
        return 0
    return answer