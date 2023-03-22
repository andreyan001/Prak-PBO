class Robot:
    jumlah_turn = 0
    a = 0
    b = 0
    c = 0

    def __init__(self, nama, health, damage):
        self.nama = nama
        self.health = health
        self.damage = damage

    def lakukan_aksi(self, nama):
        self.jumlah_turn += 1
        if nama == "Antares" :
            self.a += 1
            if self.a < 3:
                self.damage = 5000
            elif self.a == 3:
                self.damage *= 1.5
                self.a = 0

        elif nama == "Alphasetia" :
            self.b += 1
            if self.b == 2:
                self.health += 4000
                print("Alphasetia menambah darah sebanyak 4000 HP")
                self.b = 0

        elif nama == "Lecalicus" :
            self.c += 1
            if self.c < 4:
                self.damage = 5500
            elif self.c == 4:
                self.damage *= 2
                print("Lecalicus menambah darah sebanyak 7000 HP")
                self.health += 7000
                self.c = 0

    def terima_aksi(self, nama, damage):
        self.health -= damage
        print(f"{nama} menerima serangan sebanyak {damage}")
        if self.health <= 0:
            print(f"{nama} telah kalah")

class Antares(Robot):
    def __init__(self, nama, health, damage):
        super().__init__(nama, health, damage)

class Alphasetia(Robot):
    def __init__(self, nama, health, damage):
        super().__init__( nama, health, damage)

class Lecalicus(Robot):
    def __init__(self, nama, health, damage):
        super().__init__( nama, health, damage)

def match(robot1, robot2):
    sum = 1
    while True:
        if robot1.health <= 0:
            print(f"Robot lawan {robot2.nama} menang")
        elif robot2.health <= 0:
            print(f"Robotmu {robot1.nama} menang")

        if robot1.health <= 0 or robot2.health <= 0:
            break

        print(f"Turn saat ini : {sum}")
        print(f"Robotmu ({robot1.nama} - {robot1.health} HP), robot lawan ({robot2.nama} - {robot2.health} HP)")

        print("Selanjutnya, pilih 1 untuk batu, 2 untuk kertas, dan 3 untuk gunting")
        opsi1 = int(input(f"Pilih tangan robotmu ({robot1.nama}) : "))
        opsi2 = int(input(f"Pilih tangan robot lawan ({robot2.nama}) : "))

        if(opsi1 == 1):
            if(opsi2 == 1):
                print("Kedua robot seimbang")
                sum += 1
            elif(opsi2 == 2):
                R2.lakukan_aksi(R2.nama)
                print(f"Robot lawan {R2.nama} menyerang sebanyak {R2.damage}")
                R1.terima_aksi(R1.nama, R2.damage)
                sum += 1
            else:
                R1.lakukan_aksi(R1.nama)
                print(f"Robotmu {R1.nama} menyerang sebanyak {R1.damage}")
                R2.terima_aksi(R2.nama, R1.damage)
                sum += 1
            print("\n")
        elif(opsi1 == 2):
            if(opsi2 == 1):
                R1.lakukan_aksi(R1.nama)
                print(f"Robotmu {R1.nama} menyerang sebanyak {R1.damage}")
                R2.terima_aksi(R2.nama, R1.damage)
                sum += 1
            elif(opsi2 == 2):
                print("Kedua robot seimbang")
                sum += 1
            else:
                R2.lakukan_aksi(R2.nama)
                print(f"Robot lawan {R2.nama} menyerang sebanyak {R2.damage}")
                R1.terima_aksi(R1.nama, R2.damage)
                sum += 1
            print("\n")
        elif(opsi1 == 3):
            if(opsi2 == 1):
                R2.lakukan_aksi(R2.nama)
                print(f"Robot lawan {R2.nama} menyerang sebanyak {R2.damage}")
                R1.terima_aksi(R1.nama, R2.damage)
                sum += 1
            elif(opsi2 == 2):
                R1.lakukan_aksi(R1.nama)
                print(f"Robotmu {R1.nama} menyerang sebanyak {R1.damage}")
                R2.terima_aksi(R2.nama, R1.damage)
                sum += 1
            else:
                print("Kedua robot seimbang")
                sum += 1
            print("\n")


print("Selamat datang di pertandingan robot Yamako")
robotmu = int(input("Pilih robotmu     (1 = Antares, 2 = Alphasetia, 3 = Lecalicus) : "))
if robotmu == 1:
    R1 = Antares("Antares", 50000, 5000)
elif robotmu == 2:
    R1 = Alphasetia("Alphasetia", 40000, 6000)
else:
    R1 = Lecalicus("Lecalicus", 45000, 5500)
    
robot_lawan = int(input("Pilih robot lawan (1 = Antares, 2 = Alphasetia, 3 = Lecalicus) : "))
if robot_lawan == 1:
    R2 = Antares("Antares", 50000, 5000)
elif robot_lawan == 2:
    R2 = Alphasetia("Alphasetia", 40000, 6000)
else:
    R2 = Lecalicus("Lecalicus", 45000, 5500)

print("\n")
match(R1, R2)
