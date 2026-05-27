#membuat exception untuk NIM Duplikat error, MahasiswaTidakDitemukanError, NilaiTidakValidError, AbsensiDuplikatError
class NIMDuplikatError(Exception):
    def __init__(self, pesan: str = "NIM sudah terdaftar di sistem!"):
        super().__init__(pesan)

class MahasiswaTidakDitemukanError(Exception):
    def __init__(self, pesan: str = "Mahasiswa tidak ditemukan di sistem!"):
        super().__init__(pesan)

class NilaiTidakValidError(Exception):
    def __init__(self, pesan: str = "Nilai tidak valid! Pastikan nilai berupa angka antara 0 - 100."):
        super().__init__(pesan)

class AbsensiDuplikatError(Exception):
    def __init__(self, pesan: str = "Absensi untuk mahasiswa ini sudah dicatat!"):
        super().__init__(pesan)