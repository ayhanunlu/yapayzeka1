#float değişkenler kesirli sayı değişkenler
pi=3.14
#input ekrandan veri almak için kullanılır
r=input("Lütfen dairenin çapını yazınız:") #string olarak alınıyor
#print (type(r))
cap=float(r)
#print (type(cap))
alan=pi*cap**2 
cevre=2*pi*cap
print (f"Dairenin Alanı:{alan} Çevresi {cevre}")
