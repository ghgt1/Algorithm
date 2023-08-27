import math
def solution(n, k):
    answer = []
    l1 = [i for i in range(1,n+1)]
    #공식으로 풀어야함
    count = math.factorial(n)
    
    #첫번째 자릿수부터 알아야함
    #k가 5임. 하나의 자릿수는 count/n만큼임. 그러면 k/2로 앞자리 판단. 앞자리는 math.ceil(k/2)임.
    #앞자리를 구했으면 고정하고. 나머지 1에대해서 계산해야함. 다시 시작하는거임.나머지 1이라는 것은 n-1자릿수에 대해서 k가 2라는거임
    rear = k
    for i in range(n,0,-1):
        count = count / i
        front = math.ceil(rear/count)
        answer.append(l1[front-1])
        l1.remove(l1[front-1])
        rear = rear%count
        # print(front,rear,count)
        # print(l1)
        
    return answer