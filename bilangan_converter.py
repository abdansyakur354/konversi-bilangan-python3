def is_binary(s):
    return all(ch in "01" for ch in s)

def is_octal(s):
    return all(ch in "01234567" for ch in s)

def is_hexadecimal(s):
    return all(ch.upper() in "0123456789ABCDEF" for ch in s)

def is_decimal(s):
    return s.isdigit()

# === MENU DESIMAL ===
def decimal_menu():
    while True:
        print("\n=== Konversi Desimal ===")
        print("1. Desimal → Biner")
        print("2. Biner   → Desimal")
        print("3. Desimal → Oktal")
        print("4. Oktal   → Desimal")
        print("5. Desimal → Hexa")
        print("6. Hexa    → Desimal")
        print("0. Kembali")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            while True:
                d = input("Masukkan desimal: ")
                if is_decimal(d):
                    print("Biner:", bin(int(d))[2:].zfill(4))
                    break
                print("⚠️ Input harus angka desimal. Coba lagi.")

        elif pilih == "2":
            while True:
                b = input("Masukkan biner: ")
                if is_binary(b):
                    print("Desimal:", int(b, 2))
                    break
                print("⚠️ Input hanya boleh 0 dan 1. Coba lagi.")

        elif pilih == "3":
            while True:
                d = input("Masukkan desimal: ")
                if is_decimal(d):
                    print("Oktal:", oct(int(d))[2:])
                    break
                print("⚠️ Input harus angka desimal. Coba lagi.")

        elif pilih == "4":
            while True:
                o = input("Masukkan oktal: ")
                if is_octal(o):
                    print("Desimal:", int(o, 8))
                    break
                print("⚠️ Input hanya boleh 0–7. Coba lagi.")

        elif pilih == "5":
            while True:
                d = input("Masukkan desimal: ")
                if is_decimal(d):
                    print("Hexa:", hex(int(d))[2:].upper())
                    break
                print("⚠️ Input harus angka desimal. Coba lagi.")

        elif pilih == "6":
            while True:
                h = input("Masukkan hexa: ")
                if is_hexadecimal(h):
                    print("Desimal:", int(h, 16))
                    break
                print("⚠️ Input hanya boleh 0–9 atau A–F. Coba lagi.")

        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid!")

# === MENU BINER ===
def biner_menu():
    while True:
        print("\n=== Konversi Biner ===")
        print("1. Biner   → Desimal")
        print("2. Desimal → Biner")
        print("3. Biner   → Oktal")
        print("4. Oktal   → Biner")
        print("5. Biner   → Hexa")
        print("6. Hexa    → Biner")
        print("0. Kembali")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            while True:
                b = input("Masukkan biner: ")
                if is_binary(b):
                    print("Desimal:", int(b, 2))
                    break
                print("⚠️ Input hanya boleh 0 dan 1. Coba lagi.")

        elif pilih == "2":
            while True:
                d = input("Masukkan desimal: ")
                if is_decimal(d):
                    print("Biner:", bin(int(d))[2:].zfill(4))
                    break
                print("⚠️ Input harus angka desimal. Coba lagi.")

        elif pilih == "3":
            while True:
                b = input("Masukkan biner: ")
                if is_binary(b):
                    print("Oktal:", oct(int(b, 2))[2:])
                    break
                print("⚠️ Input hanya boleh 0 dan 1. Coba lagi.")

        elif pilih == "4":
            while True:
                o = input("Masukkan oktal: ")
                if is_octal(o):
                    print("Biner:", bin(int(o, 8))[2:].zfill(4))
                    break
                print("⚠️ Input hanya boleh 0–7. Coba lagi.")

        elif pilih == "5":
            while True:
                b = input("Masukkan biner: ")
                if is_binary(b):
                    print("Hexa:", hex(int(b, 2))[2:].upper())
                    break
                print("⚠️ Input hanya boleh 0 dan 1. Coba lagi.")

        elif pilih == "6":
            while True:
                h = input("Masukkan hexa: ")
                if is_hexadecimal(h):
                    print("Biner:", bin(int(h, 16))[2:].zfill(4))
                    break
                print("⚠️ Input hanya boleh 0–9 atau A–F. Coba lagi.")

        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid!")

# === MENU OKTAL ===
def octal_menu():
    while True:
        print("\n=== Konversi Oktal ===")
        print("1. Oktal   → Desimal")
        print("2. Desimal → Oktal")
        print("3. Oktal   → Biner")
        print("4. Biner   → Oktal")
        print("5. Oktal   → Hexa")
        print("6. Hexa    → Oktal")
        print("0. Kembali")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            while True:
                o = input("Masukkan oktal: ")
                if is_octal(o):
                    print("Desimal:", int(o, 8))
                    break
                print("⚠️ Input hanya boleh 0–7. Coba lagi.")

        elif pilih == "2":
            while True:
                d = input("Masukkan desimal: ")
                if is_decimal(d):
                    print("Oktal:", oct(int(d))[2:])
                    break
                print("⚠️ Input harus angka desimal. Coba lagi.")

        elif pilih == "3":
            while True:
                o = input("Masukkan oktal: ")
                if is_octal(o):
                    print("Biner:", bin(int(o, 8))[2:].zfill(4))
                    break
                print("⚠️ Input hanya boleh 0–7. Coba lagi.")

        elif pilih == "4":
            while True:
                b = input("Masukkan biner: ")
                if is_binary(b):
                    print("Oktal:", oct(int(b, 2))[2:])
                    break
                print("⚠️ Input hanya boleh 0 dan 1. Coba lagi.")

        elif pilih == "5":
            while True:
                o = input("Masukkan oktal: ")
                if is_octal(o):
                    print("Hexa:", hex(int(o, 8))[2:].upper())
                    break
                print("⚠️ Input hanya boleh 0–7. Coba lagi.")

        elif pilih == "6":
            while True:
                h = input("Masukkan hexa: ")
                if is_hexadecimal(h):
                    print("Oktal:", oct(int(h, 16))[2:])
                    break
                print("⚠️ Input hanya boleh 0–9 atau A–F. Coba lagi.")

        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid!")

# === MENU HEXA ===
def hexa_menu():
    while True:
        print("\n=== Konversi Hexa ===")
        print("1. Hexa    → Desimal")
        print("2. Desimal → Hexa")
        print("3. Hexa    → Biner")
        print("4. Biner   → Hexa")
        print("5. Hexa    → Oktal")
        print("6. Oktal   → Hexa")
        print("0. Kembali")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            while True:
                h = input("Masukkan hexa: ")
                if is_hexadecimal(h):
                    print("Desimal:", int(h, 16))
                    break
                print("⚠️ Input hanya boleh 0–9 atau A–F. Coba lagi.")

        elif pilih == "2":
            while True:
                d = input("Masukkan desimal: ")
                if is_decimal(d):
                    print("Hexa:", hex(int(d))[2:].upper())
                    break
                print("⚠️ Input harus angka desimal. Coba lagi.")

        elif pilih == "3":
            while True:
                h = input("Masukkan hexa: ")
                if is_hexadecimal(h):
                    print("Biner:", bin(int(h, 16))[2:].zfill(4))
                    break
                print("⚠️ Input hanya boleh 0–9 atau A–F. Coba lagi.")

        elif pilih == "4":
            while True:
                b = input("Masukkan biner: ")
                if is_binary(b):
                    print("Hexa:", hex(int(b, 2))[2:].upper())
                    break
                print("⚠️ Input hanya boleh 0 dan 1. Coba lagi.")

        elif pilih == "5":
            while True:
                h = input("Masukkan hexa: ")
                if is_hexadecimal(h):
                    print("Oktal:", oct(int(h, 16))[2:])
                    break
                print("⚠️ Input hanya boleh 0–9 atau A–F. Coba lagi.")

        elif pilih == "6":
            while True:
                o = input("Masukkan oktal: ")
                if is_octal(o):
                    print("Hexa:", hex(int(o, 8))[2:].upper())
                    break
                print("⚠️ Input hanya boleh 0–7. Coba lagi.")

        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid!")

# === MAIN PROGRAM ===
def main():
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Desimal")
        print("2. Biner")
        print("3. Oktal")
        print("4. Hexa")
        print("5. Keluar")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            decimal_menu()
        elif pilih == "2":
            biner_menu()
        elif pilih == "3":
            octal_menu()
        elif pilih == "4":
            hexa_menu()
        elif pilih == "5":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")

main()
