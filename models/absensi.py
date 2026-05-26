from exceptions.custom_exceptions import AbsensiDuplikatError

class CatatanAbsensi:
    """Class untuk menyimpan satu baris catatan kehadiran mahasiswa."""

    def __init__(self, pertemuan_ke: int, status: str) -> None:
        """
        Simpan pertemuan_ke dan status.
        
        :param pertemuan_ke: Nomor pertemuan (int)
        :param status: Status kehadiran ('Hadir', 'Izin', atau 'Alpa')
        """
        self.pertemuan_ke: int = pertemuan_ke
        self.status: str = status

    def __str__(self) -> str:
        """Tampilkan pertemuan ke-N: status."""
        return f"Pertemuan ke-{self.pertemuan_ke}: {self.status}"


class Absensi:
    """Class untuk mengelola kumpulan catatan absensi satu mahasiswa."""

    def __init__(self) -> None:
        """Inisialisasi _catatan = [] sebagai list penampung CatatanAbsensi."""
        self._catatan: list[CatatanAbsensi] = []

    def catat(self, pertemuan_ke: int, status: str) -> None:
        """
        Mencatat absensi pertemuan baru.
        Raise AbsensiDuplikatError jika pertemuan sudah ada. 
        Tambahkan CatatanAbsensi baru jika belum ada.
        """
        # Validasi apakah nomor pertemuan sudah pernah dicatat sebelumnya
        for catatan in self._catatan:
            if catatan.pertemuan_ke == pertemuan_ke:
                raise AbsensiDuplikatError(
                    f"Absensi untuk pertemuan ke-{pertemuan_ke} sudah dicatat."
                )
        
        # Tambahkan objek CatatanAbsensi baru ke dalam list _catatan
        catatan_baru = CatatanAbsensi(pertemuan_ke, status)
        self._catatan.append(catatan_baru)

    def persentase_hadir(self) -> float:
        """
        Return (jumlah Hadir / total catatan) * 100.
        Menghindari error pembagian dengan nol jika catatan masih kosong.
        """
        if not self._catatan:
            return 0.0
            
        jumlah_hadir = sum(1 for catatan in self._catatan if catatan.status == "Hadir")
        return (jumlah_hadir / len(self._catatan)) * 100.0

    def tampilkan(self) -> None:
        """Cetak semua catatan absensi yang ada di dalam list."""
        for catatan in self._catatan:
            print(catatan)