import sys

input = sys.stdin.readline


# 12969 ABC
# A, B, C를 이어붙여 만들 수 있는 길이 n의 문자열 s중
# 0 <= i < j < n and s[i] < s[j] 를 만족하는 i, j 쌍이 k 개인 문자열 하나를 구하는 문제
def sol12969():
    n, k = map(int, input().split())
    # A의 갯수, B의 갯수, i, j 쌍의 갯수가 같다면 같은 상태로 간주
    visited = [[[False] * (k + 1) for _ in range(n + 1)] for _ in range(n + 1)]

    def dfs(a, b, cnt, s):
        # 문자열의 길이가 n일 때 i, j 쌍의 갯수가 k개라면 문자열 반환
        # k개가 아니라면 -1 반환
        if len(s) == n:
            return ''.join(s) if cnt == k else -1

        # i, j 쌍의 갯수가 k개를 넘어버렸을 경우 -1 반환
        if cnt > k:
            return -1

        # 이미 방문한 케이스라면 -1 반환
        if visited[a][b][cnt]:
            return -1

        # 방문처리
        visited[a][b][cnt] = True

        # A를 넣을 경우
        s.append('A')
        res = dfs(a + 1, b, cnt, s)
        if res != -1:
            return res
        s.pop()

        # B를 넣을 경우
        s.append('B')
        res = dfs(a, b + 1, cnt + a, s)
        if res != -1:
            return res
        s.pop()

        # C를 넣을 경우
        s.append('C')
        res = dfs(a, b, cnt + a + b, s)
        if res != -1:
            return res
        s.pop()

        # 무엇을 넣어도 조건을 만족할 수 없다면 -1 반환
        return - 1

    return dfs(0, 0, 0, [])
