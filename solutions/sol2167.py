import sys

input = sys.stdin.readline


# 2167 2차원 배열의 합
# 단순히 매 질의마다 N * M 반복문을 돌려도 해결 가능한 문제
# 하지만 누적 합의 성질을 이용하면 보다 효율적으로 문제를 해결할 수 있다.
def sol2167():
    # 행렬의 크기 n, m
    n, m = map(int, input().split())

    # 주어진 행렬 seq
    # 누적 합의 성질 4번을 사용할 때, 0번 인덱스의 이전 인덱스를 참조할 경우를 대비해
    # 행/열의 끝에 0을 추가
    seq = [[*map(int, input().split()), 0] for _ in range(n)]
    seq.append([0] * m)
    seq.append([0] * m)

    # 2차원 배열의 누적합 배열을 구한다
    for i in range(n):
        for j in range(m):
            # 현재 위치의 누적합을 구하기 전에 같은 열의 다음 행의 값에
            # 현재위치의 값을 더해주는 것으로 열에 대한 누적합을 동시에 계산해나갈 수 있다.
            seq[i + 1][j] += seq[i][j]
            seq[i][j] += seq[i][j - 1]

    # 정답 리스트
    answer = []

    # 누적 합의 성질 4번을 사용하여 부분 합을 구하고 정답 리스트에 저장
    for _ in range(int(input())):
        i, j, x, y = map(int, input().split())
        answer.append(seq[x - 1][y - 1] + seq[i - 2][j - 2] - seq[x - 1][j - 2] - seq[i - 2][y - 1])

    # 출력 형식에 맞춰 정답 리스트 반환
    return '\n'.join(map(str, answer))
