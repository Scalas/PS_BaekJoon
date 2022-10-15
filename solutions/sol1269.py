import sys

input = sys.stdin.readline


# 1269 대칭 차집합
# 두 집합 A, B 가 주어졌을 때
# A - B , B - A 의 원소의 갯수의 합을 구하는 문제
def sol1269():
    n, m = map(int, input().split())
    seq_a = set(map(int, input().split()))
    seq_b = set(map(int, input().split()))
    
    # 두 집합의 크기의 합에서 교집합의 크기 * 2 를 뺸다
    return n + m - len(seq_a & seq_b) * 2
