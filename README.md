# 🔢 Konversi Bilangan (Python CLI)

Program **Python Command Line Interface (CLI)** untuk konversi antar sistem bilangan.  
Dibuat untuk membantu pembelajaran dasar **logika pemrograman** dan **sistem bilangan** (Desimal, Biner, Oktal, Hexa).

---

## ✨ Fitur
- Konversi antar bilangan:
  - Desimal ↔ Biner
  - Desimal ↔ Oktal
  - Desimal ↔ Hexa
  - Biner ↔ Oktal / Hexa
  - Oktal ↔ Hexa
- Validasi input:
  - Hanya menerima angka valid sesuai basis bilangan (contoh: Biner hanya `0` dan `1`)
  - Jika input salah, program meminta input ulang (loop retry)
- Output Biner otomatis minimal **4 digit** (contoh: `5 → 0101`)
- Menu interaktif berbasis teks (CLI)

---

## 🛠 Kebutuhan
- Editor / Terminal:
  - **VS Code** (Windows/Linux/macOS) → [Download](https://code.visualstudio.com/)  
  - **Termux** (Android) → [Google Play Store](https://play.google.com/store/apps/details?id=com.termux) atau [F-Droid](https://f-droid.org/packages/com.termux/)  
  

---

## 🚀 Cara Menjalankan

### 1. Jalankan di **VS Code (Windows/Linux/macOS)**
1. Install Python 3.
   - Python 3.x** → [Download di sini](https://www.python.org/downloads/)
   - Cek instalasi:  
     ```bash
     python --version
     ```
     atau
     
     ```bash
     python3 --version
     ```

3. Buka **VS Code** → buka folder project ini.  

4. Buka terminal di VS Code (`Ctrl + ~`), lalu jalankan:
   ```bash
   python3 bilangan_converter.py
   
   atau
   
   python3 ascii_converter.py

### 2. Jalankan di **Termux (Android)**
1. Install **Termux** dari [F-Droid](https://f-droid.org/packages/com.termux/) (rekomendasi).  

2. Buka **Termux**, lalu update dan install Python + Git:
   ```bash
   pkg update && pkg upgrade
   pkg install python git

3. Clone repository project ini dari GitHub:

   ```bash
   git clone https://github.com/abdansyakur354/konversi-bilangan-python3.git
   
4. Masuk ke folder project:
   ```bash
   cd konversi-bilangan-python3

5. Jalankan program:
  ```bash
  python3 bilangan_converter.py

  atau

  python3 ascii_converter.py


   
