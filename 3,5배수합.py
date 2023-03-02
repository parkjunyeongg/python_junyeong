print("[3의 배수와 5의 배수의 합 구하기]")
num=int(input("양의 정수 n을 입력하세요 :"))
sum = 0

for i in range(1,num+1):
    if i % 3 ==0 or i % 5 ==0 :
        sum += i

print("1부터 ",num,"까지의 자연수 중에서 3의 배수와 5의 배수의 합 :")
print(sum)