
#deklarasi
hasil = 0
rata2 = 0
inputLagi = "Y"
jlh_data = 0

#PROGRAM 
while inputLagi in "Y":
    inputLagi = "N"
    angka = int(input("masukkan angka : "))
    hasil += angka
    jlh_data += 1
    inputLagi = input("Input Lagi (Y/N) : ")

print("Hasil penjumlahan adalah ", hasil)
print("rata-rata = ", hasil/jlh_data)
