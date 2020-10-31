#intro
print("Hai.. nama saya Mr. Lappie, saya telah memilih sebuat bilangan bulat secara acak anatara 0 - 100. Silakan tebak ya !!!")

#pengecekan menggunakan perulangan
while True:
    bil=int(input("Tebakan Anda : ")) #ini buat menampilkan tulisan, nanti buat nginput juga

    if(bil<0) or (bil>100):
        print("error")
        exit()
    elif(bil<10):
        print("Hehehe...Bilangan tebakan anda terlalu kecil")
    elif(bil>10):
        print("Hehehe...Bilangan tebakan anda terlalu besar")
    elif(bil==10):
        print("Yee...Bilangan tebakan anda benar :)")
        break #ini buat menghentikan perulangan
    