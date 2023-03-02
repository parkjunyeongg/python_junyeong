num = int(input("인치로 변환할 길이(cm)를 입력해주세요 : "))
innum = num/2.54
if num < 0:
    print("잘못 입력하였습니다.")
else:
    print(innum,"인치 입니다.")
