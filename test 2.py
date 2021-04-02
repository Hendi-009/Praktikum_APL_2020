import os

angka = [4,2,0,6,9]

def bersihin_layar():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    bersihin_layar()
    print("MENU")
    print("Data = ", angka)
    print("[1] Tambah Data")
    print("[2] Ubah Data")
    print("[3] Hapus Data")
    print("[4] Urutkan Data")
    print("[5] Max dan Min Data")
    print("[6] Banyak Data")
    print("[0] Exit")

    pilih_menu = str(input("Pilih MENU : "))

    if (pilih_menu == "1"):
        bersihin_layar()
        print("[1] Menambah Elemen Di Indeks Tertentu")
        print("[2] Menambah Elemen Dari Belakang ")
        print("[3] Kembali")
        pilih_menu = str(input("Pilih : "))
        if (pilih_menu == "1"):
            insrt()
        elif (pilih_menu == "2"):
            bersihin_layar()
            print("[1] Satu Elemen")
            print("[2] Lebih Dari Satu Elemen")
            print("[3] Kembali")
            pilih_menu = str(input("Pilih : "))
            if (pilih_menu == "1"):
                apnd()
            elif (pilih_menu == "2"):
                extnd()
            elif (pilih_menu == "3"):
                balik_menu()
            else:
                print("Kamu memilih menu yang salah")
                balik_menu()
        elif (pilih_menu == "3"):
            balik_menu()
        else:
            print("Kamu memilih menu yang salah")
            balik_menu()
    elif (pilih_menu == "2"):
        bersihin_layar()
        print("[1] Ubah Elemen Didalam List")
        update_data(angka)
    elif (pilih_menu == "3"):
        bersihin_layar()
        print("[1] Hapus Semua Item Di List")
        print("[2] Hapus Item Menggunakan Indeks")
        print("[3] Hapus Item Menggunakan Elemen")
        print("[4] Kembali")
        pilih_menu = str(input("Pilih : "))
        if (pilih_menu == "1"):
            clr()
        elif (pilih_menu == "2"):
            pop()
        elif (pilih_menu == "3"):
            rmv()
        elif (pilih_menu == "4"):
            balik_menu()
        else:
            print("Kamu memilih menu yang salah")
            balik_menu()
    elif (pilih_menu == "4"):
        bersihin_layar()
        print("[1] Dari Terkecil")
        print("[2] Dari Terbesar")
        print("[3] Kembali")
        pilih_menu = str(input("Pilih : "))
        if (pilih_menu == "1"):
            ascen()
        elif (pilih_menu == "2"):
            descen()
        elif (pilih_menu == "3"):
            balik_menu()
        else:
            print("Kamu memilih menu yang salah")
            balik_menu()
    elif (pilih_menu == "5"):
        bersihin_layar()
        print("[1] Maximum")
        print("[2] Minimum")
        print("[3] Kembali")
        pilih_menu = str(input("Pilih : "))
        if (pilih_menu == "1"):
            Max()
        elif (pilih_menu == "2"):
            Min()
        elif (pilih_menu == "3"):
            balik_menu()
        else:
            print("Kamu memilih menu yang salah")
            balik_menu()
    elif (pilih_menu == "6"):
        bersihin_layar()
        print("[1] Banyak Elemen Didalam List")
        banyak_data()
    elif (pilih_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah")
        balik_menu()

def balik_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    menu()

#Nambah Data
def apnd():
    angka.append(int(input("Angka : ")))
    print(angka)
    balik_menu()

def extnd():
    list = []
    i = int(input("Masukkan jumlah elemen yang akan dimasukkan : "))
    while i > 0:
        angka_tambahan = (int(input("Angka : ")))
        list.append(angka_tambahan)
        i -= 1
    angka.extend(list)
    print(angka)
    balik_menu()

def insrt():
    indeks = int(input("Indeks: "))
    angka.insert(indeks, int(input("Angka : ")))
    print(angka)
    balik_menu()

#Edit Data
def update_data(angka):
    indeks = int(input("Indeks: "))
    angka[indeks] = int(input("Angka : "))
    print(angka)
    balik_menu()

#Hapus Data

def clr():
    angka.clear()
    print(angka)
    print("Semua data sudah dihapus")
    balik_menu()

def pop():
    indeks = int(input("Indeks: "))
    angka.pop(indeks)
    print(angka)
    balik_menu()

def rmv():
    angka.remove(int(input("Angka : ")))
    print(angka)
    balik_menu()

#Urut Data
def ascen():
    angka.sort()
    print(angka)
    balik_menu()

def descen():
    angka.reverse()
    print(angka)
    balik_menu()

#MaxMin

def Max():
    print(max(angka))
    balik_menu()

def Min():
    print(min(angka))
    balik_menu()

#Banyak Data
def banyak_data():
    print(len(angka))
    balik_menu()

menu()