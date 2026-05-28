from exceptions.custom_exceptions import (
    NIMDuplikatError,
    MahasiswaTidakDitemukanError,
    AbsensiDuplikatError
)
from models.pengguna import Mahasiswa, Dosen
from models.nilai import NilaiTugas, NilaiUTS, NilaiUAS


class SistemAkademik:
    def __init__(self):
        self.daftar_mahasiswa: list[Mahasiswa] = []
        self.daftar_dosen: list[Dosen] = []


    def tambah_mahasiswa(self, mahasiswa: Mahasiswa) -> str:
        for mhs in self.daftar_mahasiswa:
            if mhs.id_pengguna == mahasiswa.id_pengguna:
                raise NIMDuplikatError(f"NIM {mahasiswa.id_pengguna} sudah terdaftar!")
           
        self.daftar_mahasiswa.append(mahasiswa)
        return f"Mahasiswa {mahasiswa.nama} berhasil ditambahkan."
   
    def tambah_dosen(self, dosen: Dosen) -> str:
        for d in self.daftar_dosen:
            if d.id_pengguna == dosen.id_pengguna:
                raise NIMDuplikatError(f"ID Dosen {dosen.id_pengguna} sudah terdaftar!")
           
        self.daftar_dosen.append(dosen)
        return f"Dosen {dosen.nama} berhasil ditambahkan."
   
    def cari_mahasiswa(self, nim: str) -> Mahasiswa:
        for mhs in self.daftar_mahasiswa:
            if mhs.id_pengguna == nim:
                return mhs
        raise MahasiswaTidakDitemukanError(f"Mahasiswa dengan NIM {nim} tidak ditemukan!")
   
    def tampilkan_daftar_mahasiswa(self) -> None:
        if not self.daftar_mahasiswa:
            print("Belum ada mahasiswa terdaftar.")
            return
       
        print("\n--- DAFTAR MAHASISWA ---")
        for mhs in self.daftar_mahasiswa:
            print(mhs.info())


    def catat_absensi(self, nim: str, pertemuan: int, status: str) -> str:
        mhs = self.cari_mahasiswa(nim)
        mhs.absensi.catat_kehadiran(pertemuan, status)
        return f"Absensi pertemuan {pertemuan} untuk {mhs.nama} berhasil dicatat ({status})."
   
    def input_nilai(self, nim: str, jenis_komponen: str, nilai_angka: float) -> str:
        mhs = self.cari_mahasiswa(nim)
        if jenis_komponen.lower() == "tugas":
            komponen = NilaiTugas(nilai_angka)
        elif jenis_komponen.lower() == "uts":
            komponen = NilaiUTS(nilai_angka)
        elif jenis_komponen.lower() == "uas":
            komponen = NilaiUAS(nilai_angka)
        else:
            return f"Jenis komponen {jenis_komponen} tidak valid!"
       
        mhs.tambah_nilai(komponen)
        return f"Nilai {jenis_komponen} ({nilai_angka}) berhasil ditambahkan untuk {mhs.nama}."
   
    def rekap_nilai_kelas(self) -> None:
        print("\n--- REKAP NILAI KELAS ---")
        if not self.daftar_mahasiswa:
            print("Belum ada data mahasiswa.")
            return
       
        for mhs in self.daftar_mahasiswa:
            print(f"{mhs.nama} ({mhs.id_pengguna}) - Nilai Akhir: {mhs.nilai_akhir():.2f}")


    def laporan_kehadiran_kurang(self) -> None:
        print("\n--- LAPORAN KEHADIRAN < 75% ---")
        ditemukan = False
        for mhs in self.daftar_mahasiswa:
            persentase = mhs.absensi.hitung_persentase()
            if persentase < 75.0:
                print(f"{mhs.nama} ({mhs.id_pengguna}) - Kehadiran: {persentase:.2f}%")
                ditemukan = True


        if not ditemukan:
            print("Tidak ada mahasiswa dengan kehadiran di bawah 75%. Semua aman!")


    def peringkat_kelas(self) -> None:
        print("\n--- PERINGKAT KELAS ---")
        if not self.daftar_mahasiswa:
            print("Belum ada data mahasiswa.")
            return
       
        mahasiswa_sorted = sorted(
            self.daftar_mahasiswa,
            key=lambda m: m.nilai_akhir(),
            reverse=True
        )


        for peringkat, mhs in enumerate(mahasiswa_sorted, start=1):
            print(f"Rank {peringkat}: {mhs.nama} - Nilai Akhir: {mhs.nilai_akhir():.2f}")