import sys

input = sys.stdin.read


# 11054 가장 긴 바이토닉 부분 수열
# 증가하다가 감소하는 구간의 최대길이를 구하는 lis 응용문제
# 최장 증가부분수열의 길이를 양 방향으로 구하여 해결 가능하다
def sol11053():
    n, *seq = map(int, input().split())
    llis, rlis = [seq[0]], [seq[-1]]
    ldp, rdp = [0] * n, [0] * n
    ldp[0] = rdp[-1] = 1
    for i in range(1, n):
        num1, num2 = seq[i], seq[n - 1 - i]
        if num1 > llis[-1]:
            llis.append(num1)
        else:
            for j in range(len(llis)):
                if llis[j] >= num1:
                    llis[j] = num1
                    break
        if num2 > rlis[-1]:
            rlis.append(num2)
        else:
            for j in range(len(rlis)):
                if rlis[j] >= num2:
                    rlis[j] = num2
                    break
        ldp[i], rdp[n - 1 - i] = len(llis), len(rlis)

    print(max([ldp[i] + rdp[i] - 1 for i in range(n)]))
