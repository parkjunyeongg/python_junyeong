import random

while True :
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    dice3 = dice1+dice2
    print("나온 주사위 : ",dice1,dice2)

    if dice3 == 7:
        print("주사위 합 7, 이겼습니다.")
        print("종료합니다.")
        break
    else:
        print("주사위 합",dice3,", 졌습니다.")
        print("다시 던집니다.")
