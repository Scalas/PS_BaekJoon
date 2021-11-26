import sys

input = sys.stdin.read


# 11943 파일 옮기기
# 두개의 바구니에 들어있는 사과와 오렌지를 각각 하나의 바구니로 몰아담으려할 때
# 과일을 옮기는 최소횟수를 구하는 문제
def sol11943():
    u, v, w, x = map(int, input().split())
    return min(u+x, v+w)
