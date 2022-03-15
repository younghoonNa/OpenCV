# 물리적 명령행 : 소스코드에서 눈으로 보이는 한 행
# 논리적 명령행 : 파이썬 인터프리터 관점에서의 한 행의 명령 단위

title = '서기 1년 1월 1일부터 '\
        '오늘 까지' \
        '일 수 구하기.'  # 3행에 걸쳐 작성. -> 1개의 논리적 명령행.

months = [31, 28, 31, 30, 31, 30,
          31, 31, 30, 31, 30, 31]

year, month = 2020, 1           # 여러개 변수 한 행에 선언
day = 7; ratio = 365.2425      # 2개 논리적 명령행.

days = (year-1) * ratio + \
    sum(months[:month-1]) + day  # 1개의 논리적 명령행.

print(title), print('-년:', year), print('-월:', month)
print('-일:',day), print("*일수 총합:", int(days))
