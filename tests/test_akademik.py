import pytest


from exceptions.custom_exceptions import (
    NilaiTidakValidError,
    AbsensiDuplikatError,
    NIMDuplikatError
)
from models.pengguna import Pengguna, Mahasiswa
from models.nilai import NilaiTugas
from services.akademik import SistemAkademik


from models.nilai import NilaiUTS, NilaiUAS




def test_nilai_di_luar_range():
    with pytest.raises(NilaiTidakValidError):
        nilai_invalid_atas = NilaiTugas(105)
       
    with pytest.raises(NilaiTidakValidError):
        nilai_invalid_bawah = NilaiTugas(-10)




def test_nilai_akhir_benar():
    mhs = Mahasiswa("Andi", "2024001", "andi@kampus.ac.id", semester=3)
   
    # 100 * 0.30 = 30
    mhs.tambah_nilai(NilaiTugas(100))
    # 80 * 0.35 = 28
    mhs.tambah_nilai(NilaiUTS(80))
    # 80 * 0.35 = 28
    mhs.tambah_nilai(NilaiUAS(80))
   


    hasil = mhs.nilai_akhir()
    assert hasil == 86.0




def test_mahasiswa_adalah_pengguna():
    mhs = Mahasiswa("Budi", "2024002", "budi@kampus.ac.id", semester=3)
   
    # Act & Assert
    assert isinstance(mhs, Pengguna)
    assert isinstance(mhs, Mahasiswa)




def test_absensi_duplikat():


    sistem = SistemAkademik()
    mhs = Mahasiswa("Cici", "2024003", "cici@kampus.ac.id", semester=3)
    sistem.tambah_mahasiswa(mhs)
   
    sistem.catat_absensi("2024003", pertemuan=1, status="Hadir")
   
    # Assert: Absen kedua (harus gagal)
    with pytest.raises(AbsensiDuplikatError):
        sistem.catat_absensi("2024003", pertemuan=1, status="Hadir")




def test_nim_duplikat():
    sistem = SistemAkademik()
    mhs1 = Mahasiswa("Dedi", "2024004", "dedi@kampus.ac.id", semester=3)
    mhs2 = Mahasiswa("Dewa", "2024004", "dewa@kampus.ac.id", semester=5) # NIM sama
   
    sistem.tambah_mahasiswa(mhs1)
   
    with pytest.raises(NIMDuplikatError):
        sistem.tambah_mahasiswa(mhs2)

