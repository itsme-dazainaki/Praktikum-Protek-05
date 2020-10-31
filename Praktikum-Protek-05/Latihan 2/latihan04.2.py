#mari set nilai awal dari 2 variabel kita
kolom = 5
baris = 5

#ini bagian startnya
i = 0
while(i < baris):  #ini statement buat perulangannya
    j = 5
    while(j > i):
        print("*", end="") #ini perintahnya
        j-=1
    print(" ")
    i+=1 #ini increment

