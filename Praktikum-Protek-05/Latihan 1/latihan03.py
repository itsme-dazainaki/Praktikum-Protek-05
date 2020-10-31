#mari menginput, ini variabelnya sekalian ditulis type data inputannya
bi = int(input("Masukkan nilai Bahasa Indonesia : "))
ipa = int(input("Masukkan nilai IPA              : "))
mat = int(input("Masukkan nilai Matematika       : "))

#ini buat ngecek validasi inputan diatas dan nampilin pesan error
if(bi<0) or (bi>100) or (ipa<0) or (ipa>100) or (mat<0) or (mat>100):
    print("Nilai yang anda inputkan tidak valid")
    exit

#ini buat ngecek inputan tadi sesuai kondisi, nanti dia statusnya lulus atau tidak
elif(bi >=60) and (bi<=100) and (ipa>=60) and (ipa<100) and (mat>=70) and (mat<100):
    print("Status Kelulusan                : LULUS")
elif(bi>=0) or (bi<60) or (ipa>=0) or (ipa<60) or (mat>=0) or (mat<70):
    print("Status Kelulusan                : TIDAK LULUS")
    print("Sebab                :   ") #ini sampe bawah buat ngecek, alasan dia gak lulus, nilainya kurang dimana aja
    if(bi<60):
        print("Nilai Bahasa Indonesia anda kurang dari 60")
    if(mat<60):
        print("Nilai Matematika anda kurang dari 70")
    if(ipa<60):
        print("Nilai IPA anda kurang dari 60")
