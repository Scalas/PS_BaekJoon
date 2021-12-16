import sys

input = sys.stdin.readline


# 17388 와글와글 숭고한
# 세 대학의 참여도 합이 100이상이면 OK, 아니라면 가장 참여도가 낮은 대학의 이름을 출력하는 문제
def sol17388():
    univ = ['Soongsil', 'Korea', 'Hanyang']
    rate = list(map(int,input().split()))
    return 'OK' if sum(rate) >= 100 else univ[rate.index(min(rate))]
