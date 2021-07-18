from random import randrange

while True:
    somay = randrange(1, 101)
    solandoan = 0
    win = False
    while solandoan < 7:
        solandoan += 1
        songuoi = int(input("Máy đoán từ 1 đến 100, mời bạn đoán: "))
        print("Bạn đoán lần thứ", solandoan)
        if somay == songuoi:
            print("Chúc mừng bạn đã đoán đúng, số máy là:", somay)
            win = True
            break
        if somay > songuoi:
            print("Bạn đoán sai, số máy lớn hơn số của bạn.")
        elif somay < songuoi:
            print("Bạn đoán sai, số máy nhỏ hơn số của bạn.")
    if win == False:
        print("GAME OVER!, số mấy là:", somay)
    ask = input("Tiếp không? (Yes/No): ")
    if ask == "No":
        break
print("Cảm ơn bạn đã chơi game!")