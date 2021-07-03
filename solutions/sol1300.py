import sys

input = sys.stdin.read


# 1300 K번째 수
# a[i][j] = i*j인 n*n 배열 a 의 요소를 오름차순 정렬했을때 k번째 수를 구하는 문제
# 수의 범위 [1, n^2] 에서 이분탐색을 통해 임의의 수 m에 대해
# m보다 작거나 같은 수의 갯수를 구하여 그 수가 k보다 작다면 오른쪽구간으로
# k보다 크다면 왼쪽구간으로 좁혀가며 이분탐색을 진행하여 풀 수 있다
# 배열의 i번째 행의 요소는 i의 배수로 이루어져있기 때문에
# i열의 수 중에서 m보다 작거나 같은 수는 m 이하의 i의 배수의 갯수, 즉 m//i 가 된다
# 다만 i열의 수 중 m보다 작거나 같은 수는 아무리 많아도 n개 이기때문에 (n*n 배열이므로)
# i열 에서 m보다 작거나 같은 수의 갯수는 min(n, m//i) 가 된다

# 임의의 m을 뽑는 횟수가 O(logN), 그때마다 n개의 열에 대해 m보다 작은 수의 갯수를 구하는데 O(N) 이므로
# 이 알고리즘의 시간복잡도는 O(N*logN) 이 된다
def sol1300():
    n, k = map(int, input().splitlines())
    s, e = 1, n ** 2
    while (s <= e):
        m = (s + e) // 2
        cnt = 0
        for i in range(1, n + 1):
            cnt += min(n, m // i)
        if (cnt < k):
            s = m + 1
        else:
            e = m - 1
    print(e + 1)
