line = int(input("최대 별 개수를 몇개까지로 할까요?"))
current = 0
count = 0
while count <= line*2-1:
    if line > count:
        print("*"*current)
        current += 1
        count += 1
    else:
        print("*"*current)
        current -= 1
        count += 1
        
star = 10       
for i in range(1,star):
    print("*"*i)
for i in range(star,0,-1):
    print("*"*i)