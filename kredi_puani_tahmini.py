#Gerekli kütüphanelerin yüklenmesi
import pandas as pd

#veri okuma işlemi
veri = pd.read_csv("veri.csv")
print(veri) #Verinin hepsi
print(veri.head()) #ilk 5 satır
#print(veri.info())  #veri hakkında bilgi
#print(veri.isnull().sum()) #veride boş değer yok
