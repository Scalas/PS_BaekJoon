import sys

input = sys.stdin.readline


# 5397 키로거
# 키로거가 남긴 기록에 타이핑한 문자가 순서대로 주어지고
# 그 중 <, > 는 커서를 좌우로 한 칸 이동, - 는 백스페이스를 의미한다고 할 때
# 타이핑된 비밀번호를 구하는 문제
def sol5397():
    answers = []
    for _ in range(int(input())):
        s = input().rstrip()
        pw = []
        buf = []
        for c in s:
            # 커서 왼쪽으로 이동시 글자 하나를 pop 하여 임시 스택에 push
            if c == '<':
                if pw:
                    buf.append(pw.pop())

            # 커서 오른쪽으로 이동시 임시 스택에 글자가 있다면 pop 하여 패스워드 스택에 push
            elif c == '>':
                if buf:
                    pw.append(buf.pop())

            # 백스페이스 입력시 패스워드 스택에서 글자 하나 pop
            elif c == '-':
                if pw:
                    pw.pop()

            # 그 외에는 일반 문자 타이핑
            else:
                pw.append(c)

        # 임시 스택의 문자 모두 pop 하여 패스워드 스택에 push
        while buf:
            pw.append(buf.pop())

        answers.append(''.join(pw))

    return '\n'.join(answers)
