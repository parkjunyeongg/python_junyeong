scsco = int(input("이수한 학점을 입력하십시오 : "))
if scsco < 40:
    print("1학년 입니다")
elif (40 <= scsco < 80):
    print("2학년 입니다")
else :
    print("3학년 입니다")