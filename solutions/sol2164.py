import sys
from collections import deque

input = sys.stdin.readline


# 2164 카드 2
# 위에서부터 1부터 n 까지의 숫자가 적힌 카드뭉치에 하나 제거, 하나는 맨 뒤로 보내는 작업을 반복하여
# 마지막에 남은 한장의 카드에 적힌 숫자를 구하는 문제

# 실제로 큐에 숫자를 집어넣고 시뮬레이션 해보는 풀이
def sol2164():
    n = int(input())

    cards = deque(range(1, n + 1))

    while (len(cards) > 1):
        cards.popleft()
        cards.append(cards.popleft())

    print(cards[0])


if __name__ == '__main__':
    sol2164()


# 한바퀴 돌때마다 뭉치의 갯수가 짝수라면 짝수번째 요소를 기존 순서대로 줄세운 형태가 되며
# 홀수라면 짝수번째 요소를 기존 순서대로 줄세운 뒤 첫번째 요소를 맨 뒤로 보낸 형태가 되는 것을 이용한 풀이
# 큐를 사용하지 않을 뿐 첫 번째 풀이와 큰 차이는 없음
def sol2164():
    n = int(input())

    cards = [num for num in range(1, n + 1)]
    l = len(cards)
    while (l > 1):
        if (l % 2 == 0):
            cards = [cards[i] for i in range(1, l, 2)]
            l = len(cards)
        else:
            tmp = cards[1]
            cards = [cards[i] for i in range(3, l, 2)]
            cards.append(tmp)
            l = len(cards)

    print(cards[0])


if __name__ == '__main__':
    sol2164()