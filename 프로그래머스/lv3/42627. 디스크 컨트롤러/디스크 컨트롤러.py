import heapq
def solution(jobs):
    answer = 0
    # 소요시간 가장 짧은애?
    def sorted_key(arr):
        return arr[1]
    def sorted_key2(arr):
        return arr[0]
    jobs = sorted(jobs,key=sorted_key)
    jobs = sorted(jobs,key=sorted_key2)
    index=0
    time = jobs[index][0]
    end = jobs[index][1] + time
    total = jobs[index][1]
    index+=1
    heap = []
    print(len(jobs))
    while True:
        if len(heap) == 0 and index>=len(jobs):
            break
        tmp = index
        for k in range(tmp ,len(jobs)):
            if index < len(jobs):
                if jobs[index][0] == time:
                    heapq.heappush(heap,(jobs[index][1],jobs[index][0]))
                    index+=1
        if time == end:
            #끝났으니 판단 . 현재 힙에 있는걸로
            if len(heap) > 0:
                a, b = heapq.heappop(heap)
                end = a + time
                total += a
                total += (time-b)
            else:
                if index >= len(jobs):
                    break
                time = jobs[index][0]
                end = jobs[index][1] + time
                total += jobs[index][1]
                index+=1

        time+=1
        
    return (total//len(jobs))

# solution([[0, 3], [1, 9], [2, 6]])
