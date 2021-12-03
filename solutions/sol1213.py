import sys

input = sys.stdin.readline


# 1213 팰린드롬 만들기
# 주어진 문자열을 사전으로 가장 앞서는 팰린드롬으로 만드는 문제
def sol1213():
    name = input().rstrip()
    count = [0] * 26
    aidx = ord('A')

    for c in name:
        count[ord(c) - aidx] += 1

    # 홀수번 등장한 알파벳을 탐색
    # 홀수번 등장한 알파벳이 두 개 이상이면 팰린드롬으로 나타낼 수 없음
    odd = 0
    odd_alpha = ''
    for i in range(26):
        if count[i] % 2:
            odd +=1
            odd_alpha = chr(i+aidx)
            if odd > 1:
                return "I'm Sorry Hansoo"

    # 팰린드롬의 앞쪽 절반을 생성
    # 알파벳 순으로(사전순으로) 등장 횟수의 절반만큼 이어붙여나간다.
    half = ''
    for i in range(26):
        if count[i]:
            half += (chr(i+aidx) * (count[i] // 2))

    # 홀수번 등장한 알파벳을 사이에 두고 half 와 half 를 뒤집은 문자열을 이어붙여 반환
    return half + odd_alpha + half[::-1]
