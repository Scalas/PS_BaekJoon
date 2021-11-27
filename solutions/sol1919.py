import sys

input = sys.stdin.read


# 1919 애너그램 만들기
# 주어진 두 문자열이 애너그램이 되기위해 지워야할 문자의 최소 갯수를 구하는 문제
def sol1919():
    a, b = input().split()
    count = [0] * 26
    for c in a:
        count[ord(c)-ord('a')] += 1

    answer = 0
    for c in b:
        idx = ord(c) - ord('a')
        if count[idx]:
            count[idx] -= 1
        else:
            answer += 1
    answer += sum(count)
    return answer
