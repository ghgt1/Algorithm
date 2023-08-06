def solution(num):
    global answer
    answer = 0
    def collatz(data):
        global answer
        if data == 1:
            return
        if answer>500:
            answer = -1
            return
        answer+=1
        if data%2==0:
            collatz(data/2)
        else:
            collatz(data*3+1)
    collatz(num)
    return answer