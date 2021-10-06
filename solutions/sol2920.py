import sys

input = sys.stdin.readline


# 2920 음계
# 1-8 사이의 수로 이뤄진 길이 8의 수열이 주어졌을 때
# 수열이 오름차순인지 내림차순인지 둘다 아닌지 구하는 문제
def sol2920():
    seq = list(map(int, input().split()))
    cnt = 0
    for i in range(1, len(seq)):
        if seq[i] > seq[i-1]:
            cnt += 1
        else:
            cnt -= 1
    if cnt == len(seq)-1:
        return "ascending"
    if cnt == 1-len(seq):
        return "descending"
    return "mixed"
