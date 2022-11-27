import sys

input = sys.stdin.readline


# 1062 가르침
# anta 로 시작하여 tica로 끝나는 n개의 단어가 주어졌을 때
# 알파벳 문자를 k개만 사용하여 나타낼 수 있는 단어의 최대 갯수를 구하는 문제
def sol1062():
    n, k = map(int, input().split())
    if k < 5:
        return 0
    k -= 5

    alpha_bit = dict()
    for c in 'abcdefghijklmnopqrstuvwxyz':
        alpha_bit[c] = 1 << (ord(c) - ord('a'))

    # 알파벳을 나타내는데 필요한 문자의 종류를 bit mask로 나타냄
    # k개보다 많은 알파벳이 필요한 단어는 제거
    words = []
    default = set('antic')
    for _ in range(n):
        word_set = set(input().rstrip()) - default
        if len(word_set) > k:
            continue
        words.append(sum(alpha_bit[c] for c in word_set))

    answer = 0

    # 사용가능한 알파벳의 상태가 learned_bit 과 같을 때
    # 만들 수 있는 단어의 갯수
    def simulate(learned_bit):
        res = 0
        for word in words:
            if word | learned_bit == learned_bit:
                res += 1
        return res

    cands = list("bdefghjklmopqrsuvwxyz")

    # 사용할 k - 5개의 알파벳을 구함(무조건 들어가는 antic 제외)
    # 모두 고른 뒤 simulate 하여 나온 단어의 갯수로 최댓값을 갱신
    def select(idx, learned, count):
        nonlocal answer
        if 21 - idx < k - count:
            return

        if count == k:
            answer = max(answer, simulate(learned))
            return

        select(idx + 1, learned | alpha_bit[cands[idx]], count + 1)
        select(idx + 1, learned, count)

    select(0, 0, 0)

    return answer
