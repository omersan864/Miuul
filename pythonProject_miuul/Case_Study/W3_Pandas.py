# görev 1  titanic veri setini tanımlayınız
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("titanic")
df.head(10)
df.info()
"""
bu kısımda 
1. gerekli kütüphaneleri import ettim 
2. çıktı için gekeli ekran ayarlamaları yapıldı 
3. df = diyerek titanic veri seti çağrıldı 
4. head ve  info fonk. ile bilgiler alındı 
"""

# görev 2 titanic veri setinde kadın ve erkek yolcu sayısını bulunuz
df["sex"].value_counts()

"""
df[""]  parantez ile sütunlar arasından istediğim değişkeni seçebilir 
.value_counts() seçilen değişken içerisinde yer alan kategori
 veya değereri saydırabilirim 
"""

# görev3 her bir sütuna ait uniq değerlerin  sayısını bulunuz

for col in df.columns:
    print(df[col].value_counts())

[print(df[col].value_counts()) for col in df.columns]

"""
for col in df.columns:
    print(df[col].value_counts())
    
diyerek dataframe in her kolonunda "col" değişkeni ile gezdik 
print diyerek her aldığımız çıktıyı yazdırdık 
value_counts = > diyerek her bir değişkenin benzersiz uniq değerini yazdırdık 
"""
# görev 4 pclass değişkeninin uniq değerlerinin sayısını bulunuz

df["pclass"]

df["pclass"].value_counts()

[df[col].value_counts() for col in df.columns if col == "pclass"]

"""
df["pclass"] diyerek değişkenimize baktık ne var ne yok diyerek
df["pclass"].value_counts  diyerek  içerdiği her değerin benzersiz değer sayısına ulaştık 
aynı işlemi list compherension iile yapmaya çalıştım 

"""

# görev 5 pclass ve parc değişkenlerinin uniq değerlerini bulunuz

df["pclass"].value_counts()
df["parch"].value_counts()

new_col = ["pclass", "parch"]
df[new_col].value_counts()

"""
iki değişkenin benzersiz uniq değerlerini ayrı ayrı bulduk  (tek bir sorguda bulabilir miyiz )
iki değişkeni new_col adında bir listeye tanımladım  
ardından bu iki listeyi df[new_col] diyerek liste olarak verdiğim yapıyı dataframe içinde aratıyorum 
sonrasında listenin elemanlarını df de aratırken bulduğu takdirde value_count ile saydırıyorum 

"""

# görev 6 embarked değişkeninin tipini kontrol edin  tipini category olarak değiştirin ve tekrar kontrol ediniz

type(df["embarked"])    # pandas.core.series.Series
type(df[["embarked"]])  # pandas.core.frame.DataFrame

df["embarked"].dtypes  # asıl benden istenen bu == Out[8]: dtype('O') object


df["embarked"] = df["embarked"].astype('category')
"""
ilk adım olarak  df["embarked"] diyerek değişkenime eriştim ardından bu yapıyı type fonksiyonu içine
atarak değişkenimin tipini araştırdım 
!!! DİKKAT  == >> eğer tek parantez ile sorgu işlemini gerçekleştirirsem  pandas series olarak veriyor 
                  iki parantez kullanırsam pandas dataframe olarak veriyor 

==>>   type(df["embarked"]) ifadesi seçilen sütunu temsil eden Series nesnesinin veri tipini döndürürken, 
==>>   df["embarked"].dtypes ifadesi sadece seçilen sütunun veri tipini döndürür.

                  
 ===== df["embarked"] = df["embarked"].astype("category") =========
 
 df["embarked"] =   diyerek bu değişken üzerinde işlem yapacağımız belirttik 
 
df["embarked"] = df["embarked"].astype('category')
1. seçtik işlem yapacağız dedik yaş örneğini hatırla yaş değişkenini değiştirmek için yine yaş 
değişkenini kullanabiliyorduk burada da aynı mantık bulunmakta astype fonksiyonu ile değişkenin 
içerdiği veri türlerinin tipini değiştirdik 
 
"""

# görev 7 embarked değeri "C" olanların tüm bilgilerini listeleyiniz

df["embarked"] == "C"  # tüm data içinde embarked değeri c olanları true ve false olarak bulduk


new_df = df[df["embarked"] == "C"]

df["embarked"].head(30)

"""
df["embarked"] == "C" diyerek tüm data içinde embarked değeri C olanları True- False olarak seçtik

yukarda kullandığımız yapıyı df[] içine atarak yeni bir dataframe oluşturduk ve bu dataframe i 
bir değişken yapısı ile tuttuk 

"""


# görev 8 embarked değeri s olmayanların tüm bilgilerini gösteriniz
filtered_df = df[df['embarked'] != 'C']
# bu önceki sorunun aynısı fakat eşit değildir işaretini kullandık



# görev 9  yaşı 30 'dan küçük ve kadın yolcuların tüm bilgilerini gösteriniz
df[df["age"] < 30]  # 384 satır değer okuduk

gorev = df[(df["age"] < 30) & (df["sex"] == "female")]  # 147 ye düştük
"""
step by step  
öncelikle yaşı 30 dan küçük olanlara bir bakalım 
df["age"] > 30 diyerek verileri bir filtreden geçirdik 

bu yapıyı bir df[] içine yerleştirerek yeni bir dataframe oluşturduk ardından 
gorev diye bir değişkene atayarak çıktı almak için çalıştık 

"""


# görev 10 Fare'i 500 den büyük  ve yaşı 70 den büyük yolcuların bilgilerini gösteriniz

gorev = df[(df["fare"] > 500) & (df["age"] > 70)]

"""
bu kısımda önemli olan yapı eğer seçme işlemimize iki tane kısıt verirsek her bir kısıt 
değerini parantez içine almamız gerektiği 
"""
df[df["fare"] > 500].value_counts() # sağlama yapmak için koydum bunu


# görev 11  her bir değişkendeki boş değerlerin toplamıı bulun

"""
bu yazıyı sütun için özelleştirebilirsin

boş_değerler_toplamı=0
for sütun in df:
    for değer in df[sütun]:
        if pd.isna(değer):
            boş_değerler_toplamı += 1
"""

df.isnull().sum() # boş değerleri bulur ve sum ile toplar her değişken için

# görev 12 who değişkenini dataframeden çıkarın

df.drop("who", axis=1).head() # df.drop = df'den bir şey sileceğim
# df.drop("who") = who değişkenini sileceğim
# df.drop ("who", axis = 1) asxis 1 diyerek sütunlarda olduğunu belirttik


# görev 13  deck değişkenindeki boş değerleri en çok tekrar eden değeri (mode) ile doldurunuz
df.isnull().sum()  # kaç tane boş değer var görüntüledik her değişken için

model_value = df["deck"].mode()[0]  # en çok tekrar eden değeri buldum
# eğer birden fazla mod var ise [0] ifadesini kullanırız == "C" en çok tekrar eden
df["deck"].fillna(model_value, inplace=True)
# inplace = True kalıcı değişiklik yapmak için kullanılıyor
df.isnull().sum()  # kontrol adımı



# görev 14 age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz

df.isnull().sum()  # kaç tane boş değer var görüntüledik

model_value = df["age"].median()  # en çok tekrar eden değeri buldum
df["age"].fillna(model_value, inplace=True)
df.isnull().sum()  # kontrol adımı



# görev 15   survived değişkeninin pclass ve cinsiyet değişkenleri kırılımında sum , count , mean değerlerini bulunuz

df.pivot_table("survived", "pclass", "sex", aggfunc=["sum", "count", "mean"])
"""
df.pivot_table diyerek bir pivot tablo oluşturdum 
ilk olarak hesaplama yapılacak değişkeni verdim işlemler survived üzerinden yapılacağı için 
pclass ve sex değişkenleri ile kırılım olacağı için onları devamında verdim 
aggfunc diyererek aggrigate fonksiyonları kullandım 
birden fazla olduğu için liste yapısını kullandım 
"""



# görev 16 => 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın.
# Yazdığınız fonksiyonu kullanarak titanik veri
# setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
def yas(deger):
    if deger > 30:
        return (1)
    else:
        return (0)


df["age_flag"] = df['age'].apply(lambda x: yas(x))
df.head()



# görev 17  seaborn kütüphanesi içerisinden "TİPS" kütüphanesini tanımlayınız
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("Tips")
df.head()

df.isnull().sum()


# görev 18 time değişkeninin kategorilerine (dinner, lunch)
# göre total_bill değerlerinin  toplamını min ve max değerlerini bulun

df.pivot_table("total_bill", "time", aggfunc=["sum", "min", "max", "mean"])
"""
hesaplama yapılacak değişken total_bill olduğu için önce o değeri verdik 
# pivot_table () parantezin ilk argümanı kesişimlerde kullanıcak değişken
# satır indexinde ne olmasını istiyorsun der "sex"
# sütun indexinde ne olmasını istiyorsun der  "new_age"
"""


# görev 19 günlere göre totall_bill değerlerinin toplam min ve max ını bul

df.pivot_table("total_bill", "day","time", aggfunc=["sum", "min", "max", "mean"])
for col in df.columns:
    print(df[col].value_counts()) # neden 7 gün yok diye kontrol etmek istedim

df.groupby(["time", "day"]).agg({"total_bill": ["sum", "min", "max", "mean"]})
df.groupby(["day", "time"])["total_bill"].agg(["sum", "min", "max", "mean"])


# görev 20 lunc zamanında kadınn müşterilere ait
# total_bill ve tip değerlerinin toplam min ve max ve mean değerlerini bul

# Kadınlara ait total_bill ve tip değerlerinin toplam, min, max ve ortalama değerlerini hesapla
df[(df["time"] == "Dinner") & (df["sex"] == "female")].groupby("day").agg({"total_bill": ["sum", "min", "max", "mean"],
                                                                           "tip": ["sum", "min", "max", "mean"]})

df.pivot_table("total_bill")



# görev 21 size'ı 3 ten küçük totall_bill'i 10 dan büyük olan şiparişlerin ortalaması nedir
# df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"] ].count() burdan örnek aldım
df.loc[(df["size"] < 3 ) & (df["total_bill"] > 10)].mean()

df

# görev 23 total_bil_tip_sum adında yeni bir değişken oluşturun
# her müşterinin ödediği total_bill ve tip in toplamını versin

df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
df.head()

# görev 24 total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız
# ve ilk 30 kişiyi yeni bir dataframe'e atayınız.

new_alignment = df.sort_values("total_bill_tip_sum",ascending = False).head(30)

df1= pd.DataFrame(new_alignment)


