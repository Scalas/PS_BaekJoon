import sys

input = sys.stdin.readline


# 1244 스위치 켜고 끄기
# 규칙에 따라 스위치를 켜고 끄는 문제
def sol1244():
    n = int(input())
    switch = [0, *map(int, input().split())]
    for _ in range(int(input())):
        s, num = map(int, input().split())
        if s == 1:
            for i in range(num, n+1, num):
                switch[i] = 1-switch[i]
        else:
            switch[num] = 1 - switch[num]
            for i in range(1, min(num, n-num+1)):
                l, r = num-i, num+i
                if switch[l] == switch[r]:
                    switch[l] = 1 - switch[l]
                    switch[r] = 1 - switch[r]
                else:
                    break
    idx = 1
    sl = len(switch)
    answer = []
    while idx <= n:
        line_len = min(20, sl - idx)
        answer.append(' '.join(map(str, switch[idx:idx+line_len])))
        idx += line_len
    return '\n'.join(answer)
