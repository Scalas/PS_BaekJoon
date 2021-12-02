import sys

input = sys.stdin.readline


# 2947 나무 조각
# 버블 정렬의 과정을 출력하는 문제
def sol2947():
    sorted_seq = [1, 2, 3, 4, 5]
    seq = list(map(int, input().split()))
    answer = []
    while seq != sorted_seq:
        for i in range(4):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                answer.append(' '.join(map(str, seq)))
    return '\n'.join(answer)
