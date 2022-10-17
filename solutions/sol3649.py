import sys

input = sys.stdin.readline


# 3649 로봇 프로젝트
# 테스트케이스마다 구멍의 너비, 블록의 갯수, 각 블록의 너비의 길이가 주어졌을 때
# 각 테스트 케이스의 구멍의 너비를 두 개의 블록의 너비의 합으로 채울 수 없다면 danger를,
# 채울 수 있다면 가능한 블록의 쌍 중 너비 차가 가장 큰 쌍을 오름차순으로 출력하는 문제
def sol3649():
    answer = []

    while True:
        try:
            x = int(input()) * 10000000
        except:
            return '\n'.join(answer)
        n = int(input())

        if not n:
            answer.append('danger')
            continue

        seq = [int(input()) for _ in range(n)]
        seq.sort()

        s, e = 0, n - 1
        check = False
        while s < e:
            t = seq[s] + seq[e]
            if t == x:
                answer.append(f'yes {seq[s]} {seq[e]}')
                check = True
                break
            if t < x:
                s += 1
            else:
                e -= 1

        if not check:
            answer.append('danger')
