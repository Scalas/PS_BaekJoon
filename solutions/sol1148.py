import sys
from collections import defaultdict

input = sys.stdin.readline


# 1148 단어 만들기
# 사전의 단어와 사용 가능한 문자 9개로 이루어진 테스트케이스들이 주어졌을 때
# 각 테스트케이스마다 주어진 문자 9개중 한 문자를 반드시 사용해야할 때 만들 수 있는 단어의 수가
# 가장 적은 문자와 가장 많은 문자들을 각각 만들 수 있는 단어 수와 함께 출력하는 문제
def sol1148():
    word_count = []
    while True:
        s = input().rstrip()
        if s == '-':
            break
        alpha = [0] * 26
        for c in s:
            alpha[ord(c) - ord('A')] += 1
        word_count.append([(i, alpha[i]) for i in range(26) if alpha[i]])

    answers = []
    while True:
        s = input().rstrip()
        if s == '#':
            break
        alpha = defaultdict(int)
        for c in s:
            alpha[ord(c) - ord('A')] += 1

        score = defaultdict(int)
        for ch in alpha.keys():
            score[ch] = 0
        for word in word_count:
            check = True
            for o, cnt in word:
                if alpha[o] < cnt:
                    check = False
                    break

            if not check:
                continue

            for o, _ in word:
                score[o] += 1

        result = [(cnt, ch) for ch, cnt in score.items()]
        if not result:
            cases = ''.join(sorted(s))
            answers.append(f'{cases} 0 {cases} 0')
        else:
            result.sort()
            min_score = result[0][0]
            max_score = result[-1][0]
            answer = []
            cases = []
            for i in range(len(result)):
                cnt, sc = result[i]
                if cnt == min_score:
                    cases.append(chr(sc + ord('A')))
                else:
                    break
            answer.append(''.join(sorted(cases)))
            answer.append(str(min_score))

            cases = []
            for i in range(len(result) - 1, -1, -1):
                cnt, sc = result[i]
                if cnt == max_score:
                    cases.append(chr(sc + ord('A')))
                else:
                    break
            answer.append(''.join(sorted(cases)))
            answer.append(str(max_score))
            answers.append(' '.join(answer))
    return '\n'.join(answers)
