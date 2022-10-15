
#deklarasi
nama_pelanggan = ""
status_member = "tidak"
total_belanja = 0
diskon_persen = "0%"
diskon_harga = 0
total_bayar = 0
inputLagi = "Y"

#PROGRAM 
while inputLagi in "Y":
    inputLagi = "N"
    nama_pelanggan = input("Nama Pelanggan : ")
    status_member = input("Status Member (Ya/Tidak) : ")
    total_belanja = int(input("Total Belanja dalam Rp. : "))
    
    if status_member in "Ya":
        if total_belanja < 100000:
            diskon_persen = "1%"
            diskon_harga = int((1/100) * total_belanja)
        elif total_belanja < 1000000 :
            diskon_persen = "5%"
            diskon_harga = int((5/100) * total_belanja)
        elif total_belanja > 1000000 :
            diskon_persen = "10%"
            diskon_harga = int((10/100) * total_belanja)
            if diskon_harga > 100000:
                diskon_harga = 100000
        else:
            diskon_harga = 0
            diskon_persen = "0%"
    elif status_member in "Tidak":
        if total_belanja < 100000:
            diskon_persen = "0%"
            diskon_harga = 0
        elif total_belanja < 1000000 :
            diskon_persen = "1%"
            diskon_harga = int((1/100) * total_belanja)
        elif total_belanja > 1000000 :
            diskon_persen = "3%"
            diskon_harga = int((3/100) * total_belanja)
            if diskon_harga > 100000:
                diskon_harga = 100000
        else:
            diskon_harga = 0
            diskon_persen = "0%"

    total_bayar = total_belanja - diskon_harga
    print("Diskon = ", diskon_persen)
    print("Diskon (Rp) = ",diskon_harga)
    print("Total Bayar = ", total_bayar)
    
    inputLagi = input("Input Lagi (Y/N) : ")

