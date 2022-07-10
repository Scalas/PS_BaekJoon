import sys

from collections import defaultdict

input = sys.stdin.readline


# 3673 나눌 수 있는 부분 수열
# 수열 s의 연속하는 부분수열중 합이 d로 나누어 떨어지는것의 갯수를 구하는 문제
def sol3673():
    answers = []
    for _ in range(int(input())):
        d, n = map(int, input().split())
        seq = list(map(int, input().split()))
        seq.append(0)
        count = defaultdict(int)
        answer = 0
        for i in range(n):
            # seq[i] 까지의 누적합을 d로 나눈 나머지를 구함
            seq[i] = (seq[i - 1] + seq[i]) % d

            # 이전까지의 구간합을 d로나눈 나머지 값 중 현재 구간합을 d로 나눈 나머지와 같은 값이 있다면
            # 두 구간 사이에 더해진 수가 d의 배수라는 의미가 됨
            # 즉, 이전까지의 구간합중 d로 나눈 나머지가 현재 구간합을 d로 나눈 나머지와 같은 갯수만큼
            # d로 나누어떨어지는 구간의 갯수가 증가
            answer += count[seq[i]]

            # 만약 나머지가 0이라면 그 자체로 d의 배수이므로 하나 증가
            if not seq[i]:
                answer += 1

            # 구간합을 d로 나눈 나머지의 갯수 증가
            count[seq[i]] += 1

        answers.append(answer)
    return '\n'.join(map(str, answers))
