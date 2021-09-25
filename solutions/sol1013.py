import sys
import re

input = sys.stdin.readline


# 1013 Contact
# 문자열이 특정 규칙을 만족하는지 확인하는 문제
# 정규표현식을 사용하면 간단하게 해결 가능한 문제이다.
def sol1013():
    answer = []
    pattern = re.compile('(100+1+|01)+')
    for _ in range(int(input())):
        s = input().rstrip()
        if pattern.fullmatch(s):
            answer.append('YES')
        else:
            answer.append('NO')

    return '\n'.join(answer)
