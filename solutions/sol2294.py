import sys

input = sys.stdin.readline


# 2294 동전 2
# 주어진 값어치의 동전들을 가지고 k원을 만들 때
# 필요한 동전의 최소 갯수를 구하는 문제
def sol2294():
    # 동전의 종류 수와 만들려는 액수
    n, k = map(int, input().split())

    # 각 동전의 값어치.  중복되는 가치가 주어질 수도 있기 때문에 set 으로 중복을 제거해준다.
    coins = set([int(input()) for _ in range(n)])

    # 가장 적은 가치의 동전
    min_coin = min(coins)

    # 해당 액수를 이미 만든 적이 있는지 확인
    visited = [False] * (k + 1)

    # 처음 액수 리스트를 만들려는 액수 k로 시작하여
    # 동전의 값어치를 빼나가며 0을 만드는데 걸리는 반복 횟수를 구한다
    cost = [k]
    answer = 0
    while cost:
        answer += 1
        u = []
        for c in cost:
            for coin in coins:
                val = c - coin
                # 만약 0을 만드는데 성공했다면 answer 반환
                if val == 0:
                    return answer
                # 만들어진 액수가 가장 작은 가치의 동전보다 크거나 같고 아직 만들어진 적이 없는 액수라면
                # 만들어진 액수 리스트에 추가하고 만든적이 있는 액수로 표시
                if val >= min_coin and not visited[val]:
                    u.append(val)
                    visited[val] = True
        cost = u

    # 더이상 만들 수 있는 유의미한 액수가 없을 때 까지 0원을 만들지 못했다면 -1 반환
    return -1
