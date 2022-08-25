import sys

input = sys.stdin.readline


# 21758 꿀 따기
# n개의 장소에서 두 곳에 꿀벌을 놓고 한 곳에 벌통을 놓은 뒤
# 두 벌이 벌통을 향해 이동하며 각 장소에서 얻을 수 있는 만큼의 꿀을 수집할 때
# 얻을 수 있는 꿀의 최댓값을 구하는 문제
# (벌통이 있는 위치에서도 꿀 획득 가능, 같은 칸에서 꿀 두 번 획득 가능 - 두 벌이 한 번씩)
# 단, 두 벌이 시작한 위치에서는 꿀을 얻을 수 없음
def sol21758():
    n = int(input())
    honey = list(map(int, input().split()))
    mid_max = max(honey[1:-1])
    for i in range(n - 1):
        honey[i + 1] += honey[i]

    # 벌통이 중간에 있는 경우
    answer = honey[n - 2] - honey[0] + mid_max

    # 벌통이 양 끝에 있는 경우
    for i in range(1, n - 1):
        right_honey_amount = (honey[i - 1] - honey[0]) + (honey[n - 1] - honey[i]) * 2
        left_honey_amount = (honey[i - 1]) * 2 + (honey[n - 2] - honey[i])
        answer = max(answer, max(left_honey_amount, right_honey_amount))
    return answer
