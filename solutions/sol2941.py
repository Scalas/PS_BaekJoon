import sys
from re import sub

input = sys.stdin.readline


# 2941 크로아티아 알파벳
# 둘 이상의 문자를 하나의 알파벳으로 보는 경우를 따져 단어에 사용된 알파벳의 갯수를 구하는 문제

# 첫 번째 시도 - re.sub 를 활용한 풀이
# 단순히 크로아티아 알파벳 표현에 해당하는 문자들을 한 문자로 치환하여 문자열의 길이를 출력
def sol2941():
    print(len(sub('(c=|c-|dz=|d-|lj|nj|s=|z=)', '0', input().rstrip())))


# 두 번째 시도 - 전체 문자 수중에 하나로 묶이는 문자의 수만큼을 빼주는 풀이
# dz=의 경우 세 문자가 한 문자로 바뀌기 때문에 = 와 dz= 에서 각각 한번씩 두 번 빼준다
# 1번 풀이보다 훨씬 빨라진다. re.sub 의 import 가 시간을 상당히 잡아먹는 듯
def sol2941_2():
    s = input().rstrip()
    print(len(s) - sum(map(s.count, ['=', '-', 'lj', 'nj', 'dz='])))
