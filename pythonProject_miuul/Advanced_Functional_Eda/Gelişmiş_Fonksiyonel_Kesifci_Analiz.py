######################################
# GELİŞMİS FONKSİYONEL VERİ ANALİZİ
########################################

# 1. Genel Resim
# 2. Kategorik Değişken Analizi (Analysis of categorical Variables)
# 3. Sayısal Değişken Analizi (Analysis of Numerical Variables)
# 4. Hedef Değişken Analizi  (Ananlysis of Target Variable)
# 5. Koreleasyon Analizi    (Analysis of Correlation)

###########################
# 1. Genel Resim
###########################
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)
df = sns.load_dataset("titanic")

df.head()  # ilk 5 değer
df.tail()  # son 5 değer
df.shape  # boyutu nedir satır ve sütun (891,15)
df.info()  # tip hakkında bilgi
df.columns  # kolon  isimleri
df.index  # kaç satır değeri var
df.describe().T  # tanımlaycı istatistik değeri
df.isnull().values.any()  # eksik değer var mı  True - False
df.isnull().sum()  # eksik değerler toplamı


def check_df(dataframe, head=5):
    print("--------------Shape --------- ")
    print(dataframe.shape)
    print("-------------dtypes----------")
    print(dataframe.dtypes)
    print("--------------head------------")
    print(dataframe.head(head))
    print("--------------Tail------------")
    print(dataframe.tail(head))
    print("--------------NA---------------")
    print(dataframe.isnull().sum())
    print("--------------Quantiles---------")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)
    # print(dataframe.describe([0, 0.5, 0.95, 0.99, 1]).T)


check_df(df)

df = sns.load_dataset("tips")

check_df(df)

"""
bu kod dizininde check_df adında bir fonksiyon tanımladık ve içerisine  günlük hayatta kullanabileceğimiz
data setlerini tanımlamak için gereken fonksiyonları attık bunlar (boyut bilgisi tip bilgisi, tanımlayıcı istatistikler
,eksik gözlem değerinin olup olmadığı gibi istersek daha da fazlasını yerleştirebiliriz) ve işin kullanışlı kısmı 
fonksiyonu bir kere oluşturduktan sonra diğer data setler için de otomatik olarak kullanabilmemiz herhangi bir data 
sete genel bir bakış atmak istersek kullanabileceğimiz aşırı faydalı bir fonksiyon 
"""

###########################
# 1. Kategorik değişken analizi
###########################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)
df = sns.load_dataset("titanic")

df.head()  # ilk 5 değer

# tek bir değişkeni analiz etmek istiyorsak
df["embarked"].value_counts()  # sınıf sayılarına ulaşabiliriz
df["sex"].unique()  # 2 değerden oluşuyor male ve female olmak üzere
df["sex"].nunique()  # 2 değişkenden oluşuyor

"""
bu bölümde programatik bir şekilde fonksiyonel olarak genellenebilirlik 
kaygısıyla  DEĞİŞKEN TİPLERİNİ YAKALAMAYI  bunların özelinde bir fonksiyon
yazma işlemini  gerçekleştirmiş olacağız 

elimizde tek bir değişken olduğunda  df["embarked"].value_counts()  kullanarak 
sınıf sayılarına erişebiliriz        df["sex"].unique()
                                     df["sex"].nunique()

önemli şimdi elimizdeki data set küçük olduğu için herşeyi görebiliyoruz
fakat data set büyüdüğünde onlarca değişkenin özelliğini tek tek analiz 
etme yerine genellenebilir bir fonksiyon yazacağız

öyle bir şey yapalım ki 

datasetin içinden olası bütün kategorik değişkenleri seçsin
bunu birkaç adımda yapacağız 
1. öncelikle tip bilgisine göre seçeceğiz 
2. başka tipte görünen a

"""

df.info()

# dytype = category  & bool  & object  3 tane kategorik değişken var

cat_cols = [col for col in df.columns if str(df[col].dtype) in ["category", "bool", "object"]]
"""
1.cat_cols adında bir liste oluşturduk comphrension tarzında yazalım kodumuzu
2.col for col in df.columns diyerek bütün kolonlarda geziyoruz
3.gezdiğin değerlerin tip bilgisini kontrol et eğer tip bilgisi object categoryi bool içeriyor ise bunları seç

df.columns içinde  col olarak geziyor df[col] diyerek bunu yakalıyoruz 
df[col].dtype diyerek tip bilgisini alıyoruz 
str(df[col].dtype) diyerek aldığımız tip bilgisini stringe çeviriyoruz 
str(df[col].dtype) in ["category" , "bool", "object"]  diyerek bunların içinden biri olup olmadığını soruyoruz

df["sex"].dtypes
Out[22]: dtype('O')  Object bilgisi geldi 

str(df["sex"].dtypes)
Out[23]: 'object'

str(df["sex"].dtypes) in ["object"]
Out[24]: True

===>>> bu kısımda yapılan işlem ilgili değişkenin tip bilgisini string e çevirip
       burda girmiş olduğumuz liste içinde var mı bak demek  

"""
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]
"""
bu kısımda int olarak görünen ama kategorik olan sayısal değişkenleri nasıl bulacağımıza bakacağız 
df["survived"].value_count() ==> 0 > 549   &     1 > 342 sıfır ve bir olarak ifade ediliyor

num_but_cat  isimli boş bir liste oluşturuyoruz 

tipi integer ve float olup eşsiz  sınıf sayısı belirli bir değerden düşük olanları yakala  diyeceğiz 
num_but_cat = []

şu yaklaşımı geliştiryorum :  tipi int ve float olan değişkenleri bul bunların eşsiz sınıf sayısına bak 
mesela  : yaşın eşsiz sınıf sayısı  80'den fazla  bu o zaman kategorik değildir
çünkü ölçülebilirlik değeri taşımıyor  

ama survided e baktığımızda tip bilgisi int ama sınıf sayısı 2  bunlar int değil category dir diyeceğiz
öyleyse buraya bir koşul koyacağız 

eğer eşsiz değer sayısı 10 dan küçük ise ve bunların tipi int ve float ise 
bu bizim için nümerik görünümlü fakat category bir değişkendir 

col for col in df.columns if df[col].nunique < 10 and  df[col].dtype in ["int", "float"]

"""
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtype) in ["category", "object"]]
"""
çalıştığımız veri setinde yine object ve category tipinde veriler var fakat 
bu değişkenlerden birinin sınıf sayısı çok fazla olabilir 
örnek olarak : datasette kişi isimleri yer alırsa satır sayısı kadar kişi ismi 
olabilir  (bunlara kardinalitesi yüksek değişkenler denir , ölçülemeyecek kadar 
ölçüm değeri taşıyamayacak kadar fazla sınıfı vardır anlamına gelir  )

öyle bir şey yapmamız gerek ki kategorik gibi olan ama programatik olarak da 
bu veri setindeki kategorik tipte olduğu halde kategorik olmayan değişkenleri 
de yakalayabiliyor olmamız lazım  
"""
cat_cols = cat_cols + num_but_cat  # ekleme yapıyoruz bu kısımda

# eğer cat_but_car değişkeni içerisinden değer olursa bunu cat_cols dan çıkarmamız gerekir

cat_cols = [col for col in cat_cols if col not in cat_but_car]
"""
cat_cols = [col for col in cat_cols if col not in cat_but_car]

>>> col ismi ile cat_cols üzerinde geziniyoruz eğer col ismi cat_but_car da yoksa 
cat_cols e ekliyoruz


"""

df[cat_cols].nunique()
"""
df[cat_cols].nunique()
Out[16]: 
sex            2
embarked       3
class          3
who            3
adult_male     2
deck           7
embark_town    3
alive          2
"""

# cat_cols içerisinde olmayan değişkenleri seçmek için ==>>Out[17]: ['age', 'fare']
[col for col in df.columns if col not in cat_cols]



df["survived"].value_counts()
100 * df["survived"].value_counts() / len(df) # dataframen'in boyut bilgisi len
"""
Aşağıda yazacağımız def cat_summary (dataframe, col_name):
value_counts unu (alsın benzersiz değer sayısı, hangi sınıftan kaçar tane var)

birde sınıfların yüzdelik bilgisini yazdıralım  
==>> 100 * df["survived"].value_counts() / len(df)
"""
def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))

    print("###########################################################")
"""
print(pd.dataframe({col_name: dataframe[col_name].value_counts(),
                    "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
                             
            
1. çıktının düzgün bir formda olmasını istediğim için bir dataframe koyuyoruz
2.dataframe içine bir sözlük ekliyoruz bu sözlükte bir "key" & "value" var 

key = >> col_name ile temsil edilmiş dataframe[col_name].value_counts() benzersiz değer saydırılmış
value = >> ratio ile temsil edilmiş  ; saydırılan değer 100 ile çarpılıp df uzunluğuna bölünmüş
"""

cat_summary(df, "sex")

for col in cat_cols:
    cat_summary(df, col)
#yukarıda bütün değişkenleri for ile dolaştık




#############################################
# kategorik analiz II
#############################################
"""
İş genellenebilirlik ve ölçeklenebillik kaygısı ile ilerlediğinde fonksiyonel olarak ilerlemek gerekiyor 

"""



def cat_summary(dataframe, col_name, plot= False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))

    print("###########################################################")

    if plot:
        sns.countplot(x = dataframe[col_name],data=dataframe)
        plt.show(block=True)
"""
cat_summary fonksiyonuna bir özellik daha eklemek istersek (GRAFİK)

bir kategorik değişken sorduğumuzda bunun bilgilerine ek olarak sütun grafiğini de versin 

    if plot:
        sns.countplot(x = dataframe[col_name],data=dataframe)
        plt.show(block=True)
        
eğer plot argümanı  True ise sns içersinden  countplot fonksiyonunu getir 
ki bunun x değeri dataframe içerisindeki sütun olsun ("sex, adult_male", "embarked") 
data = dataframe de data setimiz olsun 
aşağı inip göster diyoruz 
cat_summary(df, "sex", plot=True)
"""


cat_summary(df, "sex", plot=True)

for col in cat_cols:
    if df[col].dtypes == "bool":
        print("foğdıpvbijfefff")
    else:
        cat_summary(df, col, plot=True)
#eğer cat_summary fonksiyonu tüm değişkenlere uygulamak istersek yukarıdaki döngüyü kullanıyoruz


df["adult_male"].astype(int)

for col in cat_cols:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)
        cat_summary(df, col, plot=True)

    else:
        cat_summary(df, col, plot=True)




def cat_summary(dataframe, col_name, plot= False):

    if dataframe[col_name].dtypes == "bool":
        dataframe[col_name] = dataframe[col_name].astype(int)
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))

    print("###########################################################")

    if plot:
        sns.countplot(x = dataframe[col_name],data=dataframe)
        plt.show(block=True)

    else:
        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))

        print("###########################################################")

        if plot:
            sns.countplot(x=dataframe[col_name], data=dataframe)
            plt.show(block=True)

