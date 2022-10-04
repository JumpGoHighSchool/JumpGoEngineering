month = "12"
def question():
    answer = input("난 몇월생일까?")
    if answer == month:
        print("정답입니다. 저는 "+month+"월 생입니다.")
    else:
        print("아닙니다")
        question()
question()
