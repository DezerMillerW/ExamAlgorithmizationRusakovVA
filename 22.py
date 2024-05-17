class primer:
    def matem():
        a = int(input("Введите кол-во чисел: "))
        c = 0
        pl = float(0.5)
        for i in range(a):
            b = int(input("Введите число: "))
            c+=b
        print("Среднее значеlние: ",c/a,"Округленное в меньшую сторону: ", c//a)
        if (c/a) - (c//a) < pl:
            print('Округление по правилам: ',c//a)
        else:
            print("Округление по правилам: ",c//a+1)

    while True:
        gel = input("Начать? да  нет")
        if gel == "да" or gel == "Да" or gel =="ДА":
            matem()
        else:
            print("До свидания")
            break
