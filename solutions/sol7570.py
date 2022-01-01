import sys

input = sys.stdin.read


# 7570 줄 세우기
# 1 ~ n의 수를 특정 수를 맨 앞으로 보내거나 맨 뒤로 보내는 명령만을 사용하여
# 오름차순 정렬할 때 필요한 최소 명령 수를 구하는 문제
def sol7570():
    n, *seq = map(int, input().split())

    # 카운팅 정렬
    # 정렬시에 갯수대신 해당 수의 기존 인덱스를 (1~n) 넣어준다
    ss = [0] * (max(seq) + 1)
    for i in range(n):
        ss[seq[i]] = (i+1)

    # 최대 연속증가구간 길이, 이전 숫자, 현재 연속증가구간 길이
    max_inc, pre, cnt = 0, 0, 0

    # 정렬된 수의 인덱스가 증가하는 연속 부분구간의 최대길이를 구함
    for i in range(len(ss)):
        if not ss[i]:
            continue

        if ss[i] > pre:
            cnt += 1
        else:
            max_inc = max(max_inc, cnt)
            cnt = 1
        pre = ss[i]
    max_inc = max(max_inc, cnt)

    # 연속 부분구간의 최대길이만큼은 이미 정렬된 상태이기에 건들 필요가 없음
    # 연속 부분구간의 최솟값보다 작은 수들만큼 맨앞으로 보내고 최댓값보다 큰 수들만큼 맨뒤로 보내면
    # 이동횟수를 최소화하여 정렬할 수 있기 때문에 n - max_inc 가 최소 이동횟수가 된다.
    return n - max_inc
