import sys

input = sys.stdin.readline


# 9465 스티커
# 2 * n 스티커 하나를 떼면 상하좌우의 스티커가 못쓰게된다고 할 때
# 스티커를 더이상 뗄 수 없을 때 까지 모두 뗐을 때 스티커의 점수의 합의 최대값을 구하는 문제
def sol9465():
    answer = []
    for t in range(int(input())):
        # 스티커의 열 수
        n = int(input())

        # 각 스티커의 점수
        stickers = [list(map(int, input().split())) for _ in range(2)]

        # 마지막으로 뗀 스티커가 0번째 행의 스티커일 때, 1번째 행의 스티커일 때, 떼지 않았을 때
        score = [stickers[0][0], stickers[1][0], 0]

        # 각 열에서의 선택에 따른 점수의 최댓값을 갱신
        for i in range(1, n):
            score = [max(score[1], score[2]) + stickers[0][i], max(score[0], score[2]) + stickers[1][i], max(score)]

        # 점수의 최댓값을 정답 리스트에 삽입
        answer.append(max(score))

    # 출력 형식에 맞춰 정답 리스트 반환
    return '\n'.join(map(str, answer))
