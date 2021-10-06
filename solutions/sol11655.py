import sys

input = sys.stdin.readline


# 11655 ROT13
# 알파벳을 13글자 뒤로 이동한 알파벳으로 치환하여 암호화하는 문제
# 알파벳은 소문자는 소문자내에서, 대문자는 대문자 내에서 순환해야하며
# 알파벳이 아닌문자는 변화가 없어야한다.
def sol11655():
    s = input().rstrip()
    res = []
    for c in s:
        nc = ord(c) + 13
        if c.isalpha():
            if ord('Z') < nc <= ord('Z') + 13:
                res.append(chr(ord('A') + nc % (ord('Z') + 1)))
            elif ord('z') < nc <= ord('z') + 13:
                res.append(chr(ord('a') + nc % (ord('z') + 1)))
            else:
                res.append(chr(nc))
        else:
            res.append(c)

    return ''.join(res)
