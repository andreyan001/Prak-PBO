class AkunBank:
    list_pelanggan = []

    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.list_pelanggan.append(self)
        self.__no_pelanggan = no_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo
    
    def lihat_menu(self):
        print("Halo ", self.__nama_pelanggan, "", "Berikut list menu yang tersedia")
        print("1. Lihat Saldo")
        print("2. Tarik Tunai")
        print("3. Transfer")
        print("4. Keluar")
    
    def lihat_saldo(self):
        print(f"Halo {self.__nama_pelanggan} saldo yang anda punya yaitu sebesar {self.__jumlah_saldo}")
    
    def tarik_tunai(self):
        opsi1 = False
        while(not opsi1):
            tarik = int(input("Masukkan jumlah saldo yang ingin ditarik : "))
            if(self.__jumlah_saldo > tarik):
                self.__jumlah_saldo -= tarik
                print("Saldo berhasil ditarik")
                opsi1 = True
            else: 
                print("Saldo yang anda miliki tidak cukup!")
    
    def transfer(self):
        sum_tf = int(input("Masukkan jumlah saldo yang ingin ditransfer : "))
        norek = int(input("Masukkan nomor rekening tujuan : "))
        cek = 0

        for i in self.list_pelanggan:
            if(norek == self.__no_pelanggan):
                cek = 3
            elif(norek == i.__no_pelanggan):
                if(sum_tf > self.__jumlah_saldo):
                    cek = 2
                else:
                    cek = 0
                    self.__jumlah_saldo -= sum_tf
                break
            elif(norek != i.__no_pelanggan):
                cek = 1
        
        if(cek == 1):
            print("Nomor rekening tujuan tidak dikenal!")
            cek = 0
        elif(cek == 2):
            print("Saldo yang anda miliki tidak cukup untuk melakukan transfer!")
            cek = 0
        elif(cek == 3):
            print("Nomor rekening tujuan yang anda masukkan adalah nomor rekening saat ini!")
            cek = 0
        else:
            print(f"Transfer saldo sebesar {sum_tf} ke {norek} berhasil!")
            cek = 0
    
Akun1 = AkunBank(1234, "Andreyan", 5000000000)
Akun2 = AkunBank(2345, "Ukraina", 6666666666)
Akun3 = AkunBank(3456, "Elon Musk", 9999999999)

Akun1.lihat_menu()
menu = int(input("Silahkan pilih : "))

opsi2 = False
while(not opsi2):
    if (menu == 1):
        Akun1.lihat_saldo()
        print("\n")
        Akun1.lihat_menu()
        menu = int(input("Pilih menu : "))
        print("\n")
    elif(menu == 2):
        Akun1.tarik_tunai()
        print("\n")
        Akun1.lihat_menu()
        menu = int(input("Pilih menu : "))
        print("\n")
    elif(menu == 3):
        Akun1.transfer()
        print("\n")
        Akun1.lihat_menu()
        menu = int(input("Pilih menu : "))
        print("\n")
    elif(menu == 4):
        opsi2 = True
    else:
        menu = int(input("Pilih menu : "))
        print("\n")









