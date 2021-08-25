import sys

input = sys.stdin.readline


# 2166 다각형의 면적
# 다각형을 이루는 2차원 평면상의 좌표 N개가 주어졌을 때, 다각형의 면적을 구하는 문제.
# 벡터의 외적공식을 활용하면 쉽게 해결 가능한 문제
def sol2166():
    n = int(input())
    # 외적공식을 사용하기 위해 다각형을 이루는 좌표리스트 뒤에 첫 좌표를 덧붙여준다
    pos = [list(map(int, input().split())) for _ in range(n)]
    pos.append(pos[0])

    # 공식에 따라 값을 더한다
    res = 0
    for i in range(n):
        res += (pos[i][0] * pos[i + 1][1] - pos[i + 1][0] * pos[i][1])

    # 값에 절댓값을 취한 뒤 2로 나누어 소수 첫째자리까지 반환
    return '%.1f' % (abs(res) / 2)
