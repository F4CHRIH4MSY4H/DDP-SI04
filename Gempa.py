class Gempa:
    # Konsturoktor Inisialisasi atribut
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    # Method Penentu Gempa
    def dampak(self):
        # Logika/Statement
        if self.skala < 2:
            print('Gempa Tidak Berasa')
        elif 2 <= self.skala <= 4:
            print('Gempa Berdampak Bangunan Rusak')
        elif 4 <= self.skala <= 6:
            print('Gempa Berdampak Bangunan Roboh')
        elif self.skala > 6:
            print('Gempa Berpotensi Tsunami')

        # Menampilkan lokasi dan skala Gempa
        print(f'Lokasi Gempa: {self.lokasi}')
        print(f'Skala Gempa: {self.skala}')