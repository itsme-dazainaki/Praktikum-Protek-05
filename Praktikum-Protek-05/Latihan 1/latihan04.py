#mari menginput, variabel beserta type dan inputannya
kode = int(input("Masukkan Kode Karyawan : "))
nama = str(input("Masukkan Nama Karyawan : "))
gol  = str(input("Golongan ( A, B, C, D)    : "))

#ini untuk mengecek besarnya gaji berdasarkan inputan gol
if(gol == "A"):
    gaji = 10000000
    potongan = 2.5
elif(gol == "B"):
    gaji = 8500000
    potongan = 2.0
elif(gol == "C"):
    gaji = 7000000
    potongan = 1.5
elif(gol == "D"):
    gaji = 5500000
    potongan = 1.0
else : #untuk validasi inputan golongan
    print("Maaf Golongan Karyawan yang anda masukkan salah !")
    exit()

#ini rumus buat ngitung 
hasil = gaji*(100-potongan)/100 #buat ngitung gaji bersih
kali = gaji*potongan/100 #buat ngitung jumlah potongan

#ini buat nampilin output struk
print("")
print("===========================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("---------------------------")
print("Nama            : ", nama, "(Kode : ",kode, ")")
print("Golongan        : ", gol)
print("---------------------------")
print("Gaji Pokok      : Rp. ", gaji)
print("Potongan", potongan, "%", " : Rp. ", kali)
print("--------------------------- - ")
print("Gaji Bersih     : Rp. ", hasil)