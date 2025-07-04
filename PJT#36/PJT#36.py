from datetime import datetime

def get_days_in_current_month():
    # 월별 기본 날짜 수
    days_in_month = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    today = datetime.today()
    year = today.year
    month = today.month

    # 윤년이면 2월 => 29일로
    if month == 2 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        return 29
    else:
        return days_in_month[month]

# 예시 출력
print(f"이번 달의 일수는 {get_days_in_current_month()}입니다.")
