import sys

input = sys.stdin.readline


# 2143 두 배열의 합
# 배열 A 와 B의 연속 부분배열의 합을 서로 더해서 T가 되게하는 경우의 수를 구하는 문제
def sol2143():
    # 두 부분배열의 합으로 만들려는 수 T
    t = int(input())

    # 배열 A
    n = int(input())
    seqa = [0, *map(int, input().split())]

    # 배열 B
    m = int(input())
    seqb = [0, *map(int, input().split())]

    # 배열 A
    for i in range(n):
        seqa[i + 1] += seqa[i]
    for i in range(m):
        seqb[i + 1] += seqb[i]

    # 배열 A의 모든 부분합과 그 갯수를 헤아린다
    asum = {}
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += seqa[j]
            asum[s] = asum.get(s, 0) + 1

    # 배열 B의 부분합이 s일 때 배열 A의 부분합이 t-s 인 경우의 수를 answer 에 더해준다
    answer = 0
    for i in range(m):
        s = 0
        for j in range(i, m):
            s += seqb[j]
            answer += asum.get(t - s, 0)

    # 배열 A와 B의 부분배열의 합이 T인 모든 경우의 수 반환
    return answer
