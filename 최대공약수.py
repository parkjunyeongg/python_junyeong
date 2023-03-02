print("[두 수의 최대 공약수]")
temp = 1
num1 = int(input("수를 입력해주세요 : "))
num2 = int(input("수를 입력해주세요 : "))


if num1 > num2:
    maxn = num1
    minn = num2
else:
    maxn = num2
    minn = num1
    
while temp != 0:
    temp = maxn%minn
    maxn = minn
    minn = temp
    
print("두 수의 최대 공약수는 ",maxn,"입니다.")
