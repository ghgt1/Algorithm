def solution(players, callings):
    answer = []
    dic = {}
    for k in range(len(players)):
        dic[players[k]] = k
    for k in callings:
        tmp = players[dic[k]-1]
        players[dic[k]-1] ,players[dic[k]] = players[dic[k]], players[dic[k]-1]
        dic[k]-=1
        dic[tmp]+=1
    return players