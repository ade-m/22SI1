
def hitungUpahPerJam(golongan):
    upahperjam =0
    if golongan in "A" :
        upahperjam =6000
    elif golongan in "B" :
        upahperjam =7500
    elif golongan in "C" :
        upahperjam =9000
    elif golongan in "D" :
        upahperjam =11000
    return upahperjam

def hitungUpah(jamkerja,upahperjam,nama,golongan):
    if jamkerja>48 :
        uangLembur = (jamkerja-48)*5000
        #jamkerja=48
        upah = (48*jamkerja)+uangLembur
    else :
        upah = (upahperjam*jamkerja)+uangLembur
    print("Upah \t:\t",upah)
    return [nama,golongan,jamkerja,upah]

#deklarasi
nama=""
golongan=""
jamkerja=0
upah=0
uangLembur=0
gaji=0
upahperjam=0
inputLagi=True
data = []
while inputLagi:
    #inputan
    nama= input("Nama \t\t:\t")
    golongan= input("Golongan \t:\t")
    jamkerja= int(input("Jam Kerja \t:\t"))

    #program kuis
    #hitung Upah per jam
    upahperjam = hitungUpahPerJam(golongan)
    
    data.append(hitungUpah(jamkerja,upahperjam,nama,golongan))
    tanya= input("Apakah ingin input lagi? (Y/T)")
    if tanya == "T" or tanya == "t" :
        inputLagi= False
print(data)