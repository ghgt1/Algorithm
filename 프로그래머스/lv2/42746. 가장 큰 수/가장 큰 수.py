def solution(numbers):
    answer = ''
    l1 = []
    for k in numbers:
        l1.append([k,int((str(k)*4)[0:4])])
    def sort(data):
        return data[1]
    
    l1 = sorted(l1,key=sort)
    l1.reverse()
    for k in l1:
        answer+=str(k[0])
    answer = str(int(answer))
    return answer