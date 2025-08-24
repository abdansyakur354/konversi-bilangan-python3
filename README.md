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

## 📦 Persyaratan
- Python **3.x** (cek dengan perintah):
  ```bash
  python --version
