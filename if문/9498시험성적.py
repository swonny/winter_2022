# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

a = int(input())
print('A' if 90<=a<=100 else ('B' if a>=80 else ('C' if a>=70 else ('D' if a>= 60 else 'F'))))