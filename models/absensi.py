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

    def catat(self, pertemuan_ke, status):
        # cek dulu apakah pertemuan udah ada di list
        for i in self._catatan:
            if i.pertemuan_ke == pertemuan_ke:
                raise AbsensiDuplikatError("Pertemuan sudah ada")
        
        # kalau belum ada, bikin objek baru terus masukin list
        baru = CatatanAbsensi(pertemuan_ke, status)
        self._catatan.append(baru)

    def persentase_hadir(self):
        # biar gak error dibagi 0 kalau list masih kosong
        if len(self._catatan) == 0:
            return 0.0
        
        hadir = 0
        for i in self._catatan:
            if i.status == 'Hadir':
                hadir += 1
                
        return (hadir / len(self._catatan)) * 100

    def tampilkan(self):
        for i in self._catatan:
            print(i)