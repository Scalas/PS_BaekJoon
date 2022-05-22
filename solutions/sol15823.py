import sys

input = sys.stdin.readline


# 15823 카드 팩 구매하기
# n개의 카드가 주어졌을 때, 하나의 카드팩에 같은 카드가 포함되지 않도록하여
# 서로 같은 갯수의 카드를 포함한 m개의 카드팩을 구성하려할 때
# 하나의 카드팩에 포함할 수 있는 카드의 최대 갯수를 구하는 문제
def sol15823():
    n, m = map(int, input().split())
    cards = list(map(int, input().split()))

    # cnt개의 카드로 구성된 카드팩 m개를 만들 수 있는지 체크
    def check(cnt):
        i, j = 0, 0
        pack = 0
        card_set = set()
        while j < n:
            # 카드팩에 추가할 카드
            new_card = cards[j]

            # 추가할 카드가 카드셋 내의 카드와 중복될 경우
            # 중복되지 않을 때 까지 가장 먼저 추가한 카드부터 제거
            while new_card in card_set:
                card_set.remove(cards[i])
                i += 1

            # 새 카드를 삽입
            card_set.add(new_card)

            # 카드팩이 완성된 경우 카드팩 구성을 초기화하고
            # 다음 카드부터 재탐색
            if len(card_set) == cnt:
                pack += 1
                # 만약 카드팩 m개를 모두 구성하는데 성공했을 경우 True 반환
                if pack == m:
                    return True

                card_set = set()
                i, j = j + 1, j + 1

            # 완성되지 않은 경우
            else:
                j += 1

        # 끝까지 탐색하고도 m개의 카드팩을 구성하는데 실패했을 경우
        return False

    # 이분탐색을 사용하여 m개의 카드팩을 구성할 수 있는 경우중
    # 카드의 갯수가 최대인 케이스를 구함
    s, e = 1, n // m
    answer = 1
    while s <= e:
        mid = (s + e) // 2
        if check(mid):
            answer = mid
            s = mid + 1
        else:
            e = mid - 1
            
    return answer
