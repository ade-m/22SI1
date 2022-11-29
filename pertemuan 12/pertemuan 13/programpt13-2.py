
#1 tampilkan data
#2 tambah data
#3 edit data
#4 hapus data
#5 exit

def tampilkanData(dataBelanjaan):
    print("Data Belanjaan")
    print("[Kode Barang]\tNama Barang\tQTY\tTotal")
    for i in range(1,len(dataBelanjaan)):
        print("[",dataBelanjaan[i][0],"]\t",dataBelanjaan[i][1],"\t\t",dataBelanjaan[i][2],"Kg\tIDR. ",dataBelanjaan[i][3])

def tambahData(dataBelanjaan):
    print("Penambahan Data")
    #deklarasi
    kodeBrg=""
    namaBrg=""
    qty=0
    totalharga=0
    #input data
    kodeBrg = input("Kode Barang\t:\t")
    namaBrg = input("Nama Barang\t:\t")
    qty = input("Qty\t:\t")
    totalharga = input("Total\t:\t")
    #tambahkan kedalam data belanjaan
    dataBelanjaan.append([kodeBrg,namaBrg,qty,totalharga])

def editData(dataBelanjaan):
    print("Edit Data")

def hapusData(dataBelanjaan):
    print("Hapus satu data")
    pilih = -1
    tampilkanData(dataBelanjaan)
    pilih = int(input("Pilih Data yang akan di hapus : "))
    dataBelanjaan.pop(pilih)
    tampilkanData(dataBelanjaan)
def exit():
    print("Sampai Jumpa Lagi...")

def menu():
    print("-----------Menu------------")
    print("1. Tampilkan Data Keranjang Belanjaan")
    print("2. Tambah Data Belanjaan")
    print("3. Edit Data Belanjaan")
    print("4. Hapus Data Belanjaan")
    print("5. Exit")

#deklarasi
namaPelanggan =""
pilihanMenu= 1
dataBelanjaan=[["Kode Barang","Nama Barang", 0,0]]
print("Toko Kelontong Medan Berkah")
namaPelanggan = input("Masukkan Nama Pelanggan\t:\t")

while(pilihanMenu!=5) :
    menu()
    #terima input menu dari user
    pilihanMenu = int(input("Pilih Menu\t:\t"))

    #percabangan pilih menu
    if (pilihanMenu==1) :
        tampilkanData(dataBelanjaan)
    elif(pilihanMenu==2) :
        tambahData(dataBelanjaan)
    elif(pilihanMenu==3) :
        editData(dataBelanjaan)
    elif(pilihanMenu==4) :
        hapusData(dataBelanjaan)
    elif(pilihanMenu==5) :
        exit()
    else:
        menu()