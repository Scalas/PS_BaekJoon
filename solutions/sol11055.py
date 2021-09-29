import sys

input = sys.stdin.read


# 11055 가장 큰 증가 부분 수열
# LIS 와 유사하지만 길이가 가장 긴 것이 아닌 합이 가장 큰 것을 찾아야한다
def sol11055():
    n, *seq = map(int, input().split())

    # 인덱스 i 까지의 증가 부분 수열 합의 최댓값을 gis[i] 라고 할 때
    gis = [0] * n
    gis[0] = seq[0]

    # gis[i] 는 gis[0] ~ gis[i-1] 중 최댓값에 i 번째 수(seq[i]) 를 더한 것과 같다.
    for i in range(1, n):
        gis[i] = max([gis[j] for j in range(i) if seq[j] < seq[i]], default=0) + seq[i]

    # 각 인덱스까지의 증가 부분 수열 합의 최댓값 중 최댓값을 반환
    return max(gis)
