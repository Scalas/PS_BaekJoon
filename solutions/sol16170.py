from datetime import datetime


# 16170 오늘의 날짜
# 오늘의 utc기준 날짜를 년 월 일 순으로 출력하는 문제
def sol16170():
    cur = datetime.utcnow()
    return '\n'.join(map(str, [cur.year, cur.month, cur.day]))
