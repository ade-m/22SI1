nama = input("Nama Pelanggan : ")
pesanan = input("Pesanan    :")
totalbelanja = int(input("Total Belanja :"))
diskon = 0
if("Agus" in nama) or ("agus" in nama) or ("AGUS" in nama):
    if(pesanan in "kopi tubruk") or (pesanan in "Kopi Tubruk") or (pesanan in "Kopi tubruk") or (pesanan in "kopi Tubruk") or (pesanan in "KOPI TUBRUK") :
        diskon = ((70/100) * totalbelanja)
        print("Diskon   : Promo Agus 70%")
    elif (pesanan in "Roti sobek") or (pesanan in "Roti Sobek") :
        diskon = ((40/100) * totalbelanja)
        print("Diskon   : Promo Agus 40%")
print("Diskon (IDR) :",diskon)
totalbayar = totalbelanja - diskon
print("Total Bayar(IDR) :",totalbayar)