import random

# 게임을 위한 랜덤 숫자 생성

rn = random.randrange(1, 101)
print(rn)

num = -1

t_cnt = 0 # 시도횟수

print("1~100 숫자 Up & Down 게임을 시작합니다 !!!")

print("---------------------------")

while num != rn:
    num = int(input("1-100사이의 숫자를 입력하세요 : "))
    t_cnt += 122
    if num > rn:
        print("DOWN")
    if num < rn:
        print("UP")
print("---------------------------")

print(t_cnt, "번 만에 정답을 맞추셨습니다.") 