import sys


# 1620 나는야 포켓몬 마스터 이다솜
# 딕셔너리를 사용해서 간단하게 해결 가능한 문제
def sol1620():
    n, m= map(int, sys.stdin.readline().split())
    input_data = sys.stdin.read().split()
    d = {}
    for i in range(n):
        d[input_data[i]] = str(i+1)

    answer = []
    for i in range(n, n+m):
        try:
            answer.append(input_data[int(input_data[i])-1])
        except ValueError:
            answer.append(d[input_data[i]])
    return '\n'.join(answer)
