import sys
from bisect import bisect_left

input = sys.stdin.readline


# 12015 최장 증가 수열 (LIS) 문제
# 시간복잡도 O(N^2)의 동적계획법을 활용한 풀이로는 시간초과
# 이분탐색을 사용하여 O(N*logN)으로 해결 가능

# 직접 이분탐색을 구현한 풀이
def sol12015():
    input()
    A = map(int, input().split())
    seq = [next(A)]
    for a in A:
        # A 수열의 숫자들을 순차적으로 참조, seq의 마지막 숫자보다 크다면 append (최장 증가 수열을 연장)
        if (a > seq[-1]):
            seq.append(a)

        # seq 내의 각 숫자가 작을수록 보다 큰 증가수열의 길이를 얻어낼 수 있음
        # append 되지 못한 숫자는 seq 내에서 자신보다 크거나 같은 수 중에 가장 작은 수를 대체
        else:
            s, e = 0, len(seq) - 1
            while (s <= e):
                m = (s + e) // 2
                if (seq[m] >= a):
                    e = m - 1
                else:
                    s = m + 1
            seq[min(e + 1, len(seq) - 1)] = a
    print(len(seq))


# bisect 모듈을 활용한 풀이
# bisect 모듈의 bisect_left, bisect_right 는 수열 내에서 숫자가 삽입될 수 있는 좌측, 우측 인덱스를 반환한다
# 여기서는 a보다 크거나 같은 수 중에 가장 작은 수를 구해야하기 때문에 bisect_left 를 사용한다
# 직접 이분탐색을 구현한 코드와 비교해서 굉장히 빠르다
def sol12015_2():
    n = int(input())
    A = map(int, input().split())
    seq = [next(A)]
    for a in A:
        if (a > seq[-1]):
            seq.append(a)
        else:
            seq[bisect_left(seq, a)] = a
    print(len(seq))
