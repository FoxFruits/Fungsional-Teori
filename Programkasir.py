barang = [
    {'id': 'B001', 'nama': 'Mouse', 'stok': 10, 'harga': 5000},
    {'id': 'B002', 'nama': 'Keyboard', 'stok': 5, 'harga': 5000},
    {'id': 'B003', 'nama': 'Monitor', 'stok': 7, 'harga': 20000}
]

akun = {
    'penjual': {
        'password': '123digimon',
        'nama': 'Elang',
        'email': 'elang@gmail.com',
        'role': 'penjual'
    }, 
    'pembeli' : {
        'password': '12elangjelek',
        'nama': 'Buyer',
        'email': 'pembeli@gmail.com',
        'role': 'pembeli',
        'keranjang': []
    }
}


def register():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if username in akun:
        print("User sudah ada.")
        return False
    else:
        akun[username] = {
            'password': password,
            'nama': '',
            'email': '',
            'role': ''
        }
        print("Registrasi berhasil.")
        return username

def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if username in akun and akun[username]['password'] == password:
        print("Login berhasil")
        if akun[username]['role'] == 'penjual':
            display_menu_penjual(username)
        else:
            display_menu_pembeli(username)
    else:
        print("username atau password tidak valid. Silahkan Ulangi")
        
def tambah_barang(username):
    if akun[username]['role'] == 'penjual':
        print("\nTambah Barang\n")
        id_barang = input("Masukkan id barang: ")
        nama = input("Masukkan nama barang: ")
        stok = int(input("Masukkan stok barang: "))
        harga = float(input("Masukkan harga barang: "))

        for barang in barang:
            if barang['id'] == id_barang:
                print("ID barang sudah ada. Silakan coba lagi.")
                return

        barang_baru = {'id': id_barang, 'nama': nama, 'stok': stok, 'harga': harga}
        barang.append(barang_baru)
        print(f"Barang '{nama}' berhasil ditambahkan.")
    else:
        print("Anda tidak memiliki akses untuk menambahkan barang.")
        
def update_barang(username):
    if akun[username]['role'] == 'penjual':
        print("\nUpdate Barang\n")
        id_barang = input("Masukkan id barang: ")
        for i, barang in enumerate(barang):
            if barang['id'] == id_barang:
                stok = int(input("Masukkan stok baru: "))
                barang['stok'] = stok
                print(f"Stok barang '{barang['nama']}' berhasil diupdate.")
                return
        print("ID barang tidak valid.")
    else:
        print("Anda tidak memiliki akses untuk mengupdate barang.")
        
def hapus_barang(username):
    if akun[username]['role'] == 'penjual':
        print("\nHapus Barang\n")
        id_barang = input("Masukkan id barang: ")
        for i, barang in enumerate(barang):
            if barang['id'] == id_barang:
                del barang[i]
                print(f"Barang '{barang['nama']}' berhasil dihapus.")
                return
        print("ID barang tidak valid.")
    else:
        print("Anda tidak memiliki akses untuk menghapus barang.")
        
def lihat_barang_pembeli(username):
    global barang
    if akun[username]['role'] == 'pembeli':
        print("Daftar Barang:")
        for barang in barang:
            if barang['stok'] > 0:
                print(f"ID Barang: {barang['id']} | Nama Barang: {barang['nama']} | Stok: {barang['stok']} | Harga: Rp {barang['harga']}")
    else:
        print("Anda tidak memiliki akses untuk melihat daftar barang.")
        
def beli_barang(username):
    if akun[username]['role'] == 'pembeli':
        print("Daftar Barang:")
        for barang in barang:
            if barang['stok'] > 0:
                print(f"ID Barang: {barang['id']} | Nama Barang: {barang['nama']} | Stok: {barang['stok']} | Harga: Rp {barang['harga']}")
        id_barang = input("Masukkan ID barang yang ingin dibeli: ")
        for barang in barang:
            if barang['id'] == id_barang and barang['stok'] > 0:
                if barang not in akun[username]['keranjang']:
                    akun[username]['keranjang'].append({'id': barang['id'], 'nama': barang['nama'], 'harga': barang['harga']})
                    barang['stok'] -= 1
                    print(f"Barang '{barang['nama']}' berhasil dibeli.")
                else:
                    print("Anda sudah membeli barang ini.")
                return
        print("ID barang tidak valid atau stok habis.")
    else:
        print("Anda tidak memiliki akses untuk membeli barang.")

def display_menu_penjual(username):
    while True:
        print("Menu Penjual:")
        print("1. Tambah Barang")
        print("2. Update Barang")
        print("3. Hapus Barang")
        print("4. Logout")
        choice = input("Pilih: ")
        if choice == "1":
            tambah_barang(username)
        elif choice == "2":
            update_barang(username)
        elif choice == "3":
            hapus_barang(username)
        elif choice == "4":
            print("Berhasil Logout")
            break
        else:
            print("Pilihan tidak valid. Ulangi.")

def display_menu_pembeli(username):
    while True:
        print("Menu Pembeli:")
        print("1. Lihat Barang")
        print("2. Beli Barang")
        print("3. Lihat Keranjang")
        print("4. Logout")
        choice = input("Pilih: ")
        if choice == "1":
            lihat_barang_pembeli(username)
        elif choice == "2":
            beli_barang(username)
        elif choice == "3":
            lihat_barang_pembeli(username)
        elif choice == "4":
            print("Berhasil Logout")
            break
        else:
            print("Pilihan tidak valid. Ulangi.")

def main():
    while True:
        print("Login Menu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Pilih: ")
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Pilihan tidak valid. Ulangi.")
        
if __name__ == "__main__":
    main()