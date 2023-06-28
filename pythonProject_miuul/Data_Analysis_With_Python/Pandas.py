#####################################
#Pandas
######################################
# veri analizi ve veri manipülasyonu için sıklıkla kullanılmaktadır

# pandas series
# veri okuma  (reading data)
# veriye hızlı bakış  (quick look at data)
# pandas da seçim işlemleri (selection in pandas)
# toplulaştırma ve gruplaştırma  (aggregation & grouping)
# apply ve lambda
# birleştirme (join)

#############################
# pandas series
#############################

# pandas serileri tek boyutlu ve index değeri barındıran  bir veri tipidir
# pandas dataframe ise çok boyutlu ve indez değeri barından bir veri tipidir

import pandas as pd

s = pd.Series([1, 77, 12, 4, 5]) # bu bir metod dur
type(s) # verinin tipini öğrenebiliriz
s.index # kaç tane index değerinden oluşuyor
s.dtype #  # içerisinde verinin tip bilgisini verir int64
s.size  #  verinin eleman sayısı
s.ndim # verinin boyutunu verir
s.values  # verinin içindeki değerlere erişiriz
type(s.values) # bir pandas ifadesinin sonuna values ifadesi girdiğimizde  değerlere erişmek istedğimizde zaten index değeri ile ilgilenmediği için bunu numpy array i olarak verecektir
s.head(3)  # ilk üç değeri bize getirir
s.tail(3) # sondan 3 gözlem değerini getirir


##################################
#veri okuma data reading
##################################

import pandas as pd
# control tuşu ile pd üzerine sağ tık yaparsak diğer dosya türlerini nasıl okuyabileceğimiz öğrenebiliriz
df = pd.read_csv("C:/Users/omer/Desktop/customer_churn/WA_Fn-UseC_-Telco-Customer-Churn.csv")

df.head()


########################################
# veriye hızlı bakış
########################################
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()

df.tail() # dataframe  de son 5 veriyi verir
df.shape # dataframe nin boyutunu verir
df.info()  # datarame üzerinde bulunan satır değerleri ile ilgili bilgi verir type

df.columns # sütun isimlerini yazdırır
df.index   #  kaç tane satır değirine sahip olduğuna bakabilirsin

df.describe() # tanımlayıcı istatistiksel bilgiler verir
df.isnull().values.any()  # hiç boş değer var mı demek varsa True döner yoksa False
df.isnull().sum()  # df içerisinde kaç tane boş değer varsa yazdırır
df["sex"].head() # belirli sütunun ilk 5 değerini yazdırır
df["sex"].value_counts()  # belirli sütun içindeki değişkenlerin sayısını verir 577 female örnek olark

#########################################
# Pandas da seçim işlemleri selection pandas
##########################################

# bu konuda olan şeyler iyice ele alınmalı dikkatlice öğrenilmeli

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()

# indexler

df.index
df[0:13] # ilk 13'e kadar satır değerini okuduk bütün sütunlar dahil olmak üzere

df.drop(0,axis= 0 ).head() # axis fonksiyonu 0 olursa satırları ifade eder
# drop değeri silme işlemi için kullanılır

delete_indexes = [1, 3, 5, 7]

df.drop(delete_indexes, axis=0).head(10)
# yukarıda önce bir liste tanımladık liste içinde bulunan değerlerin silinmesini söyledik
# yapılan silme işlemi bir değişkene atanmadığı için kalıcılık ifade etmemektedir

# kalıcı hale getirmek istersek silme işlemini
# df = df.drop(delete_indexes, axis=0) diyerek kalıcı  hale getirebiliriz
# df.drop(delete_indexes, axis=0 inplace = True) # inplace diyerek de kalıcı hale getirebiliriz



##################################
#değişkeni index e çevirmek
##################################
"""
bir çok senaryoda elimizde ki  dataframelerin indexini değişkene  ya da
değişkeni index e  çevirme ihtiyacı olmaktadır 
"""
df["age"].head()
df.age.head()

df.index # 0 dan 891 e kadar değerler var

df.index = df["age"]

df.drop("age", axis = 1).head() # axis 1 diyerek sütun sildik ama kalıcı değil

df.drop("age", axis = 1, inplace= True)

df.head()


###################################
# Index değerini değişkene çevirmek
###################################

df["age"]  = df.index

df.head()
df.drop("age", axis = 1, inplace= True)

df = df.reset_index().head()

df.head()



##################################
# değişkenler üzerine işlemler
###################################

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns',None)
df = sns.load_dataset("titanic")
df.head()

"age" in df # True dönüyor (bu değişken bu veri setinde bulunuyor mu ?)

df["age"].head()
df.age.head()

df["age"].head()
type(df["age"].head()) # pandas series

"""
bir değişken seçerken sonucu seri veya dataframe alabiliriz 
bir fonksiyon alacağız ve bir dataframe işlemi yapmak üzere uygulamaya
koyulduğuuzda ben bir değişken seçeyim dediğinizde -------df["age"]-------
bu şekilde fonksiyon çalışmayacak çünkü dataframe bekliyor
şimdi işlem yaparken içinde gönderdiğin değerin tip bilgisi pandas series  de 
olabilir  dataframe de olabilir içine gönderdiğin değerin tip bilgisini bir sorgula mesela
bu örnekte tek bir köşeli parantez ile tip bilgisi sorguladığında 
pandas series olurken   devamında iki tane köşeli parantez koyarsan bu sefer
dataframe dönüşüyor 

------TİP  HATALARINA DİKKAT

BİR DEĞİŞKEN SEÇERKEN SONUCU DATAFRAME OLARAK DA ALABİLİRSİN 
PANDAS SERİES DE OLARAK ALABİLİRSİN 
TEK PARANTEZ KULLANIRSAN PANDAS SERİES OLARAK ALIRSIN 
AMA İKİ PARANTEZ KULLANIRSAN SONUC DATAFRAME OLARAK KARŞIMIZ ÇIKAR

ÖRNEK : df[["age"]].head() ===>> bu bir dataframe
        
        df["age"].head()  ===>> bu da bir pandas series 
        
        burdan alınan değerler üzerinden işlem yaparken farkı gözetmek gerekir 
"""
type(df["age"])

# birden fazla değişken seçmek için

df[["age", "alive"]]

#aşağıda birden fazla sütun seçme işlemini gerçekleştirdik tip değeri datafreme çünkü verdiğimiz değer de liste
col_names = ["age", "adult_male", "alive"]

df[col_names]


#elimizdeki dataframe' yeni bir değişken eklemek için
# age2 diye kolon ekledik ve değerlerini yaş değişkeninin karesini alarak elde ettik

df["age2"] = df["age"] ** 2

df["age3"] = df["age"] / df["age2"]

df.drop("age3", axis=1).head()

#birden fazla sütun değerini silmek için

col_names = ["age", "adult_male", "alive"]
df.drop(col_names , axis=1).head()

#belirli bir string ifadeyi barındıran değişkenleri silmek istersek

df.loc[:, df.columns.str.contains("age")].head() #içinde age bulunan sütunları seçtik

df.loc[:, ~df.columns.str.contains("age")].head() #age olan sütunları sildim



####################################
# LOC & ILOC
####################################

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns',None)
df = sns.load_dataset("titanic")
df.head()

# iloc : integer based selection

# virgülden öncesi satırları sonrası sütunları temsil ediyor

df.iloc[0:3] # sıfırıncı indexten başlayarak 2. index değerine kadar tüm sütunlar
df.iloc [0,0]

# loc : label based selection
df.loc [0:3]  # data frame de verilen index değerlerinden ----0, 1, 2, 3------- değerlerini alır

df.iloc[0:3, 0:3] # 0'dan başlayarak 3'e kadar satır ve sütun seçer

df.loc[0:3, "age"] # 0, 1, 2, 3 satır alır ve sadece age sütununu verir

col_names= ["age", "embarked", "alive"]

df.loc[0:3, col_names] # birden fazla değişkeni de alabilir



##################################
# Koşullu seçim (conditional selection)
#################################

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns',None)
df = sns.load_dataset("titanic")
df.head()

# bu veri setinde yaşı 50 den büyük olanlara erişmek istiyorum

df[df["age"] > 50].head() # veri setinde yaşı 50 den büyük olanlar

df [df["age"] > 50].count() # yaşı 50 den büyük olan kaç kişi var

df[df["age"] > 50 ]["age"].count()

df.loc[df.age > 50,"class" ].head()

df.loc[df.age > 50, ["age", "class"]].head() #bir koşul + 2 tane ssütun seçtik
#yaşı 50 den büyük olanlar ve sınıfları


#yaşı 50 den büyük olan erkekleri seçmek için

df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"]].head()
# iki koşul ve 2 sütun değeri seçtik koşul değerlerini paranteze almayı unutma

df.loc[(df["age"] > 50)
       & (df["sex"] == "male") &
       (df["embark_town"] == "Southampton"),
       ["age", "class"]].head()
# 3 tane sorgu ve 2 tane sütun değeri seçili

df["embark_town"].value_counts()

df_new = df.loc[(df["age"] > 50)
            & (df["sex"] == "male") &
            ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
            ["age", "class","embark_town"]]

df_new["embark_town"].value.counts()

"""
1. yaşın 50 > büyük olması 
2. eş zamalı olarak erkek olması gerekir 
3. liman (embar_town) southampton ya da cherbourg da olanlar (burda ya da var dikkar)
"""