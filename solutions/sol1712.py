import sys

input = sys.stdin.readline


# 1712 손익분기점
# 고정비용 A, 상품 제조단가 B, 상품 판매단가 C 가 주어질 때
# 손익분기점이 되는 상품 판매량 N의 값 구하기
def sol1712():
    a, b, c = map(int, input().split())
    print(a // (c - b) + 1 if c > b else -1)
