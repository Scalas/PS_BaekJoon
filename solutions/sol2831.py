import sys

input = sys.stdin.readline


# 2831 댄스 파티
# 남자 n명, 여자 n명의 키가 주어지고 키가 음수라면 키의 절댓값이 자신보다 작은 이성과 춤을 추려는 것이라고 할 때
# 서로의 조건을 만족하는 쌍을 최대 몇 쌍 만들 수 있는지 구하는 문제
def sol2831():
    n = int(input())

    # 남자, 여자의 키를 음수, 양수로 구분하여 별도의 리스트에 삽입
    male_m, male_p, female_m, female_p = [], [], [], []
    for height in map(int, input().split()):
        if height < 0:
            male_m.append(height)
        else:
            male_p.append(height)
    for height in map(int, input().split()):
        if height < 0:
            female_m.append(height)
        else:
            female_p.append(height)

    # 절댓값 기준으로 정렬
    male_m.sort(reverse=True)
    male_p.sort()
    female_m.sort(reverse=True)
    female_p.sort()

    # 각 리스트의 길이
    mml, mpl, fml, fpl = len(male_m), len(male_p), len(female_m), len(female_p)

    # 매칭할 수 있는 짝의 갯수
    answer = 0

    # 자신보다 키가 작은 여자와 춤을 추려는 남자와
    # 자신보다 키가 큰 남자와 춤을 추려는 여자를 매칭
    mi, fi = 0, 0
    while mi < mml and fi < fpl:
        # 짝을 지을 수 있다면 짝의 수를 1 증가
        # 다음 여자, 남자로 이동
        if -male_m[mi] > female_p[fi]:
            answer += 1
            mi += 1
            fi += 1

        # 다음 남자로 이동
        else:
            mi += 1

    # 자신보다 키가 작은 남자와 춤을 추려는 여자와
    # 자신보다 키가 큰 여자와 춤을 추려는 남자를 매칭
    mi, fi = 0, 0
    while mi < mpl and fi < fml:
        # 짝을 지을 수 있다면 짝의 수를 1 증가
        # 다음 여자, 남자로 이동
        if male_p[mi] < -female_m[fi]:
            answer += 1
            mi += 1
            fi += 1

        # 다음 여자로 이동
        else:
            fi += 1

    return answer
