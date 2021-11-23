import sys

input = sys.stdin.readline


# 3460 이진수
# 자연수 n을 이진수로 표기했을 때 1의 위치를 모두 구하는 문제
def sol3460():
    answer = []
    for _ in range(int(input())):
        n = int(input())
        res = []
        idx = 0
        while n:
            if n % 2:
                res.append(idx)
            n //= 2
            idx += 1
        answer.append(' '.join(map(str, res)))
    return '\n'.join(answer)
