def solution(strings, n):
    answer = []
    strings.sort()
    #어차피 배열 과 같음
    def sort_key(data):
        return data[n]
    strings = sorted(strings,key=sort_key)
    return strings