##################################
# Numpy
################################

# neden numpy ? (why Numpy ? )
# numpy array i oluşturmak (creating of numpy arrays)
# numpy array özellikleri (attiributes of numpy arrays)
# yeniden şekillendirme (reshaping)
# Index seçimi (index selection)
# sliciling
# fancy ındex
#  numpy'da koşullu ifadeler
# matematiksel işlemler (mathematical operations )

# verimli veri saklama  , yüksek seviyeden işlemler vektörel işlemler fixtype çok daha hızlı işlem yapabilir
# numpy int türünden veri tuttuğu için vektörel işlemer daha hızlı şekilde yapılabirilir
# döngü yazmaya gerek olmadan çok daha basit işlemlerle çaba gerektiren işlemleri gerçekleştirebiliriz
# hızlı çünkü sabit tipte veri tutarak gerçekleştiriyor
# vektörel seviyede işlemler yapmayı sağlıyor  daha az çaba daha çok işlem

import numpy as np

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

# amacım bu iki listedeki elemanları birbir ile çarpmak

ab = []

# bu kısımda bir range giriyoruz ve bize 0 dan başlayarak len(a) uzunluğunda bir
# gezinmeye sağlayacak değer üretiyor
for i in range(0, len(a)):
    ab.append(a[i] * b[i])

# şimdi bu işlemi numpy kullanarak nasıl yapacağımıza bakalım
# önce np array ine dönüştürüyoruz
# sabit tipte veri tutar
# vektör seviyesinde işlem yapar
a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])

a * b

#########################################
# Numpy array oluşturma  (creating numpy arrays)
#######################################

import numpy as np

np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4, 5]))

np.zeros(10) #girdiğimiz sayı adedince 0 değeri oluşturuyor

np.random.randint(0, 10, size=10) # o ile 10 arasında rastgele 10 tane random inr değer oluşturdu

np.random.normal(10, 4, (4,4))
#yukarıda oluşturmak istediğimiz kitlenin önce ortamasını ikinci olarak  argümanı(standart sapması) üçüncüsüne de boyut bilgisini gir



########################################
#numpy array özelliklerini değerlendireceğiz
#########################################

import  numpy as np

#ndim : boyut sayısı
# shape : boyut bilgisi
# size  : toplam eleman sayısı
# stype : array veri tipi

a = np.random.randint(10, size= 5) # 0 dan 10 a kadar 5 tane eleman oluşturur

a.ndim # tek boyutlu
a.shape # boyut bilgisini sunar ve içerisinde 5 eleman var satır ve sütun sayısı
a.size  # toplam eleman sayısını verir
a.dtype # int64 olarak verir


###################################
# Reshape yeniden şekillendirme
###################################

# import numpy as np

np.random.randint(1 , 10 ,size = 9)
np.random.randint(1 , 10 ,size = 9).reshape(3,3)

ar = np.random.randint(1 , 10 ,size = 9)
ar.reshape(3,3)

####################################
# Index selection
####################################
import numpy as np
a = np.random.randint(10, size=10)
a[0]
a[0:5] # 5'e kadar gidecek ama 5. index değerini almayacak index değeri 0 dan başlar

a[0] = 999

m= np.random.randint(10, size=(3, 5))

m[0, 0] # virgülden öncesi satırları   &&&& virgülden sonrası sütunları ifade eder

m[1, 1] # oluşturulan değerler de 0 dan başlıyor satır & sütun

m [2 , 3]

m [2 , 3]  = 999

m [2, 3] = 2.9 # float değerim sadece integer kısmını alır ve atama yapar

m [: , 0 ] # bütün satırları seç sıfırıncı sütünu seç

m[1, : ] # birinci satır ve tüm sütunları seçmek istersek

m[0:2, 0:3]  # 0 ve 1 satırları aldı  &&&&  0, 1, 2 sütun değerlerini aldı



#####################################
#Fancy index
#####################################

import numpy as np

v = np.arange(0, 30, 3) # sıfırdan 30'a kadar 3'er 3'er artacak şekilde  array oluşturduk demektir

# 30'a kadar yani 30 değeri hariç tutuluyor

v[1]
v[4]

catch = [1, 2, 3]

v[catch]

"""
yukarıda elimide bulunan herhangi bir listenin birden fazla index değerine ulaşmak 
istiyorsak ulaşmak istediğimiz index değerlerini içeren bir liste hazılar ve 
bu listde elemanları ile köşeli parantez ile arama gerçekleştir

yukarıda elimizde 0 dan 30 kadar 3 erli artan bir liste var bu listenin 1, 2, 3'üncü 
elemanına ulaşmak istiyorum catch diye bir liste oluşturuyorum ve liste ismin 
bu arama kısmına veriyorum istediğim index değerlerini ulaşıyorum 
"""


###############################################
#Numpy koşullu işlemler
###############################################

import numpy as np

v = np.array([1, 2, 3, 4, 5])

# amacımız 3 ten küçük olan elemanlara ulaşmak istiyoruz

#klasik döngü ile

ab = []

for i in v:
    if i < 3:
        ab.append(i)

# Numpy ile gerçekleştirelim
v < 3 # array in bütün elemanlarına bu sorguyu yapıyor True & False

v[v < 3] # 3 ten küçük elemanları yazdırdı
v[v > 3]
v[v != 3]



#####################################
# matematiksel işlemler
#####################################

import numpy as np

v = np.array([1, 2, 3, 4, 5])

#bütün elemanlarını 5 e bölmek istersek

v / 5

v * 5 / 10

v ** 2  # her eleanın karesini aldık
# yukarıdaki işlemleri operatörler aracılığı ile gerçekleştirdik
# aşağıdaki işlemleri metodlar ile gerçekleştirdik

np.subtract (v, 1) # çıkarma işlemi için
np.add(v, 1) # toplama işlemi için
np.mean(v) # ortalama işlemi için
np.sum(v) # toplam alma
np.min(v) # min değer alma
np.max(v) # max değer alma
np.var(v) # varyans değerini hesaplar


#############################
# iki bilinmeyenli bir denklem çözümü
#############################

# 5*x0 + x1 = 12
# x0 + 3*x1 = 10

a = np.array([[5, 1], [1, 3]])
b = np.array([12, 10])
# kat sayılar bir array de tutulur sonuçlar ise diğer array de tutulur

np.linalg.solve(a, b)






