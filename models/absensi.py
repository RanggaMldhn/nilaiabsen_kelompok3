from exceptions.custom_exceptions import AbsensiDuplikatError

class CatatanAbsensi:
    def __init__(self, pertemuan_ke: int, status: str):
        self.pertemuan_ke = pertemuan_ke
        self.status = status

    def __str__(self):
        return f"Pertemuan ke-{self.pertemuan_ke}: {self.status}"


class Absensi:
    def __init__(self):
        self._catatan: list[CatatanAbsensi] = []

    # Disamakan fungsinya dengan yang dipanggil di akademik.py
    def catat_kehadiran(self, pertemuan_ke, status):
        for i in self._catatan:
            if i.pertemuan_ke == pertemuan_ke:
                raise AbsensiDuplikatError(f"Absensi pertemuan ke-{pertemuan_ke} sudah dicatat!")
        
        baru = CatatanAbsensi(pertemuan_ke, status)
        self._catatan.append(baru)

    # Disamakan fungsinya dengan yang dipanggil di akademik.py
    def hitung_persentase(self) -> float:
        if len(self._catatan) == 0:
            return 0.0
        
        hadir = 0
        for i in self._catatan:
            if i.status.lower() == 'hadir':
                hadir += 1
                
        return (hadir / len(self._catatan)) * 100

    def tampilkan(self):
        for i in self._catatan:
            print(i)