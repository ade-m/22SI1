N = 2
i = 1

while i<=N :
    nama_barang = input("Nama Barang = ")
    jenis_barabg = input("Jenis Barang. -")
    if jenis_barabg in "ATK":
        diskon = "2%"
    elif jenis_barabg in "Snack":
        diskon = "5%"
    else:
        diskon = "0%"
    print("Diskom = ", diskon)
    i+=1
