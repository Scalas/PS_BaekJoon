import sys

input = sys.stdin.readline


# 2283 구간 자르기
# 0에서 100만 사이의 좌표 두개로 이루어진 구간이 n개 주어지고
# 특정 구간 a, b(a < b) 를 정하여 주어진 n개의 구간들에서
# a와 b를 벗어나는 부분을 잘라내고 남은 길이를 더해 k가 되도록 할 때
# 이를 만족하는 a, b 쌍을 구하는 문제
# 단, 여러개 존재할 경우 a가 가장 작은 좌표쌍을, a가 같다면 b가 가장 작은 좌표쌍을 구한다
def sol2283():
    n, k = map(int, input().split())

    # 누적합을 사용하여 각 좌표별 구간의 갯수를 구함
    line = [0] * 1000001
    for _ in range(n):
        u, v = map(int, input().split())
        line[u] += 1
        line[v] -= 1
    for i in range(1000000):
        line[i + 1] += line[i]

    # 시작구간, 끝구간을 움직이며 합이 k가되는 구간을 탐색
    # 탐색 순서가 s, e를 오름차순 정렬한 순서와 같기 때문에
    # 가장 먼저 찾은 구간이 조건에 맞는 답이 됨
    s, e = 0, 0
    total = 0
    check = False
    while e < 1000001:
        total += line[e]
        e += 1
        while total > k:
            total -= line[s]
            s += 1
        if total == k:
            check = True
            break

    # 만약 check 가 False일 경우 합이 k가되는 구간을 찾지 못한 것이므로 0 0 반환
    # True일 경우 s e 를 반환
    return ' '.join(map(str, [s, e])) if check else '0 0'
