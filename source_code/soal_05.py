from collections import deque

class AntrianBank:
    def _init_(self):
        self.antrian = deque()

    def masuk(self, pelanggan):
        self.antrian.append(pelanggan)

    def keluar(self):
        if not self.is_empty():
            pelanggan_bank = self.antrian.popleft()
            return pelanggan_bank
        else:
            raise IndexError('Tidak ada pelanggan')

    def is_empty(self):
        return len(self.antrian) == 0

    def ukuran(self):
        return len(self.antrian)