#Farrel Alifah Raihan
#03081220042
#Program tahun kabisat
print('Program untuk menentukan tahun kabisat atau tidak.')
tahun = int(input("Masukkan tahun: "))


if tahun % 400 == 0:
    print(tahun , 'merupakan tahun kabisat')
elif tahun % 100 == 0:
    print(tahun , 'bukan merupakan tahun kabisat')
elif tahun % 4 == 0:
    print(tahun , 'merupakan tahun kabisat')
else:
    print(tahun , "bukan merupakan tahun kabisat")

    