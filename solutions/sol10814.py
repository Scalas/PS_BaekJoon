from sys import stdin

input = stdin.readline


# 10814 나이순 정렬
# 나이, 이름을 입력받아 나이순으로 오름차순 정렬, 나이가 같다면 입력받은 순으로 오름차순 정렬하는 문제
def sol10814():
    member = []
    for i in range(int(input())):
        age, name = input().split()
        member.append((int(age), i, name))
    member.sort()
    member = [f'{age} {name}' for age, i, name in member]
    print('\n'.join(member))
