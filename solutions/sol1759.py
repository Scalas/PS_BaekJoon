import sys
from itertools import combinations

input = sys.stdin.readline


# 1759 암호 만들기
# 주어진 알파벳으로 알파벳 순으로 증가하는 형태의 문자열 암호를 만든다
# 암호에는 최소 하나의 모음과 두개의 자음이 사용된다
# 만들수있는 모든 암호를 사전순으로 출력하는문제
def sol1759():
    l, c = map(int, input().split())
    aiueo = {'a', 'i', 'u', 'e', 'o'}

    # 알파벳들을 오름차순으로 정렬
    chars = input().split()
    chars.sort()

    answer = []

    # 알파벳 목록에서 l개를 고르는 모든 경우의 수
    for case in combinations(chars, l):
        # 모음과 자음의 갯수를 센다
        u, v = 0, 0
        for c in case:
            if c in aiueo:
                u += 1
            else:
                v += 1
        # 모음과 자음의 갯수가 조건에 맞는다면 정답리스트에 append
        # 그렇지 않다면 버린다
        if u >= 1 and v >= 2:
            answer.append(''.join(case))

    # 출력형식에 맞춰 정답리스트 반환
    return '\n'.join(answer)
