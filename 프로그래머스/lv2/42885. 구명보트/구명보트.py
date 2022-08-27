from collections import deque
import bisect
def solution(people, limit):
    people.sort()
    people = deque(people)
    answer = 0
    while True:
        if len(people) == 0:
            break
        elif len(people) == 1:
            answer = answer + 1
            break
        if people[0] + people[-1] > limit:
            answer = answer + 1
            people.pop()
        else:
            answer = answer + 1
            people.pop()
            people.popleft()
    return answer