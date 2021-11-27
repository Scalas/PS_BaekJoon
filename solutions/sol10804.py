import sys

input = sys.stdin.readline


# 10804 카드 역배치
# 1~20의 카드가 순서대로 배치된 상태에서 주어진 구간의 카드의
# 순서를 뒤집는 연산을 10번 반복한 결과를 구하는 문제
def sol10804():
    answer = list(range(21))
    for _ in range(10):
        u, v = map(int, input().split())
        answer[u:v+1] = answer[v:u-1:-1]
    return ' '.join(map(str, answer[1:]))
