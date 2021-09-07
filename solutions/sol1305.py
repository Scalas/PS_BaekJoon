import sys

input = sys.stdin.readline


# 1305 광고
# 길이 L의 전광판에 길이 N의 광고문구를 무한히 이어붙인 문자열이 표시될 때,
# 광고문구가 될수있는는가장 짧은 문자열의 길이를 구하는 문제.
def sol1305():
    # 전광판의 크기
    L = int(input())

    # 전광판에 표시된 문자열
    adv = input().rstrip()

    # LPS 테이블 전처리
    lps = [0] * L
    i = 0
    for j in range(1, L):
        while i > 0 and adv[i] != adv[j]:
            i = lps[i - 1]
        if adv[i] == adv[j]:
            i += 1
            lps[j] = i

    # L - len(lps) 반환
    return L - lps[-1]
