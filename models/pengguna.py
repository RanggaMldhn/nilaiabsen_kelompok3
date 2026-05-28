#membuat class pengguna sebagai base class
class pengguna:
    #membuat constructor untuk class pengguna dengan atribut nama:str, id_pengguna:str, dan email:str
    def __init__(self, nama:str, id_pengguna:str, email:str):
        self.nama = nama
        self.id_pengguna = id_pengguna
        self.email = email
    def info(self) -> str:
        return f"Nama: {self.nama}, ID Pengguna: {self.id_pengguna}, Email: {self.email}"
    def __str__(self) -> str:
        return f"{self.nama} ({self.id_pengguna})"

#menambahkan class mahasiswa pengguna
class mahasiswa(pengguna):
    #membuat constructor untuk mahasiswa pengguna dengan atribut nama:str, id_pengguna:str, email:str, dan semester:int
    def __init__(self, nama:str, id_pengguna:str, email:str, semester:int):
        super().__init__(nama, id_pengguna, email)
        self.semester = semester
        self._nilai_list: list = []
        from models.absensi import Absensi
        self.absensi = Absensi()

    def tambah_nilai(self, komponen) -> None:
        self._nilai_list.append(komponen)

    def nilai_akhir(self) -> str:
        info_induk = super().info()
        return f"{info_induk}, Semester: {self.semester}"

#menambahkan class dosen pengguna
class dosen(pengguna):
    #memanggil super() init pada constructor
    def __init__(self, nama:str, id_pengguna:str, email:str, mata_kuliah:str):
        super().__init__(nama, id_pengguna, email)
        self.mata_kuliah = mata_kuliah

    def info(self) -> str:
        info_induk = super().info()
        return f"{info_induk}, Mata Kuliah: {self.mata_kuliah}"