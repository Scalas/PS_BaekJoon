import sys

input = sys.stdin.readline


# 2208 보석 줍기
# n개의 보석의 가치가 주어지고 보석을 줍기 시작하면 연속으로 m개 이상 주워야하며
# 보석을 줍는 것을 멈추는 순간 더이상 보석을 주을 수 없다고 할 때
# 주을 수 있는 보석의 가치의 합의 최댓값을 구하는 문제
def sol2208():
    n, m = map(int, input().split())

    # 보석의 가치의 누적합
    jewel = [int(input()) for _ in range(n)]
    for i in range(n - 1):
        jewel[i+1] += jewel[i]
    jewel.append(0)

    # 길이가 m 이상인 첫 번째 구간 (0, m - 1) 에서 시작
    s, e = 0, m - 1
    answer = max(jewel[e] - jewel[s - 1], 0)
    while e < n - 1:
        # 구간의 끝 1 증가
        e += 1

        # 구간을 그대로 유지하는 것과 구간의 끝이 e이고 길이가 m인
        # 최소구간으로 다시 시작하는 것중 합이 더 커지는 쪽을 선택
        appended = jewel[e] - jewel[s - 1]
        created = jewel[e] - jewel[e - m]
        if created > appended:
            s = e - m + 1

        # 가치 합의 최댓값을 갱신
        answer = max(answer, jewel[e] - jewel[s - 1])

    return answer
