import random    # 게임을 위한 랜덤 숫자 생성
rn = ["0", "0", "0"]
rn[0] = str(random.randrange(1, 9, 1))
rn[1] = rn[0]
rn[2] = rn[0]
while (rn[0] == rn[1]):
    rn[1] = str(random.randrange(1, 9, 1))
while (rn[0] == rn[2] or rn[1] == rn[2]):
     rn[2] = str(random.randrange(1, 9, 1))
#print(rn)
t_cnt = 0 # 시도횟수
s_cnt = 0 # 스트라이크 갯수
b_cnt = 0 # 볼 갯수
print("숫자야구게임을 시작합니다 !!!")

print("---------------------------")

print("---------------------------")

print(t_cnt, "번 만에 정답을 맞추셨습니다.") 