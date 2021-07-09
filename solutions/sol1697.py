import sys

input = sys.stdin.readline
n, k = map(int, input().split())


# 1697 숨바꼭질
# bfs로 간단히 풀 수 있는 문제
def sol1697():
    if n >= k:
        return n - k
    else:
        visit = [0] * 100001
        q = [n]
        answer = 0
        while q:
            nq = []
            for p in q:
                if p == k:
                    return answer
                if p - 1 >= 0 and not visit[p - 1]:
                    nq.append(p - 1)
                    visit[p - 1] = 1
                if p + 1 <= 100000 and not visit[p + 1]:
                    nq.append(p + 1)
                    visit[p + 1] = 1
                if p * 2 <= 100000 and not visit[p * 2]:
                    nq.append(p * 2)
                    visit[p * 2] = 1
            answer += 1
            q = nq
        return -1
