import sys

input = sys.stdin.readline


# 2839 설탕 배달
# 어떤 수 n을 5와 3의 조합으로 만들 때 5와 3의 갯수의 최솟값을 구하는 문제
# 정확하게 n을 만들 수 없을 경우 -1 출력
# 최대한 많은 수의 5를 사용해야하는 문제이기 때문에
# 우선 n을 5로 나눈 몫을 answer 로 하고
# n을 5로 나눈 나머지가 3으로 나눠 떨어질때까지 나머지에 다시 5를 더하며 5의 갯수를 줄여나간다 (n += 5, answer -= 1)
# 나머지가 3으로 나누어 떨어지게되면 answer에 나머지를 3으로 나눈 몫을 더해주면 답이 된다
# 나머지가 끝까지 3으로 나누어 떨어지지 않을 경우 5와 3의 조합으로 만들 수 없는 수이기 때문에 -1을 출력한다
def sol2839():
    n = int(input())
    answer = 0
    answer += n // 5
    n %= 5
    while (n % 3 != 0 and answer > 0):
        n += 5
        answer -= 1
    if n%3==0:
        print(answer + n//3)
    else:
        print(-1)
