import sys

input = sys.stdin.readline


# 5721 사탕 줍기 대회
# n * m 격자공간의 각 칸에 들어있는 사탕의 갯수가 주어지고 한 칸에서 사탕을 가져가면
# 그 칸의 위 아래줄의 사탕과 왼쪽 오른쪽 한칸의 사탕이 모두 사라진다고 할 때
# 가져갈 수 있는 사탕의 최대갯수를 구하는 문제
def sol5721():
    answer = []
    while True:
        n, m = map(int, input().split())

        # 입력 종료
        if n==m==0:
            break

        # 사탕의 배치상태
        candy = [list(map(int, input().split())) for _ in range(n)]

        for i in range(n):
            # 2칸 위쪽 행까지의 최대 사탕갯수 합산
            if i > 1:
                candy[i][0] += candy[i-2][-1]
                if m > 1:
                    candy[i][1] += candy[i-2][-1]

            # 둘째 칸의 사탕을 가져가는 경우와 가져가지 않는 경우 중 최댓값
            if m > 1:
                candy[i][1] = max(candy[i][0], candy[i][1])

            for j in range(2, m):
                # 현재 박스의 사탕을 가져갈 경우와 가져가지 않을 경우중 최댓값
                candy[i][j] = max(candy[i][j-1], candy[i][j-2] + candy[i][j])

            # 위쪽 행에서 사탕을 가져가고 현재 행을 포기했을 때와 비교
            if i > 0:
                for j in range(m):
                    candy[i][j] = max(candy[i][j], candy[i-1][j])

        # 마지막 칸까지 얻을 수 있는 사탕의 최대 갯수
        answer.append(candy[-1][-1])

    return '\n'.join(map(str, answer))
