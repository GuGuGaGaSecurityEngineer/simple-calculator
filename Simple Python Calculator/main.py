jalan = True
while jalan:
    print("1, jalan")
    print("2, keluar")
    masuk = input("")
    if masuk == "1":
    
        
        try:
            nomor_1 = (input("masukkan angka pertama mau berapa?:")) 
            nomor_2 = (input("masukkan angka kedua mu mau berapa?: "))
            kalkulator = input("masukkan operator yang kamu mau: +, -, *, /: ")

            nomor_1 = float(nomor_1)
            nomor_2 = float(nomor_2)
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
            elif kalkulator == "**":
                hasil = nomor_1 ** nomor_2
                print(hasil)
            else:
                print("salah")
        except ValueError:
            print("Just a number Please!!!")                
    elif masuk == "2":
            jalan = False
    else:
        print("Try again")
        