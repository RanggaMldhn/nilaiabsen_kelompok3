from abc import ABC, abstractmethod
from exceptions.custom_exceptions import NilaiTidakValidError

#menambah kelas abstrak untuk komponen nilai dengan validasi nilai
class KomponenNilai(ABC):
    def __init__(self, nilai:float):
        self._nilai = 0.0
        self.nilai = nilai

#menambah property untuk nilai dengan validasi
    @property
    def nilai(self) -> float:
        return self._nilai
    
#menambah nilai setter dengan validasi
    @nilai.setter
    def nilai(self, value:float) -> None:
        try:
            numeric_value = float(value)
        except (ValueError, TypeError):
            raise NilaiTidakValidError("Nilai harus berupa angka numerik!")
        
        if not (0 <= numeric_value <= 100):
            raise NilaiTidakValidError("Nilai tidak valid ({numeric_value}). Harus diantara 0 - 100!")
        self._nilai = numeric_value

#menambah method abstract untuk bobot dan nama komponen
    @abstractmethod
    def bobot(self) -> float:
        pass

    @abstractmethod
    def nama_komponen(self) -> str:
        pass


#membuat class turunan nilai tugas
class NilaiTugas(KomponenNilai):
    def __init__(self, nilai:float):
        super().__init__(nilai)

    #mengimplementasikan method abstract untuk bobot dan nama komponen
    def bobot(self) -> float:
        return 0.30
    
    def nama_komponen(self) -> str:
        return "Tugas"

#membuat class turunan nilai UTS
class NilaiUTS(KomponenNilai):
    def __init__(self, nilai:float):
        super().__init__(nilai)

    #mengimplementasikan method abstract untuk bobot dan nama komponen
    def bobot(self) -> float:
        return 0.35
    
    def nama_komponen(self) -> str:
        return "UTS"

#membuat class turunan nilai UAS
class NilaiUAS(KomponenNilai):
    def __init__(self, nilai:float):
        super().__init__(nilai)

    #mengimplementasikan method abstract untuk bobot dan nama komponen
    def bobot(self) -> float:
        return 0.35

    def nama_komponen(self) -> str:
        return "UAS"
    
