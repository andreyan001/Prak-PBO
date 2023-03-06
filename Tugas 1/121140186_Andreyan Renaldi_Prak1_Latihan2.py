# Nama : Andreyan Renaldi
# NIM : 121140186

username = ("informatika")
password = ("12345678")
max = 3

for i in range (max):
    inUsername = input("Masukkan username : ")
    inPassword = input("Masukkan password : ")

    if(inUsername == username and inPassword == password):
        print("Login Berhasil!")
        break
    elif(inUsername != username or inPassword != password):
        if(i<2):
            print("Login Gagal!!")
            print("Coba Lagi")
            print("")
        else:
            print("Akun anda telah diblokir")
    