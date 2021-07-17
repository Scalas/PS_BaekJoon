import sys
from bisect import bisect_left

# 14002 가장 긴 증가하는 부분 수열 4
# 가장 긴 증가하는 부분수열의 길이 뿐 아니라 증가하는 부분 수열자체도 실제로 구하는 문제


# 첫 번째 방법
# 각 숫자가 들어올 때 마다 이전까지의 최장 증가수열을 탐색
# 해당 숫자보다 작은 숫자에서의 최장 증가수열중 길이가 가장 긴 것을 찾아 끝에 해당 숫자를 삽입하면
# 해당 숫자를 포함할 때의 최장 증가수열이 구해진다
# 그렇게 구한 모든 최장 증가수열중 가장 긴 것이 수열의 최장증가수열이 된다
def sol14002(n, seq):
    lis = [[] for _ in range(n)]
    for i in range(n):
        lis[i] = [seq[i]]
        for j in range(i):
            if seq[j] < seq[i] and len(lis[j]) + 1 > len(lis[i]):
                lis[i] = lis[j] + [seq[i]]
    res = max(lis, key = lambda x:len(x))
    return f'{len(res)}\n'+' '.join(map(str, res))


# 두 번째 방법
# 최장증가수열의 길이만을 구할때 사용했던 이진탐색 방식을 활용한다.
# 수열을 순회하며 현재 숫자가 lis 의 마지막 수 보다 클 경우 append,
# 그렇지 않은 경우 lis 에서 현재 숫자보다 크거나 같은 수 중 최솟값을 현재 숫자로 치환한다.
# 그리고 각각의 경우에서 현재 숫자의 lis 에서의 인덱스를 path 에 저장한다.
# 순회를 마치면 lis 의 길이가 최장증가수열의 길이가 되며
# path 를 역으로 순회하며 lis 의 마지막 인덱스부터 시작해서 매칭해나가면
# 최장 증가수열을 구할 수 있다.
def sol14002_2(n, seq):
    lis, path = [], []
    for i in range(n):
        num = seq[i]
        if not lis or num > lis[-1]:
            lis.append(num)
            path.append(len(lis) - 1)
        else:
            p = bisect_left(lis, num)
            lis[p] = num
            path.append(p)

    l = len(lis) - 1
    res = []
    for p, num in list(zip(path, seq))[::-1]:
        if p == l:
            res.append(str(num) + ' ')
            l -= 1
    res.append(str(len(lis)) + '\n')
    return ''.join(res[::-1])
