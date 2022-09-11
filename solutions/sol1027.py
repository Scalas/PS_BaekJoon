import sys

input = sys.stdin.readline


# 1027 고층 건물
# n개의 건물의 높이가 순서대로 주어지고 각 건물간의 거리는 인덱스의 차만큼 난다.
# 건물 i에서 다른 건물 j를 볼 수 있으려면 건물 i, j의 꼭대기끼리 직선을 이었을 때 사이의 다른 건물이 직선과 만나지 않아야 한다
# 임의의 건물의 꼭대기에서 볼 수 있는 건물의 수의 최댓값을 구하는 문제
def sol1027():
    n = int(input())
    buildings = list(map(int, input().split()))

    answer = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if i == j:
                continue

            u, v = i, j
            
            # 건물 i, j를 보다 왼쪽에 있는 건물(u)과 오른쪽에 있는 건물(v)로 정렬한 뒤
            # u, v 사이의 기울기 a를 측정
            if u > v:
                u, v = v, u
            a = (buildings[u] - buildings[v]) / (u - v)

            # 건물 i, j 사이에 있는 건물 k에 대해 
            # 건물 u와 k 사이의 기울기 b를 측정하여 b 가 a 보다 크다면 건물 k는 i, j 사이를 있는 직선과 만난다
            check = True
            for k in range(u + 1, v):
                b = (buildings[u] - buildings[k]) / (u - k)
                if b >= a:
                    check = False
                    break
            
            # 직선과 만나는 건물이 없을 경우에만 볼 수 있는 건물의 수를 1 증가시킨다.
            if check:
                count += 1
        
        # 볼 수 있는 건물의 최대 수를 갱신
        answer = max(answer, count)

    return answer
