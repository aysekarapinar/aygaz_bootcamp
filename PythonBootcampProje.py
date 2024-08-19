import random

def tas_kagit_makas_ADINIZ_SOYADINIZ():
    
    print("Taş, Kağıt, Makas oyununa hoş geldiniz!")
    print("Oyunun kuralları: Taş makası kırar, Makas kağıdı keser, Kağıt taşı sarar.")
    print("İlk iki turu kazanan oyunu kazanır.")
    print("Oyundan çıkmak için 'çıkış' yazabilirsiniz.\n")

    
    secenekler = ["taş", "kağıt", "makas"]
    oynanan_oyun_sayisi = 0
    oyuncu_galibiyetleri = 0
    bilgisayar_galibiyetleri = 0

    
    while True:
    
        oyuncu_galibiyetleri_tur = 0
        bilgisayar_galibiyetleri_tur = 0

        
        while oyuncu_galibiyetleri_tur < 2 and bilgisayar_galibiyetleri_tur < 2:
            oyuncu_secimi = input("Seçiminizi yapın (taş, kağıt, makas): ").lower()
            if oyuncu_secimi == "çıkış":
                print("Oyundan çıkılıyor...")
                return

            if oyuncu_secimi not in secenekler:
                print("Geçersiz bir seçim yaptınız, lütfen tekrar deneyin.")
                continue

            bilgisayar_secimi = random.choice(secenekler)
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")

            if oyuncu_secimi == bilgisayar_secimi:
                print("Beraberlik!")
            elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
                 (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt") or \
                 (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş"):
                print("Bu turu kazandınız!")
                oyuncu_galibiyetleri_tur += 1
            else:
                print("Bu turu bilgisayar kazandı!")
                bilgisayar_galibiyetleri_tur += 1

            print(f"Durum: Oyuncu {oyuncu_galibiyetleri_tur} - Bilgisayar {bilgisayar_galibiyetleri_tur}\n")

        
        if oyuncu_galibiyetleri_tur == 2:
            print("Tebrikler, oyunu kazandınız!")
        else:
            print("Bilgisayar oyunu kazandı.")

        oynanan_oyun_sayisi += 1

        
        tekrar_oyna = input("Başka bir oyun oynamak ister misiniz? (evet/hayır): ").lower()
        if tekrar_oyna != "evet":
            print("Oyunu bitirdiniz. Tekrar görüşmek üzere!")
            break

        bilgisayar_devam = random.choice(["evet", "hayır"])
        if bilgisayar_devam == "hayır":
            print("Bilgisayar oyunu bırakmak istiyor. Oyun sona erdi.")
            break
        else:
            print("Bilgisayar bir oyun daha oynamak istiyor. Başlıyoruz!\n")
