import  sys

input = sys.stdin.readline


# 3047 ABC
# A < B < C 일 때
# 주어진 세 수에서 A B C 를 주어진 순서에 따라 출력하는 문제
def sol3047():
    seq = [*map(int, input().split())]
    seq.sort()
    return ' '.join(map(lambda x:str(seq[ord(x)-ord('A')]), list(input().rstrip())))
