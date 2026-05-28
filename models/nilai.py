from abc import ABC, abstractmethod
from exceptions.custom_exceptions import NilaiTidakValidError

class KomponenNilai(ABC):
    def __init__(self, nilai: float):
        self._nilai = 0.0
        self.nilai = nilai

    @property
    def nilai(self) -> float:
        return self._nilai
    
    @nilai.setter
    def nilai(self, value: float) -> None:
        try:
            numeric_value = float(value)
        except (ValueError, TypeError):
            raise NilaiTidakValidError("Nilai harus berupa angka numerik!")
        
        if not (0 <= numeric_value <= 100):
            # Ditambahkan f di depan string biar format angkanya kebaca
            raise NilaiTidakValidError(f"Nilai tidak valid ({numeric_value}). Harus diantara 0 - 100!")
        self._nilai = numeric_value

    @abstractmethod
    def bobot(self) -> float:
        pass

    @abstractmethod
    def nama_komponen(self) -> str:
        pass


class NilaiTugas(KomponenNilai):
    def __init__(self, nilai: float):
        super().__init__(nilai)

    def bobot(self) -> float:
        return 0.30
    
    def nama_komponen(self) -> str:
        return "Tugas"


class NilaiUTS(KomponenNilai):
    def __init__(self, nilai: float):
        super().__init__(nilai)

    def bobot(self) -> float:
        return 0.35
    
    def nama_komponen(self) -> str:
        return "UTS"


class NilaiUAS(KomponenNilai):
    def __init__(self, nilai: float):
        super().__init__(nilai)

    def bobot(self) -> float:
        return 0.35

    def nama_komponen(self) -> str:
        return "UAS"