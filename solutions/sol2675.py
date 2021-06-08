import sys

input = sys.stdin.readline


# 2675 문자열 반복
# 문자열과 반복횟수를 입력받아 문자열의 각 문자를 반복횟수만큼 반복한 새 문자열을 만들어 출력하는 문제
def sol2675():
    answer = []
    for t in range(int(input())):
        res = []
        r, s = input().split()
        for c in s:
            res.append(c * int(r))
        answer.append(''.join(res))
    print('\n'.join(answer))
