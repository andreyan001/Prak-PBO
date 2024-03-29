class Komputer:
    def __init__(self, nama, jenis, harga, merk):
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
        self.merk = merk

class Processor(Komputer):
    def __init__(self, nama, jenis, harga, merk, jumlah_core, kecepatan_processor):
        super().__init__(nama, jenis, harga, merk)
        self.jumlah_core = jumlah_core
        self.kecepatan_processor = kecepatan_processor

    def tampil(self):
        print(f"Processor {self.jenis} produksi {self.nama}")

class RAM(Komputer):
    def __init__(self, nama, jenis, harga, merk, kapasitas_ram):
        super().__init__(nama, jenis, harga, merk)
        self.kapasitas_ram = kapasitas_ram

    def tampil(self):
        print(f"RAM {self.jenis} produksi {self.nama}")

class HDD(Komputer):
    def __init__(self, nama, jenis, harga, merk, kapasitas_hdd, rpm):
        super().__init__(nama, jenis, harga, merk)
        self.kapasitas_hdd = kapasitas_hdd
        self.rpm = rpm

    def tampil(self):
        print(f"SATA HDD {self.jenis} produksi {self.nama}")

class VGA(Komputer):
    def __init__(self, nama, jenis, harga, merk, kapasitas_vga):
        super().__init__(nama, jenis, harga, merk)
        self.kapasitas_vga = kapasitas_vga

    def tampil(self):
        print(f"VGA {self.jenis} produksi {self.nama}")

class PSU(Komputer):
    def __init__(self, nama, jenis, harga, merk, daya):
        super().__init__(nama, jenis, harga, merk)
        self.daya = daya

    def tampil(self):
        print(f"PSU {self.jenis} produksi {self.nama}")


p1 = Processor('Intel', 'Core i7 7740X', 4350000, 4, '4.3GHz')
ram1 = RAM('V-Gen','DDR4 SODimm PC19200/2400MHz',328000, 'x', '4GB')
hdd1 = HDD('Seagate','HDD 2.5 inch',295000, 'x','500GB',7200)
vga1 = VGA('Asus','VGA GTX 1050',250000, 'x', '2GB')
psu1 = PSU('Corsair','Corsair V550',250000, 'x', '500W')

print("\n")
p1.tampil()
ram1.tampil()
hdd1.tampil()
vga1.tampil()
psu1.tampil()
print("\n")