from sys import stdin, stdout


# 1654 랜선 자르기
# k개의 선을 같은 길이의 선 n개 이상으로 자를 때 잘린 선의 길이의 최댓값을 구하는 문제
# 잘린 선의 최소길이 1에서 k개의 선을 모두 합쳐 n으로 나눈 값(버리는 선이 없는 최적의 경우) 사이에서
# 조건에 맞는 선의 길이 m을 분할정복으로 탐색, 조건에 맞을경우 그보다 큰쪽의 범위에서 재탐색을 반복하여
# 조건을 만족하는 가장 큰 m을 찾을 수 있다
def sol1654():
    k, n, *lans = map(int, input().split())

    s, e = 1, sum(lans) // n
    while s <= e:
        m = (s + e) // 2
        if sum([lan // m for lan in lans]) < n:
            e = m - 1
        else:
            s = m + 1
    return s - 1
