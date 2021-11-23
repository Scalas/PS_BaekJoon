import sys

input = sys.stdin.readline


# 2161 카드1
# 1~n 번까지의 카드를 맨위에서 한장 버리고 다음카드는 맨뒤로 옮기는 작업을 반복할 때
# 버려지는 순서대로 카드번호를 출력하는 문제
def sol2161():
    cards = [i for i in range(1, int(input())+1)]
    l = len(cards)
    answer = []
    while l > 1:
        ncards = []
        last = 0
        answer.append(cards[0])
        if l % 2:
            last = cards[1]
        else:
            ncards.append(cards[1])
        for i in range(2, l):
            if i % 2:
                ncards.append(cards[i])
            else:
                answer.append(cards[i])
        cards = ncards
        if last:
            cards.append(last)
        l = len(cards)
    answer.append(cards[0])
    return ' '.join(map(str, answer))
