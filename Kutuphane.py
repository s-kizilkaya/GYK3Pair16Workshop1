class Kitap:
    def __init__(self, ad, yazar, sayfa_sayisi, isbn):
        self.ad = ad
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.__isbn = isbn

    def get_isbn(self):
        return self.__isbn

    def __str__(self):
        return f"Kitap: {self.ad}, Yazar: {self.yazar}, Sayfa Sayısı: {self.sayfa_sayisi}, ISBN: {self.__isbn}"


class Kutuphane:
    def __init__(self):
        self.kitaplar = []

    def kitap_ekle(self, kitap):
        try:
            for mevcut_kitap in self.kitaplar:
                if mevcut_kitap.get_isbn() == kitap.get_isbn():
                    raise ValueError(f"Bu ISBN ({kitap.get_isbn()}) numarasına sahip kitap zaten ekli!")

            self.kitaplar.append(kitap)
            print(f"Kitap eklendi: {kitap}")

        except ValueError as e:
            print(f"Hata: {e}")

    def kitap_sil(self, isbn):
        try:
            for kitap in self.kitaplar:
                if kitap.get_isbn() == isbn:
                    self.kitaplar.remove(kitap)
                    print(f"Kitap kaldırıldı: {kitap}")
                    return

            raise ValueError(f"ISBN ({isbn}) ile eşleşen kitap bulunamadı!")

        except ValueError as e:
            print(f"Hata: {e}")

    def kitaplari_goster(self):
        if not self.kitaplar:
            print("Kütüphanede kayıtlı kitap bulunmamaktadır.")
        else:
            print("\n** Kütüphanedeki Kitaplar **")
            for kitap in self.kitaplar:
                print(kitap)


def main():
    kutuphane = Kutuphane()

    while True:
        print("\n** Kütüphane Yönetim Sistemi **")
        print("1. Kitap Ekle")
        print("2. Kitap Sil")
        print("3. Tüm Kitapları Göster")
        print("4. Çıkış")

        secim = input("Seçiminizi yapın: ").strip()

        if secim == "1":
            ad = input("Kitap Adı: ").strip()
            yazar = input("Yazar: ").strip()
            sayfa_sayisi = input("Sayfa Sayısı: ").strip()
            isbn = input("ISBN: ").strip()

            try:
                sayfa_sayisi = int(sayfa_sayisi)
                yeni_kitap = Kitap(ad, yazar, sayfa_sayisi, isbn)
                kutuphane.kitap_ekle(yeni_kitap)
            except ValueError:
                print("Hata: Sayfa sayısı bir sayı olmalıdır!")

        elif secim == "2":
            isbn = input("Silmek istediğiniz kitabın ISBN numarası: ").strip()
            kutuphane.kitap_sil(isbn)

        elif secim == "3":
            kutuphane.kitaplari_goster()

        elif secim == "4":
            print("Programdan çıkılıyor...")
            break

        else:
            print("\nGeçersiz seçim! Lütfen tekrar deneyin.\n")


if __name__ == "__main__":
    main()