from models.pengguna import Mahasiswa, Dosen
from services.akademik import SistemAkademik
from exceptions.custom_exceptions import (
    NIMDuplikatError,
    MahasiswaTidakDitemukanError,
    NilaiTidakValidError,
    AbsensiDuplikatError
)

def menu_utama(sistem: SistemAkademik):
    """
    Fungsi menu utama untuk mengendalikan antarmuka CLI.
    Menerima parameter objek dari kelas SistemAkademik sebagai controller.
    """
    while True:
        print("\n" + "="*40)
        print("🎓 SISTEM INFORMASI AKADEMIK CLI 🎓")
        print("="*40)
        print("1. Tambah Mahasiswa")
        print("2. Tambah Dosen")
        print("3. Tampilkan Daftar Mahasiswa")
        print("4. Catat Absensi Mahasiswa")
        print("5. Input Nilai Mahasiswa")
        print("6. Rekap Peringkat & Nilai Kelas")
        print("7. Laporan Mahasiswa (Kehadiran < 75%)")
        print("0. Keluar")
        print("-" * 40)
        
        pilihan = input("Pilih menu (0-7): ")
        
        # Fitur 5: Validasi seluruh input dengan try/except agar tidak crash
        try:
            if pilihan == '1':
                print("\n-- TAMBAH MAHASISWA --")
                nama = input("Masukkan Nama: ")
                nim = input("Masukkan NIM: ")
                email = input("Masukkan Email: ")
                semester = int(input("Masukkan Semester (Angka): "))
                
                mhs = Mahasiswa(nama, nim, email, semester)
                pesan = sistem.tambah_mahasiswa(mhs)
                print(f"✅ [SUKSES] {pesan}")
                
            elif pilihan == '2':
                print("\n-- TAMBAH DOSEN --")
                nama = input("Masukkan Nama: ")
                nidn = input("Masukkan NIDN: ")
                email = input("Masukkan Email: ")
                mk = input("Masukkan Mata Kuliah: ")
                
                dsn = Dosen(nama, nidn, email, mk)
                pesan = sistem.tambah_dosen(dsn)
                print(f"✅ [SUKSES] {pesan}")

            elif pilihan == '3':
                sistem.tampilkan_daftar_mahasiswa()
                
            elif pilihan == '4':
                print("\n-- CATAT ABSENSI --")
                nim = input("Masukkan NIM Mahasiswa: ")
                pertemuan = int(input("Pertemuan ke- (Angka): "))
                status = input("Status (Hadir/Izin/Alpa): ")
                
                pesan = sistem.catat_absensi(nim, pertemuan, status)
                print(f"✅ [SUKSES] {pesan}")
                
            elif pilihan == '5':
                print("\n-- INPUT NILAI --")
                nim = input("Masukkan NIM Mahasiswa: ")
                jenis = input("Jenis Komponen (Tugas/UTS/UAS): ")
                nilai = float(input("Nilai (0 - 100): "))
                
                pesan = sistem.input_nilai(nim, jenis, nilai)
                print(f"✅ [SUKSES] {pesan}")
                
            elif pilihan == '6':
                sistem.rekap_nilai_kelas()
                sistem.peringkat_kelas()
                
            elif pilihan == '7':
                sistem.laporan_kehadiran_kurang()
                
            elif pilihan == '0':
                print("👋 Keluar dari program. Terima kasih!")
                break
                
            else:
                print("⚠️ [PERINGATAN] Pilihan tidak valid, silakan pilih angka 0-7.")
                
        # Menangkap error jika user salah memasukkan huruf pada input bertipe angka
        except ValueError:
            print("❌ [ERROR INPUT] Masukan tidak valid! Pastikan kolom Semester, Pertemuan, atau Nilai diisi dengan angka.")
        
        # Menangkap custom exception yang dilempar oleh core program
        except (NIMDuplikatError, MahasiswaTidakDitemukanError, NilaiTidakValidError, AbsensiDuplikatError) as e:
            print(f"❌ [ERROR SISTEM] {e}")
            
        # Menangkap error tidak terduga lainnya agar program tetap berjalan
        except Exception as e:
            print(f"❌ [FATAL ERROR] Terjadi kesalahan sistem: {e}")

# Blok pengeksekusi utama program
if __name__ == '__main__':
    # Membuat instance dari core service
    sistem_akademik = SistemAkademik()
    
    # Menjalankan fungsi menu utama
    menu_utama(sistem_akademik)