import sys
import math

input = sys.stdin.readline


# 2869 달팽이는 올라가고 싶다
# 달팽이가 하루에 a만큼 올라가고 b만큼 미끄러질때 v만큼 올라가기 위해 걸리는 일수를 구하는 문제
# 기본적으론 하루 a-b만큼 올라가지만 마지막에 a만큼 올라가서 v만큼 올랐을 경우 굳이 미끄러지는걸 고려할 필요가 없음
# 올라야할 높이에서 마지막 한번 오를 만큼을 미리 빼두고 a-b로 나누어 미끄러지면서 올라가야할 일수를 구한 뒤
# 마지막날 하루를 더해주면 된다.
def sol2869():
    a, b, v = map(int, input().split())
    print(math.ceil((v - a) / (a - b)) + 1)
