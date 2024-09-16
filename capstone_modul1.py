# Mengimpor modul 'time' untuk mengambil waktu dari sistem
import time

# List untuk menyimpan data barang dan transaksi
barang_list = []
transaksi_list = []

# Fungsi untuk mendapatkan waktu saat ini (diambil dari sistem) dalam format YYYY-MM-DD HH:MM:SS
def get_current_time():
    # Menggunakan fungsi localtime() untuk mendapatkan waktu dari sistem
    current_time = time.localtime()
    # Mengubah waktu menjadi format string yang mudah dibaca
    return time.strftime("%Y-%m-%d %H:%M:%S", current_time)

# Fungsi untuk menambah barang baru ke dalam daftar barang
def create_menu():
    print("== Tambah Item Barang ==")
    
    while True:  # Loop untuk terus meminta input jika ID sudah ada
        id_barang = input("Masukkan ID Barang: ")
        
        # Cek apakah ID barang sudah ada di dalam barang_list
        id_ada = False
        for barang in barang_list:
            if barang["ID"].lower() == id_barang.lower():
                id_ada = True
                break
        
        # Jika ID sudah ada, berikan pesan dan opsi kepada pengguna
        if id_ada:
            print("ID barang sudah ada. Silakan masukkan ID berbeda.")
            pilihan = input("Tekan 'x' untuk membatalkan atau tekan Enter untuk mencoba lagi: ").lower()
            if pilihan == 'x':
                main_menu()  # Kembali ke menu utama jika pengguna memilih 'x'
                return  # Keluar dari fungsi create_menu()
        else:
            break  # Keluar dari loop jika ID barang belum ada
    
    # Lanjutkan dengan input data barang jika ID tidak duplikat
    nama_barang = input("Masukkan Nama Barang: ")
    kategori = input("Masukkan Kategori Barang: ")
    harga = float(input("Masukkan Harga Barang: "))
    stok = int(input("Masukkan Jumlah Stok: "))
    waktu_modifikasi = get_current_time()  # Mengambil waktu sistem saat barang ditambahkan
    
    # Membuat dictionary untuk menyimpan data barang
    barang = {
        "ID": id_barang,  # Kode Unik (Primary Key)
        "Nama": nama_barang,
        "Kategori": kategori,
        "Harga": harga,
        "Stok": stok,
        "Waktu Modifikasi": waktu_modifikasi,
        "Transaksi Terakhir": None  # Waktu asal diisi NULL/kosong dan akan diupdate waktu sistem saat transaksi terjadi
    }
    
    # Menambahkan barang ke dalam list barang_list
    barang_list.append(barang)
    print("Barang berhasil ditambahkan!")
    
    # Kembali ke menu utama
    main_menu()

# Fungsi untuk menampilkan semua barang yang ada
def read_menu():
    print("=== Daftar Barang ===")
    
    # Cek apakah daftar barang kosong
    if len(barang_list) == 0:
        print("Belum ada barang di inventori.")
    else:
        # Loop untuk menampilkan setiap barang
        for barang in barang_list:
            waktu_transaksi = barang["Transaksi Terakhir"] if barang["Transaksi Terakhir"] else "NULL"
            print("ID: {}, Nama: {}, Kategori: {}, Harga: {}, Stok: {}, Waktu Modifikasi: {}, Transaksi Terakhir: {}".format(
                barang['ID'], barang['Nama'], barang['Kategori'], barang['Harga'], barang['Stok'], barang['Waktu Modifikasi'], waktu_transaksi))
    
    # Kembali ke menu utama
    main_menu()

# Fungsi untuk mengupdate informasi barang
def update_menu():
    print("=== Update Barang ===")
    
    # Inputan pengguna memasukkan ID Barang
    id_barang = input("Masukkan ID Barang yang akan diupdate: ").lower()
    found = False  # Flag untuk cek apakah barang ditemukan
    
    for barang in barang_list:
        if barang["ID"].lower() == id_barang:
            print("Barang ditemukan: {}".format(barang))
            
            # Menampilkan pilihan bagian field yang akan diupdate
            print("Pilih field yang ingin diupdate:")
            print("1. Nama")
            print("2. Kategori")
            print("3. Harga")
            print("4. Stok")
            
            pilihan = input("Masukkan nomor field yang akan diupdate: ")
            
            if pilihan == "1":
                barang["Nama"] = input("Masukkan Nama Barang Baru: ")
                print("Nama barang berhasil diperbarui!")
            elif pilihan == "2":
                barang["Kategori"] = input("Masukkan Kategori Barang Baru: ")
                print("Kategori barang berhasil diperbarui!")
            elif pilihan == "3":
                barang["Harga"] = float(input("Masukkan Harga Barang Baru: "))
                print("Harga barang berhasil diperbarui!")
            elif pilihan == "4":
                barang["Stok"] = int(input("Masukkan Jumlah Stok Baru: "))
                print("Stok barang berhasil diperbarui!")
            else:
                print("Pilihan tidak valid.")
            
            # Update waktu modifikasi
            barang["Waktu Modifikasi"] = get_current_time()
            found = True
            break
    
    if not found:
        print("Barang tidak ditemukan.")
    
    main_menu()

# Fungsi untuk menghapus barang dari daftar
def delete_menu():
    print("=== Hapus Barang ===")
    
    id_barang = input("Masukkan ID Barang: ").lower()
    found = False
    
    for barang in barang_list:
        if barang["ID"].lower() == id_barang :
            barang_list.remove(barang)
            print("Barang berhasil dihapus!")
            found = True
            break
    
    if not found:
        print("Barang tidak ditemukan.")
    
    main_menu()

# Fungsi untuk mencari barang berdasarkan ID atau Nama Barang
def search_menu():
    print("=== Cari Barang ===")
    
    keyword = input("Masukkan ID atau Nama Barang: ").lower()
    found = False
    
    for barang in barang_list:
        if keyword in barang["ID"].lower() or keyword in barang["Nama"].lower():
            waktu_transaksi = barang["Transaksi Terakhir"] if barang["Transaksi Terakhir"] else "NULL"
            print("Barang ditemukan: ID: {}, Nama: {}, Kategori: {}, Harga: {}, Stok: {}, Waktu Modifikasi: {}, Transaksi Terakhir: {}".format(
                barang['ID'], barang['Nama'], barang['Kategori'], barang['Harga'], barang['Stok'], barang['Waktu Modifikasi'], waktu_transaksi))
            found = True
    
    if not found:
        print("Barang tidak ditemukan.")
    
    main_menu()

# Fungsi untuk melakukan transaksi penjualan
def transaksi_penjualan():
    print("=== Transaksi Penjualan ===")

    while True:  # Loop untuk meminta ID barang sampai barang ditemukan atau pengguna memilih keluar
        # Meminta pengguna memasukkan ID atau Nama Barang yang ingin dijual
        id_barang = input("Masukkan ID Barang ('x + enter' untuk batal): ").lower()
        
        if id_barang == 'x':  # Jika pengguna memilih 'x', keluar dari transaksi
            main_menu()
            return
        
        found = False  # Flag untuk cek apakah barang ditemukan
        
        for barang in barang_list:
            if barang["ID"].lower() == id_barang:
                # Menampilkan hanya Nama dan Harga barang
                print("Barang ditemukan:")
                print("Nama Barang: {}".format(barang['Nama']))
                print("Harga: {}".format(barang['Harga']))
                
                # Meminta jumlah yang ingin dijual dengan validasi stok
                while True:
                    jumlah_jual = input("Jumlah Item (Stok : {}, 'x + enter ' untuk batal): ".format(barang['Stok']))
                    
                    if jumlah_jual == 'x':  # Jika pengguna memilih 'x', keluar dari transaksi
                        main_menu()
                        return
                    
                    jumlah_jual = int(jumlah_jual)
                    
                    # Cek apakah stok mencukupi
                    if jumlah_jual > barang["Stok"]:
                        print("Stok tidak mencukupi! Silakan masukkan jumlah yang valid.")
                    else:
                        # Menghitung total harga
                        total_harga = jumlah_jual * barang["Harga"]
                        print("Total harga: {}".format(total_harga))
                        
                        # Meminta jumlah bayar dari pelanggan dan validasi sampai benar
                        while True:
                            jumlah_bayar = input("Jumlah bayar ('x + enter' untuk batal): ")
                            
                            if jumlah_bayar == 'x':  # Jika pengguna memilih 'x', keluar dari transaksi
                                main_menu()
                                return
                            
                            jumlah_bayar = float(jumlah_bayar)
                            
                            # Cek apakah jumlah bayar cukup
                            if jumlah_bayar < total_harga:
                                print("Jumlah bayar kurang! Periksa kembali pembayaran.")
                            else:
                                break  # Keluar dari loop jika jumlah bayar valid
                        
                        # Menghitung kembalian
                        kembalian = jumlah_bayar - total_harga
                        print("Transaksi berhasil!")
                        print("Kembalian: {}".format(kembalian))
                        
                        # Mengurangi stok barang
                        barang["Stok"] -= jumlah_jual
                        
                        # Update Transaksi Terakhir 
                        waktu_transaksi = get_current_time()
                        barang["Transaksi Terakhir"] = waktu_transaksi
                        
                        # Menambahkan data transaksi ke transaksi_list
                        transaksi = {
                            "ID Barang": barang["ID"],
                            "Nama Barang": barang["Nama"],
                            "Jumlah Terjual": jumlah_jual,
                            "Total Harga": total_harga,
                            "Jumlah Bayar": jumlah_bayar,
                            "Kembalian": kembalian,
                            "Waktu Transaksi": waktu_transaksi
                        }
                        transaksi_list.append(transaksi)
                        
                        found = True
                        break  # Keluar dari loop pencarian barang
        
        if found:
            break  # Keluar dari loop transaksi jika barang ditemukan dan transaksi berhasil
        else:
            print("Barang tidak ditemukan! Silakan coba lagi.")
    
    main_menu()
# Fungsi untuk menampilkan semua transaksi
def read_transaksi_menu():
    print("=== Daftar Transaksi ===")
    
    # Cek apakah ada transaksi
    if len(transaksi_list) == 0:
        print("Belum ada transaksi.")
    else:
        # Menampilkan data transaksi
        for transaksi in transaksi_list:
            print("ID Barang: {}, Nama Barang: {}, Jumlah Terjual: {}, Total Harga: {}, Jumlah Bayar: {}, Kembalian: {}, Waktu Transaksi: {}".format(
                transaksi['ID Barang'], transaksi['Nama Barang'], transaksi['Jumlah Terjual'], transaksi['Total Harga'], transaksi['Jumlah Bayar'], transaksi['Kembalian'], transaksi['Waktu Transaksi']))
    
    main_menu()

# Fungsi utama untuk menampilkan menu utama dan menerima input pilihan dari pengguna
def main_menu():
    print("\n=== Menu Utama ===")
    print("1. Tambah Barang")
    print("2. Daftar Barang")
    print("3. Update Barang")
    print("4. Hapus Barang")
    print("5. Cari Barang")
    print("6. Transaksi Penjualan")
    print("7. Daftar Transaksi")
    print("8. Keluar")
    
    # Meminta pengguna memilih menu
    pilihan = input("Masukkan pilihan Anda: ")
    
    if pilihan == "1":
        create_menu()
    elif pilihan == "2":
        read_menu()
    elif pilihan == "3":
        update_menu()
    elif pilihan == "4":
        delete_menu()
    elif pilihan == "5":
        search_menu()
    elif pilihan == "6":
        transaksi_penjualan()
    elif pilihan == "7":
        read_transaksi_menu()
    elif pilihan == "8":
        print("Aplikasi Penjualan Toko V.1.0")
        exit()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        main_menu()

# Menjalankan program
main_menu()
