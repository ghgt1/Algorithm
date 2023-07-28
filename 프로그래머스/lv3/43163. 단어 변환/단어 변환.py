from collections import deque

def solution(begin, target, words):
    answer = 0
#     한번 방문하면 무조건 visited False
#     쭉 나가면서 하나바꿀때 되는것들 전부 queue에 넣기

    def cal(tmp):
        candidates = []
        for k in words:
            tmp_count = 0
            for u in range(len(k)):
                if tmp[u] != k[u]:
                    tmp_count+=1
            if tmp_count == 1:
                if visited[k]:
                    candidates.append(k)
        return candidates
    
    def bfs():
        queue = deque([(begin,0)])
        while queue:
            word,count = queue.pop()
            visited[word] = False
            if word == target:
                return count
            candidates = cal(word)
            for k in candidates:
                queue.append((k,count+1))
        return 0
        
            
            
            
    visited = {}
    for k in words:
        visited[k] = True
    
    answer = bfs()
    
    return answer