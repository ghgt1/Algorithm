def solution(today, terms, privacies):
    answer = []
    dic = {}
    for k in terms:
        l1 = k.split(' ')
        dic[l1[0]] = int(l1[1])
    #달은 더하고, 일은 -1하면됨
    year, month, day = today.split('.')
    year, month, day = int(year), int(month), int(day)
    count = 0
    for k in privacies:
        count+=1
        l1 = k.split(' ')
        term = dic[l1[1]]
        privacy_year, privacy_month, privacy_day = l1[0].split('.')
        tmp_year, tmp_month, tmp_day = int(privacy_year), int(privacy_month), int(privacy_day)
        tmp_month += term
        tmp_day -= 1
        if tmp_day == 0:
            tmp_month -=1
            tmp_day = 28
        while tmp_month > 12:
            tmp_month -=12
            tmp_year+=1
        # print(tmp_year,tmp_month,tmp_day)
        if tmp_year < year:
            answer.append(count)
        elif tmp_year == year:
            if tmp_month < month:
                answer.append(count)
            elif tmp_month == month:
                if tmp_day < day:
                    answer.append(count)
    return answer