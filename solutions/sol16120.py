import sys

input = sys.stdin.readline


# 16120 PPAP
# PPAP 문자열 내의 P를 PPAP로 변경하여 만들 수 있는 문자열은 PPAP 문자열이라 하고
# P는 PPAP 문자열이라고 할 때, 주어진 문자열이 PPAP 문자열인지 구하는 문제
def sol16120():
    s = input().rstrip()
    # 스택의 최상위 네문자가 PPAP가 될때마다 P로 변경하여 모든 문자를 압축했을 때 P가 된다면 PPAP 문자열
    ppap = []
    for c in s:
        if len(ppap) >= 3:
            if ppap[-3] == ppap[-2] == c == 'P' and ppap[-1] == 'A':
                ppap.pop()
                ppap.pop()
                continue
        ppap.append(c)

    return 'PPAP' if ppap == ['P'] else 'NP'
