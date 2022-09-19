import sys

input = sys.stdin.readline


# 21557 불꽃놀이
# n 개의 불꽃놀이 더미가 나란히 놓여져있고 더미가 터지면 양쪽의 인접한 더미의 높이가 1 줄어든다.
# 양 끝을 제외한 더미를 모두 터트려 남은 양 끝 두 더미 중 높이가 큰 쪽의 높이의 최솟값을 구하는 문제
def sol21557():
    n = int(input())
    seq = list(map(int, input().split()))

    # 양 끝 더미중 작은쪽, 큰쪽을 구함
    min_val, max_val = seq[0], seq[-1]
    if min_val > max_val:
        min_val, max_val = max_val, min_val

    # 두 더미의 차
    diff = max_val - min_val

    # 두 더미의 차가 n - 2 이상이라면 큰쪽을 n - 2 번 감소시킨 값이 높은 쪽의 최솟값이 된다.
    if diff >= n - 2:
        return max_val - n + 2

    # 그렇지 않다면 양 끝을 최대한 균등하게 깍아내야 최솟값을 얻을 수 있다.
    # 이 때, 마지막 1개는 양 끝이 모두 1씩 줄어든다는 점에 주의해야한다.
    remain = n - 2 - diff
    return min_val - ((remain - 1) // 2) - 1
