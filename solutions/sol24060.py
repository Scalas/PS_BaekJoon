import sys

input = sys.stdin.readline


# 24060 알고리즘 수업
# 길이 n의 수열을 merge sort 할 때
# k 번째로 본 배열에 저장되는 수를 구하는 문제
# 만약 k 번째 저장되기 전에 정렬이 끝난다면 -1 반환
def sol24060():
    n, k = map(int, input().split())
    seq = list(map(int, input().split()))
    answer = -1

    def merge_sort(s, e):
        nonlocal answer

        if s < e:
            mid = (s + e) // 2
            merge_sort(s, mid)
            if answer > 0:
                return
            merge_sort(mid + 1, e)
            if answer > 0:
                return
            merge(s, mid, e)
            if answer > 0:
                return

    def merge(s, mid, e):
        nonlocal k, answer

        i, j = s, mid + 1
        tmp = []
        while i <= mid and j <= e:
            if seq[i] < seq[j]:
                tmp.append(seq[i])
                i += 1
            else:
                tmp.append(seq[j])
                j += 1

        while i <= mid:
            tmp.append(seq[i])
            i += 1
        while j <= e:
            tmp.append(seq[j])
            j += 1

        for i in range(len(tmp)):
            seq[i + s] = tmp[i]
            k -= 1
            if k == 0:
                answer = tmp[i]

    merge_sort(0, n - 1)
    return answer
