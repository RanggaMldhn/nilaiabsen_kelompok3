# Membuat class Pengguna sebagai base class (Ubah jadi Huruf Kapital)
class Pengguna:
    def __init__(self, nama: str, id_pengguna: str, email: str):
        self.nama = nama
        self.id_pengguna = id_pengguna
        self.email = email
        
    def info(self) -> str:
        return f"Nama: {self.nama}, ID Pengguna: {self.id_pengguna}, Email: {self.email}"
        
    def __str__(self) -> str:
        return f"{self.nama} ({self.id_pengguna})"

# Menambahkan class Mahasiswa
class Mahasiswa(Pengguna):
    def __init__(self, nama: str, id_pengguna: str, email: str, semester: int):
        super().__init__(nama, id_pengguna, email)
        self.semester = semester
        self._nilai_list: list = []
        from models.absensi import Absensi
        self.absensi = Absensi()

    def tambah_nilai(self, komponen) -> None:
        self._nilai_list.append(komponen)

    # SEKARANG MENGEMBALIKAN FLOAT BIAR SINKRON SAMA TEST & AKADEMIK
    def nilai_akhir(self) -> float:
        if not self._nilai_list:
            return 0.0
        total = 0.0
        for komponen in self._nilai_list:
            total += komponen.nilai * komponen.bobot()
        return total

    def info(self) -> str:
        info_induk = super().info()
        return f"{info_induk}, Semester: {self.semester}, Nilai Akhir: {self.nilai_akhir():.2f}"

# Menambahkan class Dosen
class Dosen(Pengguna):
    def __init__(self, nama: str, id_pengguna: str, email: str, mata_kuliah: str):
        super().__init__(nama, id_pengguna, email)
        self.mata_kuliah = mata_kuliah

    def info(self) -> str:
        info_induk = super().info()
        return f"{info_induk}, Mata Kuliah: {self.mata_kuliah}"