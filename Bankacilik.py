class Hesap:
    def __init__(self, hesap_sahibi, hesap_numarasi, bakiye=0):
        self.hesap_sahibi = hesap_sahibi
        self.hesap_numarasi = hesap_numarasi
        self.__bakiye = bakiye

    def para_yatir(self, miktar):
        if miktar > 0:
            self.__bakiye += miktar
            print(f"{miktar} TL yatırıldı. Yeni bakiye: {self.__bakiye} TL")
        else:
            print("Geçersiz tutar!")

    def para_cek(self, miktar):
        if 0 < miktar <= self.__bakiye:
            self.__bakiye -= miktar
            print(f"{miktar} TL çekildi. Kalan bakiye: {self.__bakiye} TL")
        else:
            print("Yetersiz bakiye veya geçersiz tutar!")

    def bakiye_goster(self):
        print(f"Hesap Sahibi: {self.hesap_sahibi} - Bakiye: {self.__bakiye} TL")

    def get_bakiye(self):
        return self.__bakiye


class VadesizHesap(Hesap):
    def __init__(self, hesap_sahibi, hesap_numarasi, bakiye=0):
        super().__init__(hesap_sahibi, hesap_numarasi, bakiye)


class VadeliHesap(Hesap):
    def __init__(self, hesap_sahibi, hesap_numarasi, bakiye=0, faiz_orani=0.05):
        super().__init__(hesap_sahibi, hesap_numarasi, bakiye)
        self.faiz_orani = faiz_orani

    def faiz_hesapla(self, ay_sayisi):
        faiz_miktari = self.get_bakiye() * self.faiz_orani * ay_sayisi
        print(f"{ay_sayisi} ay için hesaplanan faiz: {faiz_miktari} TL")
        return faiz_miktari

    def para_cek(self, miktar):
        if miktar > 0 and miktar <= self.get_bakiye() * 0.9:
            super().para_cek(miktar)
        else:
            print("Vadeli hesapta en az %10 bakiye bırakılmalıdır!")


def main():
    hesaplar = {}

    while True:
        print("\n** Banka Hesap Yönetimi **")
        print("1. Hesap Aç")
        print("2. Para Yatır")
        print("3. Para Çek")
        print("4. Hesap Bakiyesi Görüntüle")
        print("5. Vadeli Hesapta Faiz Hesapla")
        print("6. Çıkış")

        secim = input("Seçiminizi yapın: ").strip()

        if secim == "1":
            hesap_sahibi = input("Hesap Sahibinin Adı: ").strip()
            hesap_numarasi = input("Hesap Numarası: ").strip()
            hesap_turu = input("Hesap Türü (1: Vadesiz, 2: Vadeli): ").strip()

            if hesap_turu == "1":
                hesaplar[hesap_numarasi] = VadesizHesap(hesap_sahibi, hesap_numarasi)
            elif hesap_turu == "2":
                faiz_orani = float(input("Faiz Oranı (Örn: 0.05): ").strip())
                hesaplar[hesap_numarasi] = VadeliHesap(hesap_sahibi, hesap_numarasi, 0, faiz_orani)
            else:
                print("Geçersiz hesap türü!")

        elif secim == "2":
            hesap_numarasi = input("Hesap Numarası: ").strip()
            if hesap_numarasi in hesaplar:
                miktar = float(input("Yatırılacak Miktar: ").strip())
                hesaplar[hesap_numarasi].para_yatir(miktar)
            else:
                print("Hesap bulunamadı!")

        elif secim == "3":
            hesap_numarasi = input("Hesap Numarası: ").strip()
            if hesap_numarasi in hesaplar:
                miktar = float(input("Çekilecek Miktar: ").strip())
                hesaplar[hesap_numarasi].para_cek(miktar)
            else:
                print("Hesap bulunamadı!")

        elif secim == "4":
            hesap_numarasi = input("Hesap Numarası: ").strip()
            if hesap_numarasi in hesaplar:
                hesaplar[hesap_numarasi].bakiye_goster()
            else:
                print("Hesap bulunamadı!")

        elif secim == "5":
            hesap_numarasi = input("Hesap Numarası: ").strip()
            if hesap_numarasi in hesaplar and isinstance(hesaplar[hesap_numarasi], VadeliHesap):
                ay = int(input("Faiz Hesaplanacak Ay Sayısı: ").strip())
                hesaplar[hesap_numarasi].faiz_hesapla(ay)
            else:
                print("Vadeli hesap bulunamadı veya yanlış hesap türü!")

        elif secim == "6":
            print("Programdan çıkılıyor...")
            break

        else:
            print("\nGeçersiz seçim! Lütfen tekrar deneyin.\n")


if __name__ == "__main__":
    main()
