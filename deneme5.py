kelime=input("Lütfen bir kelime yazın:")
uzunluk=len(kelime)
print (f"{kelime} kelimesi {uzunluk} tane harften oluşuyor... ")
kac=int(input("kacinci karakterden başlasın:")) #alınan string degeri sayiya cevir kac degiskenine yükle
kac2=int(input("kacinci karaktere kadar alsın:"))
kelime2=kelime[kac:kac2] #KAC 0.KARAKTERDEN BAŞLAR kac2 İSE KELİMENİN İLK HARFİNDEN BAŞLAR
print (f"Alınan kısım {kelime2}")
#araba a(0. indeks)+r(1. indeks)+a(2. indeks)+b(3. indeks)+a(4. indeks)
