#string (harfsel değişkenler)
k="Trakya üniversitesi"
print(type(k))
print (k)
l=len(k)
print (f"k değişkeni {l} harften oluşuyor")

kelime=input("Lütfen bir kelime yazın:")
uzunluk=len(kelime)
print (f"{kelime} kelimesi {uzunluk} tane harften oluşuyor... ")
kac=int(input("kacinci karakter:")) #alınan string degeri sayiya cevir kac degiskenine yükle
kelime2=kelime[kac]
print (f"Alınan kısım {kelime2}")
#araba a(0. indeks)+b(1. indeks)+a(2. indeks)+b(3. indeks)+a(4. indeks)



