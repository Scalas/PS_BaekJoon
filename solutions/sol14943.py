import sys

input = sys.stdin.readline


# 14943 벼룩 시장
# n명의 사람이 서로 번호의 차이만큼 떨어져있도록 일렬로 서있고
# 서로 벼룩을 매매하며 사는 벼룩의 양과 파는 벼룩의 양은 같다.
# 벼룩을 매매할 때 들어가는 비용은 거래되는 벼룩의 양과 두 사람의 거리를 곱한 값이라 할 때
# 벼룩의 거래를 끝내는데 필요한 최소 비용을 구하는 문제
def sol14943():
    n = int(input())
    seq = list(map(int, input().split()))

    # 벼룩을 파는 사람과 사는 사람으로 구분
    # 이 때, 구매량을 나타내는 음수의 seq 값은 거래량을 파악하기 편하도록 양수로 변경
    sellers = []
    buyers = []
    for i in range(n):
        if seq[i] > 0:
            sellers.append(i)
        elif seq[i] < 0:
            buyers.append(i)
            seq[i] = -seq[i]

    # 왼쪽에 있는 판매자부터 벼룩을 판매해나간다고 할 때,
    # 왼쪽의 구매자의 거래비용은 거리에 비례하여 점점 증가할 것이기 때문에
    # 구매자 또한 왼쪽에서부터 찾는 것이 효율적
    buyers = buyers[::-1]
    answer = 0
    for seller in sellers:
        amount = seq[seller]
        while amount:
            buyer = buyers[-1]
            if amount >= seq[buyer]:
                amount -= seq[buyer]
                buyers.pop()
                answer += abs(seller - buyer) * seq[buyer]
            else:
                seq[buyer] -= amount
                answer += abs(seller - buyer) * amount
                amount = 0

    return answer
