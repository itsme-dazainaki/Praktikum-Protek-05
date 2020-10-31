#mari mendeklarasikan variabel 
a = 0

#ini buat ?
from random import randint

#ini perulangannya
while True:
    a = a + 1 #ini incrementnya
    bil = randint(0,10)
    print(bil)
    if bil == 5:
        break

#ini buat menampilkan output si a
print("Jumlah Perulangan : ", a)