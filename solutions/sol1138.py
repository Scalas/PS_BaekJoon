import sys

input = sys.stdin.read


# 1138 한 줄로 서기
# 1번부터 n번까지의 사람들이 자신보다 번호가 큰 사람이 왼쪽에 몇명있는지 알고있을 때
# 사람들의 순서를 구하는 문제
def sol1138():
    seq = [*map(int, input().split())]
    n = seq[0]
    res = [10] * n
    for i in range(1, n+1):
        cnt = 0
        for j in range(n):
            if res[j] > i:
                cnt += 1
            if cnt > seq[i]:
                res[j] = i
                break

    return ' '.join(map(str, res))
