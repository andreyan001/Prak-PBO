class Mahasiswa:
    #atribut global
    prodi = "Teknik Informatika"

    def __init__(self, nama, nim, umur, alamat):
        #atribut publik
        self.nama = nama
        self.nim = nim

        #atribut protected
        self._umur = umur

        #atribut private
        self.__alamat = alamat


    def get_umur(self):
        return self._umur
    
    #fungsi protected
    def set_umur(self, x):
        self._umur = x
    
    #fungsi private
    def set_alamat(self, x):
        self.__alamat = x
    
    #instance private
    def get_alamat(self):
        return self.__alamat
    
    def bio(self):
        print("Nama : ", self.nama)
        print("NIM  : ", self.nim)
        print("Umur : ", self.get_umur())
        print("Prodi  : ", self.prodi)
        print("Alamat : ", self.get_alamat())
        print("")

#objek untuk class
Mhs1 = Mahasiswa("Andreyan", 186, 19, "Lampung")
Mhs1.bio()

#akses atribut kelas
print("Program Studi : ", Mhs1.prodi, "\n")

#akses atribut instance kelas
print("Nama : ", Mhs1.nama)
print("NIM  : ", Mhs1.nim, "\n")

#ubah atribut instance protected
Mhs1.set_umur(20)
#akses atribut instance protected
print("Umur : ", Mhs1.get_umur(), "\n")

#ubah atribut instance private
Mhs1.set_alamat("Bangka")
#akses atribut instance private
print("Alamat : ", Mhs1.get_alamat(), "\n")

Mhs1.bio()
    

