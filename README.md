Santai, bagian tugasnya sudah saya kosongkan sesuai permintaanmu.

Untuk menjawab kebingunganmu soal *"gimana cara test, fitur, class diagram, keputusan desain"*, itu sebenarnya **bukan sesuatu yang harus kamu tes satu-satu sekarang**, melainkan sekadar **judul bagian (bab) di dalam file `README.md**`-mu untuk menjelaskan proyek ini ke orang lain (atau dosen).

* **Cara test:** Isinya cuma perintah terminal untuk menjalankan *unit testing* yang ada di folder `tests/`.
* **Fitur:** Daftar apa saja yang bisa dilakukan programmu (nambah mahasiswa, hitung nilai, dll).
* **Class Diagram:** Penjelasan struktur *class* OOP-mu secara singkat.
* **Keputusan Desain:** Penjelasan *kenapa* kode proyekmu dibuat dengan struktur seperti itu (misal: kenapa pakai *inheritance* atau folder dipisah-pisah).

Berikut adalah draf lengkap `README.md` yang sudah disesuaikan dengan nama proyek dan kelompokmu. Tinggal *copy-paste* saja!

---

```markdown
# Sistem Nilai dan Absensi Mahasiswa

Aplikasi CLI berbasis OOP Python untuk mengelola data mahasiswa, nilai, dan absensi secara otomatis.

## 👥 Anggota Kelompok
* **Moh. Rozan Istazada Firdausy** - 25083000060 (Tugas: )
* **Rangga Maulidhani** - 25083000064 (Tugas: )
* **Arbi Maulana** - 25083000070 (Tugas: )

---

## 🚀 Cara Menjalankan Program
Buka terminal di folder proyek ini, lalu jalankan perintah berikut:
```bash
python main.py

```

---

## 🧪 Cara Menjalankan Test (Unit Testing)

Proyek ini dilengkapi dengan *testing* otomatis untuk memastikan tidak ada *bug* di dalam kode. Untuk menjalankannya, ketik perintah ini di terminal:

```bash
python -m unittest tests/test_akademik.py

```

---

## ✨ Fitur Utama

* **Manajemen Data:** Menambah dan mengelola data mahasiswa.
* **Kalkulasi Nilai:** Input nilai secara terpisah (Tugas 30%, UTS 35%, UAS 35%) dan menghitung nilai akhir secara otomatis.
* **Sistem Absensi:** Mencatat kehadiran per pertemuan dan menghitung persentase kehadiran mahasiswa.
* **Rekap Akademik:** Menampilkan ringkasan data mahasiswa beserta nilai akhir dan status kehadirannya.
* **Validasi Keamanan:** Menggunakan *error handling* untuk mencegah NIM duplikat, absensi ganda, atau input nilai di luar rentang 0-100.

---

## 🏗️ Struktur Class (Class Diagram)

Program ini dibangun dengan struktur *class* berikut:

* **Pengguna**: *Base class* yang menyimpan identitas (nama, id, email).
* **Mahasiswa**: Turunan dari Pengguna yang menyimpan nilai dan absensi.
* **Dosen**: Turunan dari Pengguna yang memiliki mata kuliah.


* **KomponenNilai**: *Abstract class* untuk standarisasi bobot nilai.
* Diturunkan menjadi **NilaiTugas**, **NilaiUTS**, dan **NilaiUAS**.


* **Absensi & CatatanAbsensi**: Mengelola status kehadiran per pertemuan.
* **SistemAkademik**: *Controller* utama yang menghubungkan dan menjalankan semua fitur di atas.

---

## 💡 Keputusan Desain (Design Decisions)

1. **Pemisahan Folder (Modular):** Kode dipisah ke folder `models`, `services`, dan `exceptions` agar rapi, mudah dibaca, dan gampang dicari jika ada *bug*.
2. **Inheritance (Pewarisan):** `Mahasiswa` dan `Dosen` diturunkan dari `Pengguna` supaya kita tidak perlu menulis ulang variabel yang sama seperti nama dan ID.
3. **Polymorphism:** Penggunaan *abstract class* pada `KomponenNilai` membuat perhitungan nilai akhir menjadi jauh lebih dinamis dan rapi.
4. **Custom Exceptions:** Menggunakan *class error* buatan sendiri (seperti `NIMDuplikatError`) agar pesan *error* saat program gagal lebih mudah dipahami oleh pengguna.
