#mari menginput, variabel beserta type dan inputannya
kode = int(input("Masukkan Kode Karyawan : "))
nama = str(input("Masukkan Nama Karyawan : "))
gol  = str(input("Masukkan Golongan ( A, B, C, D)    : "))
status = str(input("Status (1 = Menikah / 2 = Belum) : "))
#ini buat validasi status, kalo valid ada inputan lagi, kalo gak valid nanti statusnya berubah keterangan 
if (status == "1"):
        status1 = "Menikah"
        anak =int(input("Masukkan Jumlah anak (0 jika tidak punya) : "))
elif (status == "2"):
    status1 = "Belum Menikah"

#ini untuk mengecek besarnya gaji berdasarkan inputan gol
if(gol == "A") :
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

else :  #untuk validasi inputan golongan
    print("Maaf input yang anda masukkan salah !")
    exit()

#mari deklarasikan nilai awal dari 2 buah variabel
tnjnikah = 0
tnjanak = 0

#ini rumus tunjangan buat yang memenuhi kondisi
if(status=="1"):
    tnjnikah = gaji/10
    tnjanak = anak*(gaji/20)

#-ini rumus buat ngitung 
kotor  = gaji+tnjnikah+tnjanak #ngitung gaji kotor
jpot= gaji*potongan/100 #ini buat ngitung jumlah potongan
bersih = kotor-jpot #buat ngitung gaji bersih

#ini buat nampilin output
print("")
print("===========================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("---------------------------")
print("Nama          : ", nama, "(Kode : ",kode, ")")
print("Golongan      : ", gol)
print("Status        : ", status1)
if (status == "1"): #buat ngecek status, kalo memenuhi bakal ada output tambahan
        print("Jumlah Anak   : ", anak)
print("---------------------------")
print("")            
print("Gaji Pokok            : Rp. ", gaji)
print("Tunjangan Suami/Istri : Rp. ", int(tnjnikah))
print("Tunjangan Anak        : Rp. ", int(tnjanak))
print("--------------------------- +")
print("")
print("Gaji Kotor            : Rp. ", int(kotor))
print("Potongan ", potongan,"%"      "       : Rp. ",int(jpot))
print("---------------------------")
print("")
print("Gaji Bersih           : Rp. ", int(bersih))
