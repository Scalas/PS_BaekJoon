import sys
from math import log2, ceil

input = sys.stdin.readline


# 2201 이친수 찾기
# 1이 연속으로 등장하지 않는 이진수를 이친수라 하고 이를 크기순으로 정렬했을 때
# k번째 이친수를 구하는 문제
def sol2201():
    k = int(input())

    # 2 이하인 이친수는 바로 반환
    if k == 1:
        return 1
    if k == 2:
        return 10

    # dp[i] 는 각 자릿수별 이친수의 갯수
    # 모든 두자리 이상의 이친수는 10으로 시작하므로
    # n자리 이친수는 10 뒤에 자신보다 작은 자릿수를 붙여 만들 수 있음
    # 단, 10으로 두자리를 사용하기 때문에 n - 2 자리까지의 이친수만을 붙일 수 있음
    # 0자리 이친수는 존재하지 않지만 10 뒤에 아무 이친수도 붙이지 않고 0으로만
    # 나머지 자리를 채우는 경우의 수를 계산하기 위해 1개 존재하는 것으로 둔다
    dp = [1, 1, 1]

    # acc[i] 는 i자리 까지의 이친수의 갯수의 합
    # 단, 여기에는 실제로 이친수가 아닌 0자리 이친수가 포함되므로
    # 실제 이친수의 갯수는 acc[i] - 1 이 된다
    acc = [1, 2, 3]

    # 총 이친수의 갯수가 k개 이상이 될때까지 자릿수 증가
    while acc[-1] - 1 < k:
        dp.append(acc[-1] - dp[-1])
        acc.append(acc[-1] + dp[-1])

    # k번째 이친수의 자릿수는 처음으로 acc[i] - 1이 k 이상이 됐을 때의 i값
    # 즉, dp 배열의 마지막 인덱스
    digit = len(dp) - 1

    # k번째 이친수를 완성해나가기 위한 재귀함수
    def dfs(remain, idx):
        nonlocal digit

        # 만약 모든 자릿수를 확정지었다면 함수 종료
        if idx >= digit:
            return

        # 처음으로 이친수의 총 갯수가 remain 이상이 되는 자릿수를 구함
        # 단, 여기서는 맨 앞자리가 1일 필요가 없기 때문에 0자리 이친수도 갯수에 포함시킴
        i = 0
        while acc[i] < remain:
            i += 1

        # 구한 이친수의 시작점을 해당하는 자릿수에 표시하고 확정된 자릿수를 증가시킴
        # 단, 자릿수가 0인 이친수의 경우 1을 표시하지 않으며
        # 자릿수가 2 이상인 이친수를 붙였을 경우에만 확정 자릿수를 2 증가시킨다(그 외에는 1 증가)
        idx = digit - i
        if idx < digit:
            answer[idx] = '1'
        idx += 1
        if i > 1:
            idx += 1

        # 이 과정에서 지나친 이친수의 갯수만큼을 구해야할 남은 이친수 갯수에서 제외
        remain -= acc[i - 1]

        dfs(remain, idx)

    # k번째 이친수의 자릿수 길이만큼의 배열을 생성
    answer = ['0'] * digit

    # 첫 시작은 0
    answer[0] = '1'

    # 현재 값이 확정된 자릿수는 2개 (10)
    idx = 2

    # 현재보다 자릿수가 적은 이친수는 모두 지나쳤기 때문에
    # 앞으로 remain만큼의 이친수를 더 구해야함
    remain = k - acc[digit - 1] + 1

    dfs(remain, idx)

    return ''.join(answer)
