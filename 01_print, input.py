print("a" + "b") # ab
print("a", "b") # a b

print(1, 2, 3) # 1 2 3

print('안녕', 'python') # 안녕 python

print(1, 2, 3, sep=' -> ') # 1 -> 2 -> 3

print('안녕', 'python', sep='하지못해 ') #안녕하지못해 python

print(1, 2, 3, sep='\n') # 1\n 2\n 3\n

print('1\n2\n3') # 1\n 2\n 3\n #'\'을 문자로 출력하고 싶을 때는 \\
    
print(1, end="")
print(2, end="")
print(3) # 123

print(1, end=' ')
print(2, end=' ')
print(3) # 1 2 3

print('-'*100) # '문자열'을 숫자만큼 반복하여 출력

company = '리로스쿨'
print(company)

ip = '108.138.141.4' #도메인으로 ip 확인(https://thisthatbase.com/domain-ip-check-online-command/)
url = 'https://jchsl.riroschool.kr/'
print("리로스쿨 url(IP): " , url , "(" + ip + ")") # 문자열을 합칠 때는 + / 리로스쿨 url(IP):  https://jchsl.riroschool.kr/(108.138.141.4)
print("리로스쿨 url(IP): " , url + "(" + ip + ")")  #                     / 리로스쿨 url(IP): https://jchsl.riroschool.kr/(108.138.141.4)
print("리로스쿨 url(IP): " + url + "(" + ip + ")") # 위와 같은 결과 출력 / 리로스쿨 url(IP): https://jchsl.riroschool.kr/(108.138.141.4)


print('너 몇살이니?')
old = float(input()) # input으로 받은 값은 모두 문자열로 저장됨. 계산에 사용될 숫자를 입력하고 싶다면 int(input())
print('10년 뒤 너는', end=' ')
print(int(old + 10), end=' ')
print('살 입니다')

age = 18
print("너는 올해" + str(age) , "살 이니?") # 숫자 age를 문자로 결합하여 사용하려면 str( )로 묶기
# 데이터 타입이 다르면 '+'로 더하거나 이어 붙이기를 할 수 없음.