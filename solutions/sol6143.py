import sys

input = sys.stdin.readline


# 6143 문자열 생성 2
# 문자열 s의 맨앞 또는 맨뒤의 문자를 뽑아 이어붙여서 만들 수 있는 문자열중
# 사전순으로 가장 빠른 문자열을 구하는 문제
def sol6143():
    n = int(input())
    string = ''.join([input().rstrip() for _ in range(n)])

    answer = []
    cnt = 0
    l, r = 0, n-1
    while l < r:
        if string[l] < string[r]:
            answer.append(string[l])
            l += 1
        elif string[l] > string[r]:
            answer.append(string[r])
            r -= 1
        else:
            pl, pr = l, r
            while pl < pr and string[pl] == string[pr]:
                pl += 1
                pr -= 1
            if string[pl] < string[pr]:
                answer.append(string[l])
                l += 1
            else:
                answer.append(string[r])
                r -= 1
        cnt += 1
        if not cnt % 80:
            answer.append('\n')
    if l == r:
        answer.append(string[l])
    return ''.join(answer)
