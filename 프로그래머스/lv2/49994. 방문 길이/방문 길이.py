def solution(dirs):
    answer = 0
    graph = [[0 for i in range(11)] for _ in range(11)]
    record = []
    x = 5
    y = 5
    for k in dirs:
        if k == 'U':
            if x==10:
                continue
            record.append(f'{x}+{y}+{x+1}+{y}')
            record.append(f'{x+1}+{y}+{x}+{y}')
            x+=1
        elif k == 'D':
            if x==0:
                continue
            record.append(f'{x}+{y}+{x-1}+{y}')
            record.append(f'{x-1}+{y}+{x}+{y}')
            x-=1
        elif k == 'R':
            if y==10:
                continue
            record.append(f'{x}+{y}+{x}+{y+1}')
            record.append(f'{x}+{y+1}+{x}+{y}')
            y+=1
        elif k == 'L':
            if y == 0:
                continue
            record.append(f'{x}+{y}+{x}+{y-1}')
            record.append(f'{x}+{y-1}+{x}+{y}')
            y-=1
    record = list(set(record))
    answer = len(record)/2
    return answer