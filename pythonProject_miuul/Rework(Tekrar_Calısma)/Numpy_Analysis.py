#####################
# Numpy
######################

# neden numpy ? WHY numpy ?
# numpy array oluşturmak  (creating numpy arrays)
# numpy array özellikleri oluşturmak (attiributes of numpy array)
# yeniden şekillendirme (reshaping)
# Index seçimi
# slicing
# fancy index
# numpy da koşullu işlemler
# matemetiksel işlemler

# numpy python da nümerik işlemleri gerçekleştirmek için geliştirilmiş bir kütüphanedir

import numpy as np

# sabit tipte veri tutuyor ve bu yüzden hızlı

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

# amacım iki listeyi birbiri ile çarpmak olsun
# iki listenin elemanlarını gezmemiz ve bunları çarpıp yeni bir listeye eklememiz gerekiyor

ab = []

for i in range (0, len(a)):
    ab.append(a[i]*b[i])


a = np.array([1, 2, 3, 4])
a = np.array([2, 3, 4, 5])
a*b


##############################
# numpy array i oluşturma
##############################

import numpy as np

np.array([1, 2, 3, 4, 5])

type(np.array([1, 2, 3, 4, 5]))

np.zeros(10, dtype=int)
np.random.randint(0,10, size=10)
np.random.normal(10,4,(3,4))


############################
#numpy array özellikleri
##########################

import numpy  as np

# ndim : boyut sayısı
# shape : boyut bilgisi
# size : toplam eleman sayısı
# dtype : array veri tipi

a = np.random.randint(10,size=5)

a.ndim # bir boyutunu var
a.shape # içinde 5 eleman var
a.size # toplam 5 eleman var
a.dtype # int32 dedi



# elimizdeki bir numpay arrayinin boyutunu değiştirmek isteğimizde reshaiping kullanırız


np.random.randint(1,10,size=9)

np.random.randint(1,10,size=9).reshape(3,3) # 3 e 3 bir matris oldu


###########################
# Index seçimi
############################

import numpy as np

a = np.random.randint(10, size=10)

# sıfırıncı elemana gitmek istersek
a[0]

a[0:5] #slience dilimleme denir sıfırdan 5 e kadar git 5 dahil değil


# sıfırıncı indexteki elemanı değiştirmek istediğimizi düşünelim

a[0] = 999


# iki boyutlu bir array olursa bu kısımda bir seçim işlemini nasıl gerçekleştireceğiz


m = np.random.randint(10, size=(3, 5))

# ilk elemana erişmek istersek
#virgülden öncesi satırları sonrası ise sütunları temsil etmektedir
m[0,0]

# 1 e 1 indexine gitmek istersek hangi değer karşılık gelir
m[1,1]


m[2,3]
m[2,3] = 200 # yerine atama işlemi yapılır

m[2,3] = 20.3 # sadece int kısmını aldı





m[:,0] # bütün satırları seç sıfırıncı sütunu seç

# birinci satırı tüm sütunları seçmek istediğimiz düşünelim

m[1,:]

m[0:2, 0:3] # sıfırdan ikiye kadar git sütunlarda ise 3'e kadar git


########################
# numpy da koşullu işlemler (condition on numpy )
##########################

import numpy as np

v = ([1, 2, 3, 4, 5])
# bu array içindeki 3 ten küçük değerlere erişmek istiyoruz
# klasik döngü ile
ab = []
for i in v:
    if i < 3:
        ab.append(i)


# bu işlemi numpy ile nasıl gerçekleştiririz
import numpy as np

v =np.array([1, 2, 3, 4, 5])
v < 3 # her elemanın 3'ten küçük olup olmadığını kontrol eder

v[v < 3 ]

# vektörrel seviyeden  bir koşulun sağlanıp sağlanmadığını numpy hesaplıyor
# önemli bir farkındalık


########################
# matematiksel işlemler
###########################

import numpy as np
v =np.array([1, 2, 3, 4, 5])

v/ 5 # bütün elemanları tek tek beşe nöldü ve bize de numpy array i formatında bize verdi

v * 5 / 10 # peş peşe iki operatör de girilebilir

v ** 2  # bütün elemanlarının karesini de alabiliriz

# bu işlemleri operatörler aracılığı ile yaptık  methodlar aracılığı ile de gerçekleştirebiliriz

np.subtract(v, 1) # çıkarma işlemi
np.add(v, 1) # toplama
np.mean(v)
np.sum(v)
np.min(v)
np.max(v)
np.var(v) # varyans işlemi

########################
# numpy ile iki bilinmeyenli denklem çözümü
#########################

# 5*x0 + x1 = 12
# x0 + 3*x1 = 10
# bu kısımda yer alan 5, 1 ifadesi x0 ın katsayı değerlerini ifade eder
a = np.array([[5, 1], [1, 3]])
b = np.array([12, 10])
np.linalg.solve(a,b)