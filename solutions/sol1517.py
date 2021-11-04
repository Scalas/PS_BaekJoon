import sys

input = sys.stdin.readline


# 1517 버블 소트
# 수열이 주어졌을 때 해당 수열을 버블정렬로 오름차순 정렬하기 위해 일어나는 swap의 횟수를 구하는 문제
# 수열의 크기가 최대 50만이기 때문에 버블정렬을 실제로 수행하면 당연히 시간초과가 발생한다.

# 머지 정렬을 활용한 방법
def sol1517():
    n = int(input())
    seq = list(map(int, input().split()))

    return sort(seq, 0, n)


def sort(seq, left, right):
    cnt = 0
    if right - left > 1:
        mid = (left + right) // 2
        cnt += sort(seq, left, mid)
        cnt += sort(seq, mid, right)
        cnt += merge(seq, left, mid, right)
    return cnt


def merge(seq, left, mid, right):
    i, j = left, mid
    cnt = 0
    tmp = []
    while i < mid and j < right:
        # swap
        # 병합할 두 부분은 이미 정렬된 상태이기 때문에
        # i 번째 수가 j번째 수보다 크다면 i+1 ~ mid-1 번째 수들도 모두 j번째 수보다 크다
        # 그러므로 seq[i] > seq[j] 일 때 일어나는 버블정렬의 swap 횟수는 mid - i 번
        if seq[i] > seq[j]:
            tmp.append(seq[j])
            j += 1
            cnt += (mid-i)
        else:
            tmp.append(seq[i])
            i += 1
    while i < mid:
        tmp.append(seq[i])
        i += 1
    while j < right:
        tmp.append(seq[j])
        j += 1

    seq[left:right] = tmp
    return cnt
