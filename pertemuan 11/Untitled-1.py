
#dekarasi 
#inputan
#array dua d =>data belanjaan
#list/tuple daftar nama  buah dan harga

#input data pel
#perulangan
    # input pesanan
    # cek apakah kode ada dalam list/tuple
    #jika ada hitung total harga buah
        #simpan data ke aray dua d

#urutkan data
#tampilkan output

import turtle,random
def hati(n):
    warna = ["red","green","blue","pink"]
    if(n>0):
        love =  turtle.Turtle()
        love.color(warna[n%4])
        #love.color(random.choice(warna))
        love.left(50+n*2)
        love.forward(100+n*2)
        love.circle(40+n*2,180)
        love.left(260+n*2)
        love.circle(40+n*2,180)
        love.forward(100+n*2)
        hati(n-1)

n= int(input("Mau berapa kali? "))
window = turtle.Screen()
window.bgcolor("black")
hati(n)
carver = turtle.Turtle()
love.done()
