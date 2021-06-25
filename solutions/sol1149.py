from sys import stdin


# 1149 RGB 거리
# 인접한 집이 같은색이 되지 않도록 칠할 때 최소비용을 구하는 문제
# 이전 집에서 어떤색을 골랐을때의 최소비용을 동적계획법으로 구해나가면 해결 가능하다
# 첫번째 집에선 단순히 입력받은 가격순
# 두번째 집 이후는 (이번집에서 고른 색의 값) + (이전 집에서 그 색이 아닌 색을 골랐을 떄의 값 중 최솟값)이 된다
def sol1149():
    n = int(stdin.readline())
    cost = list(map(int, stdin.readline().split()))
    for i in stdin:
        c = list(map(int, i.split()))
        c[0] += min(cost[1], cost[2])
        c[1] += min(cost[0], cost[2])
        c[2] += min(cost[0], cost[1])
        cost = c

    print(min(cost))
