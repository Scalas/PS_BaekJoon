import sys

input = sys.stdin.readline


# 1568 새
# 1번부터 n번 까지의 새가 k=1부터 시작하여 1초마다 한번씩 오름차순으로 노래를 부르며
# k번 노래를 부를 때마다 k 마리의 새가 날아가며 노래의 번호가 남아있는 새보다 많을 경우
# 1번 노래부터 다시시작할 때, 모든 새가 날아가는데 걸리는 시간을 구하는 문제
def sol1568():
    answer = 0
    k = 1
    bird = int(input())
    while bird:
        if bird < k:
            k = 1
        answer += 1
        bird -= k
        k += 1
    return answer
