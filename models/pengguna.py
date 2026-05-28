# Sesuai standar PEP 8: Menggunakan PascalCase untuk penamaan Class
class Pengguna:
    def __init__(self, nama: str, id_pengguna: str, email: str):
        self.nama = nama
        self.id_pengguna = id_pengguna
        self.email = email
        
    def info(self) -> str:
        return f"Nama: {self.nama}, ID: {self.id_pengguna}, Email: {self.email}"
        
    def __str__(self) -> str:
        return f"{self.nama} ({self.id_pengguna})"


class Mahasiswa(Pengguna):
    def __init__(self, nama: str, id_pengguna: str, email: str, semester: int):
        super().__init__(nama, id_pengguna, email)
        self.semester = semester
        self._nilai_list: list = []
        from models.absensi import Absensi
        self.absensi = Absensi()

    def tambah_nilai(self, komponen) -> None:
        self._nilai_list.append(komponen)

    def nilai_akhir(self) -> float:
        # Mengkalkulasi nilai otomatis berdasarkan bobot polimorfisme komponen
        if not self._nilai_list:
            return 0.0
        return sum(k.nilai * k.bobot() for k in self._nilai_list)

    def info(self) -> str:
        info_induk = super().info()
        return f"{info_induk}, Semester: {self.semester}, Nilai Akhir: {self.nilai_akhir():.2f}"


class Dosen(Pengguna):
    def __init__(self, nama: str, id_pengguna: str, email: str, mata_kuliah: str):
        super().__init__(nama, id_pengguna, email)
        self.mata_kuliah = mata_kuliah

    def info(self) -> str:
        info_induk = super().info()
        return f"{info_induk}, Mengajar: {self.mata_kuliah}"