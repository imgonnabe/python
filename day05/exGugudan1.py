"""
파일명: exGugudan1.py
프로그램 설명: while문을 이용한 구구단 출력하기
"""

dan=2
i=1
while i<=9:
    print(f'{dan} x {i} = {dan*i}', end=' ')
    i+=1
else:
    print()