import sys
import re

input = sys.stdin.readline


# 22859 html 파싱
# html 코드를 파싱하는 문제
def sol22859():
    html = input()

    # div 태그를 title : <제목> 으로 치환
    html = re.sub('<div title=\"', '\ntitle : ', html)
    html = re.sub('\">', '', html)

    # p 태그 개행으로 치환
    html = re.sub('<p>', '\n', html)

    # 그 외의 모든 태그 제거
    html = re.sub('<[^>]*>', '', html)

    # 두번 이상 반복된 공백 하나로 치환
    html = re.sub('( )+', ' ', html)

    # 문장 양 끝의 공백을 제거
    # 이 때, 첫 문단으로 인해 생긴 비어있는 첫 라인 제거
    html = '\n'.join(map(lambda x: x.strip(), html.splitlines()[1:]))

    return html
