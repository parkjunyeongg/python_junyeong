import random

player = 50

while True:
    if (player < 0):
        print("파산!")
        break
    if (player > 100):
        print("당신이 가진 $ :",player,"이겼습니다!")
        break
    print("당신이 가진 $ :",player)
    coin = random.randint(1,2)
    num = int(input("앞면, 뒷면을 맞추기 (앞면1,뒷면2) : "))
    
    if coin == num:
        print("맞췄습니다! 9$획득\n")
        player += 9
        coin = 0
        num = 0
    else:
        print("틀렸습니다. 10$손실\n")
        player -= 10
        coin =0
        num= 0

