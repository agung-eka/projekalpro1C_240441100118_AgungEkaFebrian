from datetime import datetime, timedelta

# Daftar buku yang tersedia di perpustakaan
nama_buku = [
    "Hidup Manis Ala Rasulullah", "Sabar Menghadapi Cobaan", "Jalur Langit", 
    "Gak Bisa Yura Aku Capek", "Laskar Pelangi", 
    "The Alchemist", "Atomic Habits", "To Kill a Mockingbird", 
    "Pride and Prejudice", "The Great Gatsby"
]
harga_buku = [50000, 60000, 55000, 45000, 70000, 85000, 95000, 78000, 72000, 83000]
kode_buku = [879, 698, 756, 987, 860, 101, 102, 103, 104, 105]
penerbit_buku = [
    "Ratnani", "Bilif Abdullah", "Hiliyah", "Ust.Hanan Ataki", "Bintang Samudra",
    "HarperCollins", "Penguin Random House", "Harper Lee Estate", 
    "Vintage Classics", "Scribner"
]

# Menggabungkan semua informasi buku ke dalam daftar tuple
buku_tersedia = list(zip(nama_buku, harga_buku, kode_buku, penerbit_buku))

# Dictionary untuk menyimpan data peminjaman
peminjaman = {}

def tampilkan_buku():
    """Menampilkan daftar buku yang tersedia beserta ID buku."""
    print("\nDaftar Buku Tersedia:")
    print("ID Buku | Judul Buku                     | Penerbit")
    print("---------------------------------------------------")
    for buku in buku_tersedia:
        print(f"{buku[2]:<7} | {buku[0]:<30} | {buku[3]}")

def tampilkan_harga_buku():
    """Menampilkan daftar harga buku berdasarkan ID buku dan judulnya."""
    print("\nDaftar Harga Buku:")
    print("ID Buku | Judul Buku                     | Harga")
    print("---------------------------------------------------")
    for buku in buku_tersedia:
        print(f"{buku[2]:<7} | {buku[0]:<30} | Rp {buku[1]}")

def pinjam_buku(nama_anggota, id_buku, tanggal_peminjaman):
    """Memproses peminjaman buku berdasarkan ID buku."""
    for buku in buku_tersedia:
        if buku[2] == id_buku:
            if nama_anggota in peminjaman:
                peminjaman[nama_anggota].append((buku, tanggal_peminjaman))
            else:
                peminjaman[nama_anggota] = [(buku, tanggal_peminjaman)]
            buku_tersedia.remove(buku)
            print(f"{nama_anggota} berhasil meminjam buku '{buku[0]}' pada tanggal {tanggal_peminjaman}.")
            return
    print(f"Buku dengan ID {id_buku} tidak tersedia.")

def kembalikan_buku(nama_anggota, id_buku, tanggal_pengembalian):
    """Memproses pengembalian buku dengan menghitung keterlambatan dan denda."""
    if nama_anggota in peminjaman:
        for i, (buku, tanggal_peminjaman) in enumerate(peminjaman[nama_anggota]):
            if buku[2] == id_buku:
                peminjaman[nama_anggota].pop(i)
                buku_tersedia.append(buku)

                # Menghitung tanggal peminjaman dan pengembalian
                tgl_peminjaman = datetime.strptime(tanggal_peminjaman, "%d-%m-%Y")
                tgl_pengembalian = datetime.strptime(tanggal_pengembalian, "%d-%m-%Y")
                batas_peminjaman = tgl_peminjaman + timedelta(days=15)
                keterlambatan = (tgl_pengembalian - batas_peminjaman).days

                if keterlambatan > 0:
                    denda = keterlambatan * 1000
                    print(f"{nama_anggota} mengembalikan buku '{buku[0]}' terlambat {keterlambatan} hari dengan denda Rp {denda}.")
                else:
                    print(f"{nama_anggota} mengembalikan buku '{buku[0]}' tepat waktu. Tidak ada denda.")

                if not peminjaman[nama_anggota]:
                    del peminjaman[nama_anggota]
                return
    print(f"{nama_anggota} tidak meminjam buku dengan ID {id_buku}.")

def tampilkan_peminjam():
    """Menampilkan daftar peminjam beserta buku yang dipinjam."""
    print("\nDaftar Peminjam Buku:")
    if peminjaman:
        for nama_anggota, buku_list in peminjaman.items():
            for buku, tanggal_peminjaman in buku_list:
                print(f"- {nama_anggota} meminjam buku '{buku[0]}' (ID: {buku[2]}) pada tanggal {tanggal_peminjaman}.")
    else:
        print("Tidak ada peminjam saat ini.")

def laporkan_buku_hilang(nama_anggota, id_buku):
    """Memproses laporan buku hilang."""
    if nama_anggota in peminjaman:
        for i, (buku, _) in enumerate(peminjaman[nama_anggota]):
            if buku[2] == id_buku:
                peminjaman[nama_anggota].pop(i)
                denda = buku[1] * 2
                print(f"{nama_anggota} melaporkan buku '{buku[0]}' hilang. Denda yang harus dibayar adalah Rp {denda}.")
                if not peminjaman[nama_anggota]:
                    del peminjaman[nama_anggota]
                return
    print(f"{nama_anggota} tidak meminjam buku dengan ID {id_buku}.")

def update_buku(id_buku, judul_baru, harga_baru):
    """Memperbarui data buku berdasarkan ID buku."""
    for i, buku in enumerate(buku_tersedia):
        if buku[2] == id_buku:
            buku_tersedia[i] = (judul_baru, harga_baru, id_buku, buku[3])
            print(f"Buku dengan ID {id_buku} berhasil diperbarui menjadi '{judul_baru}' dengan harga Rp {harga_baru}.")
            return
    print(f"Buku dengan ID {id_buku} tidak ditemukan.")

def hapus_buku(id_buku):
    """Menghapus buku dari daftar berdasarkan ID buku."""
    for i, buku in enumerate(buku_tersedia):
        if buku[2] == id_buku:
            buku_tersedia.pop(i)
            print(f"Buku '{buku[0]}' berhasil dihapus dari daftar.")
            return
    print(f"Buku dengan ID {id_buku} tidak ditemukan.")

def main():
    while True:
        print("\n===SISTEM PEMINJAMAN BUKU DI PERPUSTAKAAN CAHAYA ILMU===")
        print("Menu Peminjaman Buku di Perpustakaan Cahaya Ilmu:")
        print("1. Tampilkan Buku")
        print("2. Tampilkan Harga Buku")
        print("3. Pinjam Buku")
        print("4. Tampilkan Peminjam")
        print("5. Kembalikan Buku")
        print("6. Laporkan Buku Hilang")
        print("7. Update Data Buku")
        print("8. Hapus Data Buku")
        print("9. Keluar")
        pilihan = input("Pilih menu (1/2/3/4/5/6/7/8/9): ")

        if pilihan == '1':
            tampilkan_buku()
        elif pilihan == '2':
            tampilkan_harga_buku()
        elif pilihan == '3':
            nama = input("Masukkan nama peminjam: ").capitalize()
            id_buku = int(input("Masukkan ID buku yang ingin dipinjam: "))
            tanggal = input("Masukkan tanggal peminjaman (DD-MM-YYYY): ")
            pinjam_buku(nama, id_buku, tanggal)
        elif pilihan == '4':
            tampilkan_peminjam()
        elif pilihan == '5':
            nama = input("Masukkan nama pengembali: ").capitalize()
            id_buku = int(input("Masukkan ID buku yang ingin dikembalikan: "))
            tanggal_pengembalian = input("Masukkan tanggal pengembalian (DD-MM-YYYY): ")
            kembalikan_buku(nama, id_buku, tanggal_pengembalian)
        elif pilihan == '6':
            nama = input("Masukkan nama pelapor: ").capitalize()
            id_buku = int(input("Masukkan ID buku yang hilang: "))
            laporkan_buku_hilang(nama, id_buku)
        elif pilihan == '7':
            id_buku = int(input("Masukkan ID buku yang ingin diperbarui: "))
            judul_baru = input("Masukkan judul buku baru: ")
            harga_baru = int(input("Masukkan harga buku baru: "))
            update_buku(id_buku, judul_baru, harga_baru)
        elif pilihan == '8':
            id_buku = int(input("Masukkan ID buku yang ingin dihapus: "))
            hapus_buku(id_buku)
        elif pilihan == '9':
            print("Terima kasih telah menggunakan sistem peminjaman Perpustakaan 'Cahaya Ilmu'.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

main()