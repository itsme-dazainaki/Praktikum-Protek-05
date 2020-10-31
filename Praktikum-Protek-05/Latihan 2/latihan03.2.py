#mari deklarasikan nilai awal dari variabel kita
#Start
a=0
tmb=0

#ini statement perulangannya
for b in range (0,100):
    if b % 2 == 1:
        a = a+1 #ini increment, bawahnya juga
        tmb = tmb+b
        print(b)

#ini buat menampilkan output       
print("Banyaknya Bilangan Ganjil (range 0 - 100): "+str(a))
print("Jumlah Seluruh Bilangan Ganjil : " + str(tmb))