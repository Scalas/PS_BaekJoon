import sys

input = sys.stdin.readline


# 17299 오등큰수
# 수열의 각 수마다 자신보다 오른쪽에있으면서 등장 횟수가 자신보다 많은 수중
# 가장 왼쪽에 있는 수를 구하는 문제. 없다면 -1을 반환
def sol17299():
    n = int(input())
    seq = list(map(int, input().split()))

    # 등장횟수 카운트
    count = [0] * (max(seq)+1)
    for num in seq:
        count[num] += 1

    # answer[i] 는 seq[i] 는 NGF
    answer = [-1] * n

    # seq의 수를 스택에 순차적으로 삽입해나감
    st = []
    for i in range(len(seq)):
        # 기존 스택에 자신보다 등장횟수가 적은 수가 있다면 pop 하고 그 수의 ngf로 자신을 기록
        while st and count[st[-1][0]] < count[seq[i]]:
            _, idx = st.pop()
            answer[idx] = seq[i]

        # 자신을 인덱스와 함께 스택에 삽입
        st.append([seq[i], i])

    # 수열의 모든 수의 ngf 반환
    return ' '.join(map(str, answer))
