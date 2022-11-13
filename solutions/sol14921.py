import sys

input = sys.stdin.readline


# 14921 용액 합성하기
# n개의 용액의 특성값이 오름차순으로 주어졌을 때
# 두 용액의 특성값을 합쳐 만들 수 있는 0에 가장 가까운 값을 구하는 문제
def sol14921():
    n = int(input())
    lq = list(map(int, input().split()))

    # 합칠 두 용액을 양쪽 끝에서 탐색하기 시작
    # 왼쪽 용액은 오른쪽으로 갈수록 합이 커지고 오른쪽 용액은 왼쪽으로 갈수록 합이 작아진다.
    # 양 끝의 용액의 합이 0보다 크면 오른쪽 용액을 왼쪽으로, 0보다 작으면 왼쪽 용액을 오른쪽으로 한칸 이동
    # 매 순간 두 용액의 특성값의 합의 절댓값이 기존 0에 가장 가까운 값(answer)보다 작다면 값을 갱신
    s, e = 0, n - 1
    answer = lq[e] + lq[s]
    while s < e:
        k = lq[e] + lq[s]
        if abs(k) < abs(answer):
            answer = k
        if k > 0:
            e -= 1
        elif k < 0:
            s += 1
        else:
            return 0

    return answer
