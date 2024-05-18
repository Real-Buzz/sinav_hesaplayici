import time

def sonucHesapla():

    try:
        vize = float(input("\nVize puanınızı girin: "))
        if(vize < 0 or vize > 100):
            print("\nBu puan geçersiz.\n")
            time.sleep(1)
            sonucHesapla()
        final = float(input("\nFinal puanınızı girin: "))
        if(final < 0 or final > 100):
            print("\nBu puan geçersiz.\n")
            time.sleep(1)
            sonucHesapla()
    except:
        print("\nGeçersiz bir giriş yaptınız.\n")
        time.sleep(1)
        sonucHesapla()

    sonuc = vize*0.4 + final*0.6

    if(sonuc <= 100 and sonuc >= 90):
        print(f"\nSonuç: {sonuc:.2f}. Harf kodu: AA. Geçtiniz.\n")
        time.sleep(2)
        main()
    elif(sonuc < 90 and sonuc >= 85):
        print(f"\nSonuç: {sonuc:.2f}. Harf kodu: BA. Geçtiniz.\n")
        time.sleep(2)
        main()
    elif(sonuc < 85 and sonuc >= 80):
        print(f"\nSonuç: {sonuc:.2f}. Harf kodu: BB. Geçtiniz.\n")
        time.sleep(2)
        main()
    elif(sonuc < 80 and sonuc >= 70):
        print(f"\nSonuç: {sonuc:.2f}. Harf kodu: CB. Geçtiniz.\n")
        time.sleep(2)
        main()
    elif(sonuc < 70 and sonuc >= 60):
        print(f"\nSonuç: {sonuc:.2f}. Harf kodu: CC. Geçtiniz.\n")
        time.sleep(2)
        main()
    elif(sonuc < 60 and sonuc >= 50):
        print(f"\nSonuç: {sonuc:.2f}. Harf kodu: DC. Koşullu geçer.\n")
        time.sleep(2)
        main()
    elif(sonuc < 50 and sonuc >= 45):
        print(f"\nSonuç: {sonuc:.2f}. Harf kodu: DD. Koşullu geçer.\n")
        time.sleep(2)
        main()
    elif(sonuc < 45 and sonuc >= 35):
        print(f"\nSonuç: {sonuc:.2f}. Harf kodu: FD. Kaldınız.\n")
        time.sleep(2)
        main()
    elif(sonuc < 35 and sonuc >= 0):
        print(f"\nSonuç: {sonuc:.2f}. Harf kodu: FF. Kaldınız.\n")
        time.sleep(2)
        main()

def gecmekIcinKacAlmaliyim():

    try:
        vize = float(input("\nVize puanınızı girin: "))
        if(vize < 0 or vize > 100):
            print("\nBu puan geçersiz.\n")
            time.sleep(1)
            gecmekIcinKacAlmaliyim()
    except:
        print("\nGeçersiz bir giriş yaptınız.\n")
        time.sleep(1)
        gecmekIcinKacAlmaliyim()

    gerekenNot = (5*(60 - vize*0.4))/3

    print(f"\nGeçmek için final sınavından en az {gerekenNot:.2f} almalısınız.\n")
    time.sleep(2)
    main()

def main():
    
    try:
        secim = int(input("Ne yapmak istediğinizi seçin.\n• (1) Vize ve Final Puanlarıyla Ortalama ve Harf Notu Hesaplama\n• (2) \"Geçmek için Finalden Kaç Almalıyım?\" Hesaplama\n• (3) Çıkış\n-> "))
    except:
        print("\nGeçersiz bir seçim yaptınız.\n")
        time.sleep(1)
        main()

    if(secim == 1):
        sonucHesapla()
    elif(secim == 2):
        gecmekIcinKacAlmaliyim()
    elif(secim == 3):
        print("\nHoşçakalın...")
        time.sleep(1)
        exit()
    else:
        ("\nGeçersiz bir seçim yaptınız.\n")
        time.sleep(1)
        main()

main()