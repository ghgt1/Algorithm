def solution(array):
    answer = []
    global one
    global zero
    one = 0
    zero = 0
    for k in array:
        for u in k:
            if u == 0:
                zero+=1
            else:
                one+=1
    
#     quad를 네개 호출
    def quad(arr):
        global one
        global zero
        #여기서 네개 나누기
        if len(arr[0]) == 1:
            # 끝이라는 것
            return
        tmp = arr[0][0]
        flag = True
        for u in arr:
            for q in u:
                if q!=tmp:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            if tmp == 0:
                zero -= (len(arr)*len(arr)-1)
            else:
                one -= (len(arr)*len(arr)-1)
            return
        
        width = int(len(arr)/2)
        l1 = [arr[k][:width] for k in range(0,width)]
        l2 = [arr[k][width:] for k in range(0,width)]
        l3 = [arr[k][:width] for k in range(width,len(arr))]
        l4 = [arr[k][width:] for k in range(width,len(arr))]
        
        
        quad(l1)
        quad(l2)
        quad(l3)
        quad(l4)
    
    quad(array)
    answer = [zero,one]
    return answer