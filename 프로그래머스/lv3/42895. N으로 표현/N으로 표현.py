def solution(n, number):
    #어쨋든 dp다.
    #부분문제로 쪼개보자
    #n을 두번썻을때는 n을 한번썻을때의 결과에 사칙연산이 더해지는거임
    #즉 이거는 바텀업 방식으로 올라가면된다
    #큰실수
    #예를들어 55+55는 4지만 3에서 갈수가없음. 따라서 n번째는 n-1뿐만아니라 그이전의 모든 경우를 다봐야함
    answer = -1
    count = 1
    dic = {}
    dic[1] = [n]
    dic[2] = [n*2,0,1,11*n,n*n]
    if number in dic[1]:
        return 1
    if number in dic[2]:
        return 2
    for k in range(3,9):
        tmp = [int('1'*k)*n]
        for u in range(1,k):
            for q in dic[k-u]:
                for p in dic[u]:
                    tmp.append(q+p)
                    tmp.append(q-p)
                    tmp.append(p-q)
                    tmp.append(q*p)
                    if p!=0:
                        tmp.append(q//p)
                    if q!=0:
                        tmp.append(p//q)
        dic[k] = list(set(tmp))
        if number in tmp:
            return k
                        
    return answer