import random #랜덤 숫자를 만들기 위해 import를 사용하여여 랜덤모듈을 가져옴
n = random.randint(1, 100) #randint코드를 사용해 1~100 사이에 랜덤 숫자 생성
while True: #정답을 맞출 때까지 반복
    x = int(input("맞춰보세요 (1~100): ")) #숫자 입력 받기
    if x < n: #만약 숫자가 정답보다 작으면
        print("Up") #업 출력
    elif x > n: #만약 숫자가 정답보다 크면
        print("Down") #다운 출력
    else: #정답을 맞추면
        print("정답!") #정답 출력
        break #끝