jalan = True
while jalan:
    print("1, jalan")
    print("2, keluar")
    masuk = input("")
    if masuk == "1":

        nomor_1 = float(input("masukkan angka pertama mau berapa?:")) 
        nomor_2 = float(input("masukkan angka kedua mu mau berapa?: "))
        kalkulator = input("masukkan operator yang kamu mau: +, -, *, /: ")
        if kalkulator == "+":
            hasil = nomor_1 + nomor_2
            print(hasil)
        elif kalkulator == "-":
            hasil = nomor_1 - nomor_2
            print(hasil)
        elif kalkulator == "*":
            hasil = nomor_1 * nomor_2
            print(hasil)
        elif kalkulator == "/":
            hasil = nomor_1 / nomor_2
            print(hasil)
        else:
            print("salah")
    elif masuk == "2":
        jalan = False
    else:
        print("Try again")