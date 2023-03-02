print("[파보나치 수열]")
pa = 1;
pa2 = 1;
result = 0;

num = int(input("몇 번째 항을 출력할까요? (1이상의 양의 정수) :"))

if num > 2:
    for i in range(num-2):
        result=pa+pa2
        pa =pa2
        pa2 =result
else:
    print("파보나치 수열의 ",num,"번째 항은 1입니다.")

print("파보나치 수열의 ",num,"번째 항은",result,"입니다.")