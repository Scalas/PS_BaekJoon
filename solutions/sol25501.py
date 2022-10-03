import sys

input = sys.stdin.readline


# 25501 재귀의 귀재
# 재귀로 팰린드롬 여부를 판별하는 함수 isPalindrome 으로 문자열 s를 판별할 때
# 팰린드롬 여부와 판별까지 호출된 isPalindrome 의 횟수를 구하는 문제
def sol25501():
    answers = []

    def is_palindrome(s):
        count = 0
        left, right = 0, len(s) - 1
        while left < right:
            count += 1
            if s[left] != s[right]:
                return 0, count
            left += 1
            right -= 1
        return 1, count + 1

    for _ in range(int(input())):
        s = input().rstrip()
        answers.append(' '.join(map(str, is_palindrome(s))))

    return '\n'.join(answers)
