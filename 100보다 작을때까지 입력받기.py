sum = 0

print("[숫자의 합이 100보다 작을때 까지 입력받기]")

while sum < 100:
    num = int(input("숫자를 입력하세요: "))
    sum += num
    
print("[결과]")
print("입력받은 숫자들의 합 :",sum)
