import datetime
#dekarasi 
#inputan Inputan berupa Nama, tanggal hari ini, kode buah, kuantitas dalam kg
nama = ""
tanggal = datetime.datetime.now()
kodebuah =""
kuantitas = 0
keranjang = "Y"
#array dua d =>data belanjaan
databelanjaan = [ ["","",0,0,0] ]
#list/tuple daftar nama  buah dan harga
daftarbuah = [["MB001","ANGGUR", 112900],["MB002","MELON", 20000],["MB003","SEMANGKA", 13000],["MB004","APEL", 21000],["MB005","BUAH NAGA", 18000],["MB006","SAWO", 12000],["MB007","PEPAYA CALIFORNIA", 13000]]
#input data pel
nama = input("Nama Pelanggan : ")
print("Tanggal : ",tanggal)

#perulangan
while keranjang =="Y" :
    kodebuah = input("Kode Buah : ")
    kuantitas = int(input("kuantitas : "))
    # input pesanan
    # cek apakah kode ada dalam list/tuple
    for i in range(0,len(daftarbuah)):
        if(kodebuah==daftarbuah[i][0]):
            hargabuah = daftarbuah[i][2]
            totalhargabuah = kuantitas * daftarbuah[i][2]
        #jika ada hitung total harga buah
            #simpan data ke aray dua d  
            databelanjaan.append([kodebuah,daftarbuah[i][1],kuantitas,daftarbuah[i][2],totalhargabuah])
            break
    keranjang = input("Masih ada buah lainnya? (Y/N)")
#urutkan data
for i in range(1,len(databelanjaan)):
    for j in range(i+1, len(databelanjaan)):
        if(databelanjaan[i][4]> databelanjaan[j][4]):
            tmp = databelanjaan[i]
            databelanjaan[i] = databelanjaan[j]
            databelanjaan[j] = tmp
#tampilkan output
print("==================================")
print("======----Toko Buah Medan----=====")
print("==================================")
print("Nama Pelanggan : ",nama)
print("Tanggal : ", tanggal)
print("")
print("Daftar Belanjaan")
print("Kode Buah \t Nama buah \t Kuantitas \t Harga \t Total")
for i in range(1,len(databelanjaan)) :
    print(databelanjaan[i][0], "\t\t", databelanjaan[i][1], "\t",databelanjaan[i][2], "\t",databelanjaan[i][3], "\t", databelanjaan[i][4], "\t")