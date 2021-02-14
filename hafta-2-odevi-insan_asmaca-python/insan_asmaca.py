# İnsan Asmaca Oyunu
# -----------------------------------
import random
import string
import pandas as pd

KELIME_LISTESI_DOSYASI = "tdk_sozcukler2.csv"
TÜRKÇE_ALFABE = 'abcçdefgğhıijklmnoöprsştuüvyz'
def kelimeleri_yükle():
    """
    Geçerli kelimelerin bir listesini döndürür. 
    Kelimeler, küçük harflerden oluşan dizelerdir.
    
    Sözcük listesinin boyutuna bağlı olarak, bu işlevin 
    tamamlanması biraz zaman alabilir.
    """
    print("Dosyadan kelime listesi okunuyor...")
    # dosyanın okunması
    dosya = pd.read_csv("tdk_sozcukler2.csv")
    # sözcüklerin küçük harfe çevrilmesi
    dosya['SOZCUKLER'] = dosya['SOZCUKLER'].str.lower() 
    # wordlist: list of strings
    kelime_listesi = dosya['SOZCUKLER'].tolist()
    print(f"{len(kelime_listesi)} kelimelik liste hazırlandı.")
    return kelime_listesi


def kelime_seç(kelime_listesi):
    """
    kelime_listesi (liste): kelimelerin listesi (dize)
    
    Kelime listesinde rastgele bir kelime döndürür.
    """
    return random.choice(kelime_listesi)

def unique(gizli_kelime):
    #puanlama amaçlı kullanmak üzere ekledim
    newlist=[]
    for harf in gizli_kelime:
        newlist.append(harf)
    newlist = set(newlist)
    return newlist

# Programın herhangi bir yerinden erişilebilmesi için kelime 
# listesini değişken kelime_listesine yükleyin
kelime_listesi = kelimeleri_yükle()

def kelime_tahmin_edildi_mi(gizli_kelime, tahmin_edilen_harfler):
    '''
    gizli_kelime: dize, kullanıcının tahmin ettiği kelime; 
        tüm harflerin küçük olduğunu varsayar
    tahmin_edilen_harfler: şimdiye kadar tahmin edilen harflerin listesi; 
        tüm harflerin küçük olduğunu varsayar
    döndürdüğü: boolean, gizli_kelime'nin tüm harfleri tahmin_edilen_harfler içindeyse True; 
        aksi takdirde False
    '''
    tahmin = True
    for harf in gizli_kelime:
        if harf in tahmin_edilen_harfler:
            pass
        else:
            tahmin = False
    return tahmin


def tahmin_edilen_kelimeyi_al(gizli_kelime, tahmin_edilen_harfler):
    '''
    gizli_kelime: dize, kullanıcının tahmin ettiği kelime; 
        tüm harflerin küçük olduğunu varsayar
    tahmin_edilen_harfler: şimdiye kadar tahmin edilen harflerin listesi; 
        tüm harflerin küçük olduğunu varsayar
    döndürdüğü: dize, harflerden oluşur, alt çizgiler (_) ve gizli_kelime içindeki hangi harflerin 
        şimdiye kadar tahmin edildiğini temsil eden boşluklardan oluşur.
    '''
    tek = []
    for harf in gizli_kelime:
        if harf in tahmin_edilen_harfler:
            tek.append(harf)
        else:
            tek.append('_')
    return " ".join(tek)

def uygun_harfleri_al(tahmin_edilen_harfler, alfabe = TÜRKÇE_ALFABE):
    '''
    tahmin_edilen_harfler: şimdiye kadar tahmin edilen harflerin listesi; 
        tüm harflerin küçük olduğunu varsayar
    döndürdüğü: dize (harfler), Henüz tahmin edilmemiş harfleri temsil 
        eden harflerden oluşur.
    '''
    # alfabedeki harfleri alır
    alfabe = TÜRKÇE_ALFABE

    uygun_harfler = []
    for harf in alfabe:
        uygun_harfler.append(harf)
    #print(f">>>>{uygun_harfler}")
    for harf in tahmin_edilen_harfler:
        if harf in uygun_harfler:
            uygun_harfler.remove(harf)
    uygun_harfler = ', '.join(uygun_harfler)
    return uygun_harfler

def dogru_harf_mi(gizli_kelime,harf):
    include = False
    for char in gizli_kelime:
        if harf == char:
            include = True
    return include 
    

def insan_asmaca(gizli_kelime, alfabe = TÜRKÇE_ALFABE):
    
    # alfabedeki harfleri alır
    alfabe = TÜRKÇE_ALFABE
    print(f">>>İnsan Asmaca Oyununa Hoşgeldiniz<<<\n6 tahmin hakkınız bulunmaktadır. Tahmin edeceğiniz kelime {len(gizli_kelime)} harf içermektedir.")
    isFinished = False
    tahmin_sayisi = 6
    uyari_sayisi = 3
    tahmin_edilen_harfler = []
    while isFinished != True:
        should_i_pass = False
        print(f"Kalan tahmin hakkınız: {tahmin_sayisi}")
        print(f"Kalan uyarı hakkınız: {uyari_sayisi}")
        tahmin = str(input("Lutfen bir harf giriniz: "))
        tahmin = tahmin.lower()
        if tahmin in tahmin_edilen_harfler:
            print("Oops, bu harfi daha önce girmiştiniz!")
            print(tahmin_edilen_kelimeyi_al(gizli_kelime,tahmin_edilen_harfler))
            if uyari_sayisi <= 0:
                tahmin_sayisi += -1
                should_i_pass = True
            else:
                uyari_sayisi += -1
                should_i_pass = True
        elif len(tahmin) != 1 or not tahmin.isalpha():
            
            if uyari_sayisi <= 0:
                tahmin_sayisi += -1
                should_i_pass = True
            else:
                uyari_sayisi += -1
                should_i_pass = True
            print("Oops! Lutfen gecerli bir harf giriniz!")
        
        if should_i_pass == False:    
            tahmin_edilen_harfler.append(tahmin)
        should_i_pass = True
        sonuc = kelime_tahmin_edildi_mi(gizli_kelime,tahmin_edilen_harfler)
        print(f"Uygun Harfler: {uygun_harfleri_al(tahmin_edilen_harfler,alfabe)}")
        print(sonuc)
        x = dogru_harf_mi(gizli_kelime,tahmin)
        if x != True:
            print(f"Oops! Bu harf benim kelimemde yok: {tahmin_edilen_kelimeyi_al(gizli_kelime,tahmin_edilen_harfler)}")
            if tahmin in {"a","e","i","ı","ö","o","ü","u"}:
                tahmin_sayisi -= 2
            else:
                tahmin_sayisi -= 1
        if x == True:
            print(f"Güzel tahmin: {tahmin_edilen_kelimeyi_al(gizli_kelime,tahmin_edilen_harfler)}")
        if tahmin_sayisi <= 0 and sonuc != True:
            print(f"Oyun bitti! Maalesef kaybettiniz :( \nGizli Kelime: {gizli_kelime}")
            isFinished = True
        elif sonuc == True:
            print(f"Oyun bitti! Tebrikler, kazandınız :)\nBu oyun için toplam puanınız: {tahmin_sayisi * len(unique(gizli_kelime))}")
            isFinished = True
        print("----")

#b _ r _ ş
def boşluklarla_eşleştir(benim_kelimem, diğer_kelime):
    '''
    benim_kelimem: _ karakterli dize, geçerli gizli_kelime tahmini
    diğer_kelime: dize, normal Türkçe kelime
    döndürdüğü: boolean, eğer benim_kelimem'in tüm gerçek harfleri 
       diğer_kelime'nin karşılık gelen harfleriyle eşleşiyorsa veya 
       harf özel sembol _ ise ve benim_kelimem ve diğer_kelim aynı 
       uzunluktaysa True; aksi takdirde False. 
    '''
    
    benim_kelimem = benim_kelimem.replace(" ","")
    if len(benim_kelimem) == len(diğer_kelime):
        for i in range(len(benim_kelimem)):
            if benim_kelimem[i] != "_":
                if benim_kelimem[i] != diğer_kelime[i]:
                    return False
        return True
    return False



def olası_eşleşmeleri_göster(benim_kelimem):
    '''
    benim_kelimem: _ karakterli dize, geçerli gizli_kelime tahmini
    döndürdüğü: hiçbir şey, ancak kelime listesindeki my_word ile eşleşen her kelimeyi 
             yazdırmalıdır. Ekranda bir harf tahmin edildiğinde, o harfin gizli kelimede 
             geçtiği tüm pozisyonların ortaya çıktığını unutmayın. Bu nedenle, 
             gizli harf (_) zaten açığa çıkmış kelimedeki harflerden biri olamaz.
    '''
    new_kelime_list = []
    for kelime in kelime_listesi:
        if boşluklarla_eşleştir(benim_kelimem,kelime):
            new_kelime_list.append(kelime)
    print(new_kelime_list)



def ipuçlarıyla_insan_asmaca(gizli_kelime, alfabe=TÜRKÇE_ALFABE):
    
    # alfabedeki harfleri alır
    alfabe = TÜRKÇE_ALFABE
    print(f">>>İnsan Asmaca Oyununa Hoşgeldiniz<<<\n6 tahmin hakkınız bulunmaktadır. Tahmin edeceğiniz kelime {len(gizli_kelime)} harf içermektedir.")
    isFinished = False
    tahmin_sayisi = 6
    uyari_sayisi = 3
    tahmin_edilen_harfler = []
    while isFinished != True:
        should_i_pass = False
        print(f"Kalan tahmin hakkınız: {tahmin_sayisi}")
        print(f"Kalan uyarı hakkınız: {uyari_sayisi}")
        #ipucu=str(input("Eşleşen kelimeleri görmek istiyor musunuz? (E/H): "))
        
        tahmin = str(input("Lutfen bir harf giriniz (ipucu kelimeleri için * girin): ")) 
        
        if tahmin in tahmin_edilen_harfler:
            print("Oops, bu harfi daha önce girmiştiniz!")
            print(tahmin_edilen_kelimeyi_al(gizli_kelime,tahmin_edilen_harfler))
            if uyari_sayisi <= 0:
                tahmin_sayisi += -1
                should_i_pass = True
            else:
                uyari_sayisi += -1
                should_i_pass = True
        elif len(tahmin) != 1 or not tahmin.isalpha():
            if tahmin == "*":
                olası_eşleşmeleri_göster(tahmin_edilen_kelimeyi_al(gizli_kelime,tahmin_edilen_harfler))
            else:
                if uyari_sayisi <= 0:
                    tahmin_sayisi += -1
                    should_i_pass = True
                else:
                    uyari_sayisi += -1
                    should_i_pass = True
            print("Oops! Lutfen gecerli bir harf giriniz!")
            
        if should_i_pass == False:
            tahmin_edilen_harfler.append(tahmin)
        should_i_pass = False
        sonuc = kelime_tahmin_edildi_mi(gizli_kelime,tahmin_edilen_harfler)
        print(sonuc)
        print(f"Uygun Harfler: {uygun_harfleri_al(tahmin_edilen_harfler,alfabe)}")
        
        x = dogru_harf_mi(gizli_kelime,tahmin)
        if x != True:
            print(f"Oops! Bu harf benim kelimemde yok: {tahmin_edilen_kelimeyi_al(gizli_kelime,tahmin_edilen_harfler)}")
            if tahmin in {"a","e","i","ı","ö","o","ü","u"}:
                tahmin_sayisi -= 2
            else:
                tahmin_sayisi -= 1
        if x == True:
            print(f"Güzel tahmin: {tahmin_edilen_kelimeyi_al(gizli_kelime,tahmin_edilen_harfler)}")
        if tahmin_sayisi <= 0 and sonuc != True:
            print(f"Oyun bitti! Maalesef kaybettiniz :( \nGizli Kelime: {gizli_kelime}")
            isFinished = True
        elif sonuc == True:
            print(f"Oyun bitti! Tebrikler, kazandınız :)\nBu oyun için toplam puanınız: {tahmin_sayisi * len(unique(gizli_kelime))}")
            isFinished = True
        print("----")
    

if __name__ == "__main__":
    
    #ipucuyla mı yoksa normal mi oynamak istediğinize oyun içinde karar verebilirsiniz

    should_continue = True
    while should_continue != False:
        gizli_kelime = kelime_seç(kelime_listesi)
        control = str(input("Normal insan asmaca için '1', ipuçlarıyla insan asmaca oynamak için '2', çıkmak için '3' giriniz: "))
        if control not in {'1','2'}:
            if control == 'q':
                break
            print("Lütfen doğru bir girdi giriniz!")
            continue
        if control == '2':
            ipuçlarıyla_insan_asmaca(gizli_kelime, alfabe=TÜRKÇE_ALFABE)
        if control == '1':
            insan_asmaca(gizli_kelime, alfabe=TÜRKÇE_ALFABE)