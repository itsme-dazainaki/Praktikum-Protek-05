#mari menginput, ini variabelnya sekalian ditulis type data inputannya
bi = int(input("Masukkan nilai Bahasa Indonesia : "))
ipa = int(input("Masukkan nilai IPA              : "))
mat = int(input("Masukkan nilai Matematika       : "))

#ini buat ngecek inputan tadi sesuai kondisi, nanti dia statusnya lulus atau tidak
if(bi >=60) and (bi<=100) and (ipa>=60) and (ipa<100) and (mat>=70) and (mat<100):
    print("Status Kelulusan                : LULUS")
elif(bi>=0) or (bi<60) or (ipa>=0) or (ipa<60) or (mat>=0) or (mat<70):
    print("Status Kelulusan                : TIDAK LULUS")
