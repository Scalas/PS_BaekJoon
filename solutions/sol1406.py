import sys

input = sys.stdin.readline


# 1406 에디터
# 리스트 내에서 삽입, 삭제 연산을 반복하여 결과를 반환하는 문제
# 연결리스트를 사용하여 해결해야하는 문제
# Python 은 연결리스트를 지원하지 않지만 두개의 리스트를 스택처럼 활용하면
# 사실상 연결리스트처럼 사용할 수 있다.
def sol1406():
    editor = list(input().rstrip())
    editor_r = []
    for _ in range(int(input())):
        cmd = input().split()
        t = cmd[0]
        if t == 'P':
            editor.append(cmd[1])
        elif t == 'B':
            if editor:
                editor.pop()
        elif t == 'L':
            if editor:
                editor_r.append(editor.pop())
        else:
            if editor_r:
                editor.append(editor_r.pop())


    return ''.join(editor+editor_r[::-1])
