def solution(new_id):
    answer = ''
    l1 = []
    candidates = []
    for k in range(97,123):
        candidates.append(k)
    for k in range(48,58):
        candidates.append(k)
    candidates.append(ord('-'))
    candidates.append(ord('_'))
    candidates.append(ord('.'))
    #1
    new_id = new_id.lower()
    for k in new_id:
        #2
        if ord(k) in candidates:
            l1.append(k)
    
    id = ''.join(l1)
    
    #3
    while '..' in id:
        id = id.replace('..','.')
    
    l1 = []
    for k in id:
        l1.append(k)
        
    #4
    if len(l1) >0 and l1[0] == '.':
        del l1[0]
    if len(l1) >0 and l1[-1] == '.':
        del l1[-1]
    
    #5
    if len(l1) == 0:
        l1.append('a')
    
    #6
    if len(l1)>=16:
        l1 = l1[:15]
    if l1[-1] == '.':
        del l1[-1]
    
    #7
    while len(l1)<=2:
        l1.append(l1[-1])
        
    answer = ''.join(l1)
    return answer