import sys

input = sys.stdin.readline


# 5598 카이사르 암호
# 알파벳 문자를 3칸 뒤로 밀어서 만들어진 암호를 복호화하는 문제
def sol5598():
    return ''.join(map(caesar_decryption, input().rstrip()))


def caesar_decryption(c):
    conv = (ord(c) - ord('A') - 3)
    if conv < 0:
        conv += 26
    return chr(ord('A') + conv)
