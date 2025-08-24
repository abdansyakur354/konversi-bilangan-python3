# Program Konversi Teks, ASCII, dan Biner (Lengkap + Save ke File)

# Fungsi untuk menyimpan hasil ke file
def simpan_hasil(teks):
    with open("hasil_konversi.txt", "a", encoding="utf-8") as file:
        file.write(teks + "\n")
    print(" ✅ Hasil disimpan ke 'hasil_konversi.txt'")
    print("\n==========================================")

def teks_ke_ascii(teks):
    print("==========================================")
    print("\nHasil Konversi Teks ke ASCII:")
    hasil = []
    for karakter in teks:
        hasil.append(f"{karakter} -> {ord(karakter)}")
    print("\n".join(hasil))
    simpan_hasil("\n".join(hasil))

def ascii_ke_teks(kode_list):
    print("==========================================")
    print("\nHasil Konversi ASCII ke Teks:")
    hasil_teks = ''.join(chr(int(kode)) for kode in kode_list)
    hasil = f"{' '.join(kode_list)} -> {hasil_teks}"
    print(hasil)
    simpan_hasil(hasil)

def teks_ke_biner(teks):
    print("==========================================")
    print("\nHasil Konversi Teks ke Biner:")
    hasil = []
    for karakter in teks:
        hasil.append(f"{karakter} -> {bin(ord(karakter))[2:].zfill(8)}")
    print("\n".join(hasil))
    simpan_hasil("\n".join(hasil))

def biner_ke_teks(biner_list):
    print("==========================================")
    print("\nHasil Konversi Biner ke Teks:")
    hasil_teks = ''.join(chr(int(b, 2)) for b in biner_list)
    hasil = f"{' '.join(biner_list)} -> {hasil_teks}"
    print(hasil)
    simpan_hasil(hasil)

def ascii_ke_biner(kode_list):
    print("==========================================")
    print("\nHasil Konversi ASCII ke Biner:")
    hasil = []
    for kode in kode_list:
        biner = bin(int(kode))[2:].zfill(8)
        hasil.append(f"{kode} -> {biner}")
    print("\n".join(hasil))
    simpan_hasil("\n".join(hasil))

def biner_ke_ascii(biner_list):
    print("==========================================")
    print("\nHasil Konversi Biner ke ASCII:")
    hasil = []
    for b in biner_list:
        ascii_val = int(b, 2)
        hasil.append(f"{b} -> {ascii_val}")
    print("\n".join(hasil))
    simpan_hasil("\n".join(hasil))


while True:
    print("\n======= Program Konversi Lengkap =======")
    print("1. Teks ke ASCII")
    print("2. ASCII ke Teks")
    print("3. Teks ke Biner")
    print("4. Biner ke Teks")
    print("5. ASCII ke Biner")
    print("6. Biner ke ASCII")
    print("7. Keluar")
    
    pilihan = input("Pilih menu (1-7): ")
    
    if pilihan == "1":
        teks = input("Masukkan teks: ")
        teks_ke_ascii(teks)
    elif pilihan == "2":
        kode = input("Masukkan kode ASCII (pisahkan dengan spasi): ").split()
        ascii_ke_teks(kode)
    elif pilihan == "3":
        teks = input("Masukkan teks: ")
        teks_ke_biner(teks)
    elif pilihan == "4":
        biner = input("Masukkan kode biner (pisahkan dengan spasi): ").split()
        biner_ke_teks(biner)
    elif pilihan == "5":
        kode = input("Masukkan kode ASCII (pisahkan dengan spasi): ").split()
        ascii_ke_biner(kode)
    elif pilihan == "6":
        biner = input("Masukkan kode biner (pisahkan dengan spasi): ").split()
        biner_ke_ascii(biner)
    elif pilihan == "7":
        print("Terima kasih, program selesai.")
        break
    else:
        print("Pilihan tidak valid, coba lagi!")
