##########################
# Pandas
#############################
# pandas series
# veri okuma
# veriye hızlı bakış
# pandas da seçim işlemleri
# toplulaştırma ve gruplaştırma
# apply ve lambda
# birleştirme (join) işlemleri

####################
# pandas Series
######################
# pandas series en yaygın kullanılan veri yapılarıdır
# tek boyutlu ve index bilgisi barındıran bir veri tipidir
# pandas dataframe ise çok boyurlu ve index bilgisi barındıran veri tipidir

import pandas as pd
s = pd.Series([10, 77, 12, 4, 5]) # bu şekilde bir seri oluşturabiliriz  bu bir metoddur
# bu der ki bana liste veya farklı tipte bir veri ver ki  ben bunu pandas serisine çevireyim
# çıktı olarak sol tarata index bilgisi bulunur  # index bilgisi bir iç özellik

type(s)

# index metodunu kullanarak serisinin index bilgisine erişebiliriz
s.index # sıfırdan 5 e kadar birer birer artacak şekilde index i olduğunu ifade ediyor

s.dtype # içindeki bilginin tip bilgisini verir  Out[33]: dtype('int64')

s.size # içinde barınan eleman sayısına erişmek istersek bu mthodu kullanabilriz

s.ndim # boyut bilgisine erişebiliriz  tek boyutludur seriler

s.values # serinin içindeki değerlerin kendilerine erişmek istersek Out[34]: array([10, 77, 12,  4,  5], dtype=int64)

# bak normalde series ile çalışıyoruz ama burda numpy array dönüyor
# çünkü values diyerek biz aslında index bilgisini boşver diyoruz
type(s.values) # Out[35]: numpy.ndarray

s.head() # seri içindeki ilk 5 gözlem değerini default olarak getirir

s.tail() # dersek de sondan 5 değeri default olarak görmüş oluruz

###################################
# Veri Okuma (reading data)
###################################

import pandas as pd
df = pd.read_csv("datasets/advertising.csv")

df.head()
# pandascheatsheet diyerek pandas da kullanılan fonksiyon ve metodları bulabilriz


######################
# veriye hızlı bakış (quick look at data )
#########################

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()
"""
survived değişkeni bağımlı değişkendir 1 yazması o yolcunun hayatta olduğunu gösterir 
"""
df.tail()  # sondaki değerlere göz atabiliriz
df.shape  # boyut bilgisi için Out[45]: (891, 15)

df.info()  # detaylı bilgi almak istersek  değişkenler değişken tipleri
# info bize 891 tane gözlem birimi olduğunu ifade etmiş
# 0 to 890   a kadar gittiğini ifade etmiş
# alt kısımda ise değişkenler değişkenlerin tipleri ve değişkenlerde kaç tane dolu gözlem var
# pandas da çalışırken denk gelebileceğimiz object ve category türündeki değişkeler kategorik değişkendir (object)


# bu data framenin değişkenlerinin isimlerine erişmek istersek
df.columns

df.index # index bilgisine erişmek istersek Out[49]: RangeIndex(start=0, stop=891, step=1)


# elimizdeki bir dataframenin özet istatistik bilgisine erişmek istersek
df.describe().T
# sonuna .T koyarak bunun TRANSPOZUNU al diyerek daha okunabilir bir formatta gelmesini sağlıyoruz z

# detaylarına girmeden sadece veri setinde en az bir tane dahi olsa  eksiklik var mı
df.isnull().values.any() # Out[53]: True
# bu valueslerden herhangi birisinde isnull durumu var mı demek için de any() ifadesi kullanılır



# peki yine hızlı şekilde bir veri setinde detaylara girmeden
# değişkenlerdeki eksiklik durumu incelenmek istenirse ne yapılır
df.isnull().sum()
"""
df.isnull() ==>> bunu bir değerlendirelim  bize True- False  değerleri döndü
dikkat True = 1'i & False = 0'ı  temsil eder bu durumda eğer elinizdeki bir
True - False array'ine   örneğin sum() atarsanız ya da min() atarsanız 
True'ları bir  False'ları da sıfır olarak sayacaktır 

her bir değişkende kaç tane eksik değer olduğu bilgisini hesaplamış oldu 

df.isnull().sum()
Out[56]: 
survived         0
pclass           0
sex              0
age            177
sibsp            0
parch            0
fare             0
embarked         2
class            0
who              0
adult_male       0
deck           688
embark_town      2
alive            0
alone            0
dtype: int64


"""

# bir kategorik değişkende kaç tane sınıf olduğu  ve bu sınıfların  kaçar tane olduğu bilgisine erişmek istiyoruz
# örnek cinsiyet kategorik değişken kadın- erkek , kaç erkek var gibi
# bir dataframe den değişken seçmek istediğimizde köşeli parantez gireriz
# değişkenin ismini tırnak içinde gireriz
df["sex"].head() # diyerek seçtiğimiz değişkeni gözlemleyelim
# amacımıza geri dönelim kateorik değişkenin sınıfları  ve bunların kaçar tane olduğu
df["sex"].value_counts()





#####################
# Pandas da seçim işlemleri (selection in pandas)
####################

import pandas as pd
import seaborn as sns
df = sns.load_dataset("titanic")
df.head()

# öncelikle dış özellik diyebileceğimiz indexlerden başlayalım

df.index  # index'e gitmek istersek Out[61]: RangeIndex(start=0, stop=891, step=1)

# bir slice (dilimleme ) işlemi yapmak istersek
df[0:13]  # sıfırıncı indexten 13'üncü indexe kadar git  diyecek olursak
# BELİRLİ BİR ARALIKTA SEÇİM İŞLEMİ GERÇEKLEŞTİ
# !!!! 13 dahil değil unutma DİKKAT

# indexlerde silme işlemi de gerçekleştirebilriz
df.drop(0, axis=0).head()
"""
df.drop() diyerek  senden birşey sileceğim bilgisini verdim

df.drop(axis=0) diyerek satılardan mı sütunlardan mı sileceğimi belirttim = satır

df.drop(0,axis=0) hangi index değerini sileceğimi belirttim 

df.drop(0, axis=0).head() gözlemlemek için head() dedik

böylelikle ilk satıda bulunan index değerini sildik
"""

# eğer birden fazla index değerini silmek istersek

delete_index = [1, 3, 5, 7]

df.drop(delete_index, axis=0).head(10)
# bu silme işlemi kalıcı değildir
# işlemi kalıcı hale getirmek için 2 yol izlenebilir
# 1. yol ==> df = df.drop(delete_index,axis=0).head(10) diyebiliriz
# yani yaptığımız işlemi df değişkenine atarız

# 2. yol inplace=True argümanını atayabiliriz
# df.drop(delete_index,axis=0, inplace=True).head(10) diyebiliriz


#####################
# Değişkeni Indexe Çevirmek
#####################

# öncelikle bir değişkeni seçmek için şu şekilde bir seçim yapabiliriz
df["age"].head()
df.age.head() # diyerek de seçim işlemini gerçekleştirebiliriz

# şimdi yaş değişkenini index değerine atmak istiyorum
df.index  # dediğimizde ne görüyoruz == veri setinin index bilgisini görüyoruz
# şimdi bu index yerine (başka bir değişken de olabilir ) yaş değişkenini atamak istiyoruz

df.index = df["age"] # dersek işlemimiz gerçekleşmiş olacaktır
# df.index i seç ve çalıştır == yaş değerinin atandığını görürüz

# madem bunu index olarak ekledik artık değişken olarak ihtiyaçımız olmadığını düşünürsek
# bunu nasıl silebiliriz

df.drop("age", axis=1).head() # diyerek silme işleminin sütunlardan olduğunu ifade ettik

# bu değişikliği kalıcı bir şekilde yapalım ve değişkenlerin arasından yaş değişkenini uçuralım


df.head()


#########################
# Indexi değişkene çevirme
#######################

df.index
df["age"] = df.index

df.head()  # kontrol edelim
"""
df.[] dediğimizde eğer girecek olduğumuz string ifade bu dataframe içinde varsa 
bu durumda bu değişken seçilirken 
EĞER GİRİLEN İFADE DATAFRAME İÇİNDE YOKSA YENİ DEĞİŞKEN EKLENDİĞİ ANLAŞILIR 

BİR dataframe yeni değişken eklemek için o dataframe içinde olmayan bir ifade 
girersek yeni değişken ekleriz (en sona ekliyor )
"""
# yukarıda yaptığımız işlemler 1. yol du
# şimdi yaptıklarımız silip 2. yolu deneyelim

df.drop("age",axis=1, inplace=True)
df.head() # kontrol ettik ve yaş değişkeni gitti

df.reset_index().head()
# index kısmında yer alan değerleri silecek ve sütun olarak ekleyectir

df = df.reset_index()  # diyerek atama işlemini gerçekleştirebiliriz

df.head()

#############################
# Değişkenler üzerinde İşlemler
#############################
# satır indexleri üzerinde çalıştık şimdi sütunlar üzerinde işlemler gerçekleştireceğiz (değişkenler)
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns',None)
df = sns.load_dataset("titanic")
df.head()

# herhangi bir değişkenin adının o dataframe içinde olup olmadığını sorgulamak için
"age" in df # cevap bool türünde dönecektir bu sorunun cevabı == True

# özellikle bir değişken seçmek istersek iki şekilde yapılır
df["age"].head()
df.age.head()
#ÇIKTI DEĞERİ PANDAS SERİSİ Mİ YOKSA DATAFRAME DİKKAT ETMEK GEREKİYOR
type(df["age"])  # bunun çıktısı pandas series
df[["age"]].head()
type(df[["age"]]) # bunun çıktısı dataframe
# önemli olan dataframe şeklinde çıktı almak

df[["age", "alive"]].head()  # birden fazla değişken seçebiliriz

col_names = ["age", "adult_male", "alive"]
df[col_names].head()
type(df[col_names]) # yine dataframe :))

# elimzdeki veri setine yeni bir değişken eklemek istersek
# eğer df[] içine df'de olmayan bir isim girersen ekleme otomatik olur

df["age2"] = df["age"]**2 # var olan yaşın karesini alıp ekledik

df["age3"] = df["age"] / df["age2"]
# iki yeni değişkeni var olan değişkenlerin üzerinden oluşturduk


# eğer bir değişkeni silmek istersek ne yapacağız
df.drop("age3", axis=1).head()

# eğer birden fazla değişkeni silmek istersek önce silmek istediklerini listeye at
col_names = ["age", "adult_male", "alive"]
df.drop(col_names,axis=1).head()


# belirli bir string ifadeyi barındıran değişkenleri silmek için ne yapabiliriz

df.loc[:, ~df.columns.str.contains("age")].head()
# tilda bunun dışındakileri seç onlar kalsın age leri sil





#########################
# İloc ve loc
#########################
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

# iloc : integer based selection

df.iloc[0:3]
df.iloc[0,0] # virgülden öncesi satırları sonrası sütunları temsil etmektedir
# yukarıda sıfırıncı satır ve sıfırıncı sütunu getir dedik

# loc : label based selection
# label bases selection = mutlak olarak isimlendirmenin kendisini seçiyor
# df.loc[0 : 3] dediğimizde index değerleri = 0, 1 , 2 ,3
df.loc[0:3]

# satırlarda 0'dan 3'e kadar gitmek istiyorum  ama sütunlardan bir değişken seçmek istiyorum
df.iloc[0:3,"age"] # burada value error veriyor "age" yerine int değer girmek gerek
df.iloc[0:3,0:3]
df.loc[0:3,"age"]


# birden fazla değişkeni isimlerini ifade ederk seçebiliriz
col_names = ["age", "embarked", "alive"]
df.loc[0: 3 , col_names]



#####################
# Koşullu seçim işlevleri
#######################
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

# bu veri stinde yaşı 50 den büyük olanlara erişmek istediğimizi düşünelim

df[df["age"] > 50].head()

df[df["age"] > 50]["age"].count() # yaşı 50 ' den büyük 64 kişi varmış

# yaşı 50 den büyük olan kişilerin  yolculuk sınıfı değerlerini nasıl öğreniriz

df.loc[df["age"] > 50, "class"].head()# yaşı 50 den büyük olanların sınıf bilgisi geldi

# eğer 50 yaşından büyük yolcuların sınıf ve yaş bilgisini almak istersek
# yani bir koşul verip 2 değişken(sütun) bilgisini almak istersek listelerden faydalanabiliriz

df.loc[df["age"] > 50 , ["age", "class"]].head() # 50 yaşından büyük yolcuların yaş ve sınıf bilgileri


# şimdi 50 yaşından büyük ve erkek olan yolcuların yaş ve sınıf bilgilerini almak istersek
# yani aynı anda iki tane koşul ve iki tane değişken (sütun) bilgisi isteyeceğiz
# bu kısımda önemli nokta eğer iki koşul varsa bu koşullar ayrı ayrı paranteze alınmalıdır
df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"] ].count()


# 50 yaşından büyük erkek ve cherbourg limanından (embark_town) limanından binen yolcuların yaş ve sınıf bilgisi

df.loc[(df["age"] > 50) &
       (df["sex"] == "male") &
       (df['embark_town'] == "Cherbourg"), ["age", "class", "embark_town"]].head()


# 50 yaşından büyük erkek ve cherbourg limanından ve Southampton (embark_town)
# limanından binen yolcuların yaş ve sınıf bilgisi

df["embark_town"].value_counts()

df_new = df.loc[(df["age"] > 50) &
                (df["sex"] == "male") &
                ((df["embark_town"] == "Cherbourg") | (df['embark_town'] == "Southampton")),
                ["age", "class", "embark_town"]]

df_new["embark_town"].value_counts()

"""
1. yaşın 50 den büyük koşulunu verdik 
2. bununla eş zamanlı olarak cinsiyetin erkek olması koşulunu verdik 
3. 1.ci ve 2.ci koşul ile ez zamanlı olarak bir koşul daha verdik 
3.1 => ilk iki koşulu sağlayanlar ve bindiği liman Cherbourg YA DA Southampton olanlar 
4.  bütün koşulları sağlayanların yaşı sınıfı ve bindiği limanı listeledik 
"""

#################################
# Toplulaştırma ve Gruplama (Aggregation & Grouping)
#################################

# Toplulaştırma nedir : bir veri yapısı içerinde yer alan değerlerin toplu şekilde temsil edilmsi
# özet istatistikler bunun için güzel bir örnektir
# bir array içindeki elemanları saydırırsak tek bir değer döner
# - Count()
# - first()  ilk değer
# - last()   son değer
# - mean()   ortalama
# - median()
# - min()
# - max()
# - std()
# - var()
# - sum()
# -pivot table


import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns',None)
df = sns.load_dataset("titanic")
df.head()

# kadın ve erkeklerin yaş ortalamasına erişmek istiyoruz

df["age"].mean() # bu şekilde herkesin yaş ortalamasını alabiliriz

df.groupby("sex")["age"].mean()

df.groupby("sex").agg({"age": "mean"})

# kadın ve erkeklerin yaş ortalamasına ve toplamına  erişmek istiyoruz

df.groupby("sex").agg({"age": ["mean", "sum"]})

# kadın ve erkeklerin  yaş ortalaması ve toplamına erişmek istiyoruz ve hayatta kalma ortalamalarına bakalım
df.groupby("sex").agg({"age": ["mean", "sum"],
                       "survived": "mean"})

df.groupby(["sex", "embark_town"]).agg({"age": ["mean"],
                                      "survived": "mean"})
"""
çıktı sonucu oluşan tabloda 

1. cinsiyete göre veri kadın ve erkek olarak bölünmüş 
2. daha sonra embark a göre veri seti bölünmüş 

"""




df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean"],
                                      "survived": "mean"})
# yukarıda cinsiyete , bindiği limana ve yolcu sınıfına göre hayatta kalma ve yaş ortalamalarına bakabiliriz



df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean"],
                                                 "survived": "mean",
                                                 "sex": "count"})
"""
kadın ve erkeklerin bindikleri limanları ve yolculuk sınıfları gözlemleyebiliyoruz 
aynı zamanda  bir limandan binen erkek veya kadınların birinci sınıfının yaş ortalamasını 
hayatta kalma ortalamasını ve o sınıfta bulunan yolcu sayısını bulabiliyoruz 

örnek bir yorum 

cherbourg limanından birinci sınıfta yolculuk eden kadınların yaş ortalması 
36 dır hayatta kalma oranı %90 dır  ve 43 tane kadın birinci sınıf yolcu vardır
cherbought de binen 
"""

##############################
# Pivot Tablo Pivot Table
##############################

import pandas as pd
import seaborn as sns

pd.set_option('Display.max_columns',None)
df = sns.load_dataset("titanic")
df.head()


# yaş ve gemiye binme lokasyonunu ifade eden bu iki değişken açısından pivot tablo oluştur


df.pivot_table("survived", "sex", "embarked")
# yukarıdaki kod da cinsiyet ve liman bilgisine göre hayatta kalma ortalamalarına baktık


df.pivot_table("survived", "sex", "embarked", aggfunc="std")
# yukarıda cinsiyet ve liman bilgisine göre  hayatta kalmanın standart sapmasını aldık

# kırılım cinsiyet değişkenine göre yapılmıştır
df.pivot_table("survived", "sex", ["embarked", "class"])
# yukarıda cinsiyete göre limana göre ve yolculuk sınıfına göre haytta kalma ortalaması verilmiştir


# şimdi yaş değişkeni ve cinsiyet değişkeninin ilişkisi için pivot tablo oluşturalım
# yaş değeri numeric olduğu için öncelikle categoric değişkenedönüştürmek gerek

# cut() kullanımında parantez içine ilk neyi böleceği verilir df["age"]
# nasıl böleceği verilir liste ile verebiliriz [0, 10, 18, 25, 40, 90]
df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])
"""
pd.cut ve pd.qcut fonksiyonları elimizdeki sayısal değişkenleri kategorik
değişkenlere çevirmek en yaygın kullanılan iki ayrı fonksiyondur 

genelde sayısal değişkenimizi hangi kategorilere bölmek istediğimizi biliyorsak
bu durumda cut fonksiyonu kullanılır 

elimizdeki sayısal değişkeni tanımıyor dolayısıyla çeyreklik değerlere göre bölünsün
istiyorsanız bu durumda qcut kullanılır 

örnek: 
    yaş değişkenini kategorik değişkene çevirmek istediğimizde yaş değişkeni 
adındaki değişkeni tanıyorum yani diyebilirim ki 0-10 arasına çocuk de 
10-18 arasına genç de  18-30 arasına da genç de  30-50 arasına orta yaşlı de 
gibi . dolayısı ile bu değişkeni tanıyoruz o yüzden bu değişkeni kategorik değişkene 
çevirirken cut () fonksiyonunu kullanabiliriz  eğer bir kategori tanımlayamıyorsak
qcut () fonksiyonu kullanırız 


"""
# 0-10 , 10-18 gibi kategoriler oluşur
# sıfır hariç 10 dahildir diyeceğiz   diğer kategori için 10 dahil 18 hariçtir

# yaş kırılımında da hayatta kalma oranını incelemek istersek

# pivot_table () parantezin ilk argümanı kesişimlerde kullanıcak değişken
# satır indexinde ne olmasını istiyorsun der "sex"
# sütun indexinde ne olmasını istiyorsun der  "new_age"
df.pivot_table("survived", "sex", "new_age")




df.pivot_table("survived", "sex", ["new_age", "class"])
"""
df.pivot_table("survived", "sex", ["new_age", "class"])
Out[158]: 
new_age (0, 10]                   (10, 18]                   (18, 25]  \
class     First Second     Third     First Second     Third     First   
sex                                                                     
female      0.0    1.0  0.500000  1.000000    1.0  0.523810  0.941176   
male        1.0    1.0  0.363636  0.666667    0.0  0.103448  0.333333   
new_age                      (25, 40]                      (40, 90]            \
class      Second     Third     First    Second     Third     First    Second   
sex                                                                             
female   0.933333  0.500000  1.000000  0.906250  0.464286  0.961538  0.846154   
male     0.047619  0.115385  0.513514  0.071429  0.172043  0.280000  0.095238   
new_age            
class       Third  
sex                
female   0.111111  
male     0.064516  
"""


################################
# Apply ve Lambda
################################

# Apply satır ve sütunlarda otomatik olarak fonksiyon çalıştırma imkanı sağlar
# bir fonksiyon tanımlama şeklidir  farklı olarak kullan at fonksiyondur


import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("titanic")
df.head()


df["age2"] = df["age"] * 2
df["age3"] = df["age"] * 5

# yaş değişkenlerini 10 a bölmek istersek nasıl bir yol izleriz
(df["age"] / 10).head()
(df["age2"] / 10).head()
(df["age3"] / 10).head()


for i in df.columns:
    if "age" in i:
        print(i)


for i in df.columns:
    if "age" in i:
        print((df[i] / 10).head())
"""
"age" değerini içeren sütunları 10 a bölmek için df.columns içinde dolaş 
eğer i değeri "age" değerini içeriyorsa 
print(df[i]) diyerek dataframe den ilgili değişkeni seç 
print(df[i] / 10) seçilen değişkeni 10 a böl dedik
ilk 5 değeri gözlemlemek için  df[i] / 10 işleminin etrafına parantez giriyoruz
print((df[i] / 10).head())

"""
# df bulunan değişkenlere işlem yaptık yaptığımız işlemi df ' ye tekrar kaydetmedik


for i in df.columns:
    if "age" in i:
        df[i] = df[i] / 10
# şu adn yaptığımız işlemleri kaydettik

df.head()

# şimdi bu işlemleri apply ve lambda ile yapalım

df[["age", "age2", "age3"]].apply(lambda x: x/10).head()

# bunu biraz daha programatik yapmak istersek
# apply foksiyonu döngü yazmadan değişkenlerde gezme imkanı sağladı
df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head()
# adım adım kodu açıklayalım
# df.loc diyoruz dilimle (slince)
# df.loc[:,]  burada bütün satırları seç dedik
# df.loc[:, df.columns] dataframe kolonları içerisinden
# df.loc[:, df.columns.str.contains("age")] yaş değişkenlerini barındıranları seç
# apply(lambda x: x/10) bu kısımda x'ler değişkenleri temsil ediyor
# sonrasında lambda fonksiyonunu uyguluyoruz


# öyle bir fonksiyon kullanmak istiyoruz ki
# bu fonksiyon uygulandığı dataframe deki  değerleri standartlaştırsın
# yani normalleştirme standarlaştırma fonksiyonunu kullanmak istiyoruz diyelim
# tüm gözlem birimlerinden ilgili değişkenin ortalamasını çıkarak ve standart sapmasına bölecek

df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()

# şimdi lambda ifadesinden sonra gelen işlemleri açıklayalım

# (lambda x : (x- x.mean)) (yaş - yaşın ortalaması) demek istiyoruz
# age sütununda bulununan her satırdan (gözlem birimi)  age sütununun ortalamasını çıkarıyoruz

# (lambda x : (x - x.mean()) / x.std() ) diyerek standart sapmaya bölüyoruz
# şimdi lambda işi biraz karıştı lambda nın içinde def ile tanımlanmış fonksiyon da kullanabiliriz


# yukarıda lambda içine yazdığımız işlemi bir fonksiyona tanımladık ki her seferinde tek tek yazmayalım
def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

# bu kısımda anlaşılması gereken apply fonksiyonu satır ve sütunlara uygulama imkanı sunar


# sonda bulunan head() değerini sildik çünkü yapmak istediğimiz işlemi kaydediyoruz
df.loc[:, ["age", "age2", "age2"]] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)


# yukarıdaki işlemi programatik hale getirelim

df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)

# yani  sol tarafta işlem yapmak istediğimiz yerleri seçtik
# sağ tarafta istediğim yeri tekrar seçtikten sonra buraya apply ile bir işlem uyguladım


df.head()



#############################
# Birleştirme İşlemleri Join
#############################

import pandas as pd
import numpy as np

m = np.random.randint(1,  30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99


pd.concat([df1, df2])

pd.concat([df1, df2], ignore_index=True)


###########################
# Merge İle Birleştirme İşlemleri
###########################

df1 = pd.DataFrame({"employees": ["John", "dennis", "mark", "maria"],
                    "group": ["accounting", "engineering", "engineering", "hr"]})

df2 = pd.DataFrame({"employees": ["mark", "john", "dennis", "maria"],
                    "start_date": [2010, 2009, 2014, 2019]})


# her çalışanın işe başlangıç tarihine erişmek istiyoruz(elimizde çalışan group, start_date bilgisi olsun istiyoruz )

pd.merge(df1, df2)

pd.merge(df1, df2, on="employees")


# amaç: her çalışanın müdür bilgisine erişmek istiyoruz

df3 = pd.merge(df1, df2)

df4 = pd.DataFrame({"group": ["accounting",  "engineering", "hr"],
                    "manager": ["caner", "mustafa", "berkcan"]})



pd.merge(df3, df4)

