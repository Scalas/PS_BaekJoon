import sys

input = sys.stdin.readline


# 2866 문자열 잘라내기
# 주어진 n * m 의 문자열의 행렬에서 맨 윗 행을 제거했을 때
# 문자를 위에서 아래로 읽어 만든 문자열중 같은 문자열이 하나도 없을 경우
# count 를 1 더하고 맨 위의 문자들을 제거한다.
# 주어진 문자 행렬에 대해 위 연산을 반복했을 때 얻을 수 있는 count의 수를 구하는 문제
def sol2866():
    n, m = map(int, input().split())
    # 맨 윗열은 맨처음에 제거하고 같은 문자열이 있는지를 보기 때문에 의미가 없음
    input()

    # 남은 문자열 행렬에서 세로로 읽은 문자열을 추출하여 역순으로 뒤집은 뒤 정렬
    strings = list(map(lambda x: ''.join(x[::-1]), zip(*[list(input().rstrip()) for _ in range(n - 1)])))
    strings.sort()

    # 정렬한 문자열은 인접해있을수록 앞부분이 같은 문자열인 수가 많기 때문에 O(N)으로 일치하는 문자수가 가장 많은 것을 탐색 가능
    # 처음으로 같은 문자열이 등장하는 순간은 뒤쪽부터 봤을 때 가장 같은 부분이 긴 문자열의 중복부분을 처음 방문한 순간
    # 전체 연산 수에서 모든 문자열의 뒷부분으로부터의 일치 문자 갯수의 최댓값을 뺀 값이 답이된다.
    max_match = 0
    for i in range(m - 2):
        cnt = 0
        while cnt < n - 1 and strings[i][cnt] == strings[i + 1][cnt]:
            cnt += 1
        max_match = max(max_match, cnt)
    return n - max_match - 1
