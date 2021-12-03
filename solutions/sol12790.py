import sys

input = sys.stdin.readline


# 12790 Mini Fantasy War
# 주어진 hp, mp 공격력, 방어력과 각각의 추가수치를 합산하여
# 주어진 공식에 따라 전투력을 계산하는 문제
def sol12790():
    answer = []
    for _ in range(int(input())):
        hp, mp, atack, defense, ahp, amp, aatk, adef = map(int, input().split())
        hp += ahp
        if hp < 1:
            hp = 1

        mp += amp
        if mp < 1:
            mp = 1

        atack += aatk
        if atack < 0:
            atack = 0

        defense += adef

        answer.append(hp + 5 * mp + 2 * atack + 2 * defense)

    return '\n'.join(map(str, answer))
