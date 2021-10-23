import sys

input = sys.stdin.readline


# 9935 문자열 폭발
# 문자열에서 특정 문자열을 찾아 제거하고 그 결과 얻은 문자열에 대해
# 다시 특정 문자열을 찾아 제거하기를 반복하여 더이상 제거할 문자열을 찾을 수 없을 때
# 그 문자열을 출력하는 문제
def sol9935():
    string = input().rstrip()
    boom = list(input().rstrip())

    # 문자를 하나씩 추가하다가 제거할 문자열의 끝부분과 일치하는 문자가 들어왔을 경우
    # 문자열을 비교하여 해당 문자열과 일치한다면 제거한다.
    # 스택을 활용하는 방식.
    st = []
    for c in string:
        st.append(c)
        if c == boom[-1] and st[-len(boom):] == boom:
            del st[-len(boom):]
    return ''.join(st) if st else 'FRULA'
