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
- **Python 3.x** → [Download di sini](https://www.python.org/downloads/)  
- Editor / Terminal:
  - **VS Code** (Windows/Linux/macOS) → [Download](https://code.visualstudio.com/)  
  - **Termux** (Android) → [Google Play Store](https://play.google.com/store/apps/details?id=com.termux) atau [F-Droid](https://f-droid.org/packages/com.termux/)  

---

## 🚀 Cara Menjalankan

### 1. Jalankan di **VS Code (Windows/Linux/macOS)**
1. Install Python 3.x sesuai OS kamu.  
   - Cek instalasi:  
     ```bash
     python --version
     ```
     atau  
     ```bash
     python3 --version
     ```

2. Buka **VS Code** → buka folder project ini.  

3. Pastikan file utama bernama `converter.py`.  

4. Buka terminal di VS Code (`Ctrl + ~`), lalu jalankan:
   ```bash
   python3 bilangan_converter.py
   atau
   ascii_converter.py
