############################################
# Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
############################################

import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

############################################
# Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
############################################

df["sex"].value_counts()

############################################
# Her bir sutuna ait unique değerlerin sayısını bulunuz.
############################################

df.nunique()

############################################
# Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz
############################################

df["pclass"].nunique()  # cevap bu
df["pclass"].unique()

############################################
# Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz
############################################

new = ["pclass", "parch"]
df[new].nunique()

############################################
# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.
############################################


type(df["embarked"])  # pandas series == saç yolduran serisinden

df["embarked"] = df["embarked"].astype("category")

type(df["embarked"])

df.info()
# df.astype({'embarked': 'category'}).dtypes

############################################
# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
############################################
# bu kısımda koşullu seçim işlevi yer alıyor
df[df["embarked"] == "C"].head()

############################################
# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz
############################################

df[df["embarked"] != "S"].head()

############################################
# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz
############################################

df[(df["age"] < 30) & (df["sex"] == "female")].head()

############################################
# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
############################################

df[(df["fare"] > 500) | (df["age"] > 70)].head()

############################################
# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz
############################################

df.isnull().sum()

############################################
# Görev 12: who değişkenini dataframe’den çıkarınız.
############################################

df.head()
df.drop("who", axis=1)

############################################
# Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz
############################################

df.isnull().sum()
df["deck"].isnull().sum()
df["deck"].mode()
model_values = df["deck"].mode()[0]  # mode kullanımı sonuc olarak bir değer değil seri dönderiyor ilk değer için [0]
df["deck"].fillna(model_values, inplace=True)
df["deck"].isnull().sum()
df.isnull().sum()

############################################
# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz
############################################

df["age"].isnull().sum()  # 177
model_values = df["age"].median()
df["age"].fillna(model_values, inplace=True)
df["age"].isnull().sum()
df.isnull().sum()

############################################
# Görev 15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz
############################################

df.groupby(["pclass", "sex"]).agg({"survived": ["sum", "count", "mean"]})

df.pivot_table("survived", ["pclass", "sex"], aggfunc=["sum", "count", "mean"])


############################################
# Görev 16: 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın.
# Yazdığınız fonksiyonu kullanarak titanik veri
# setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
############################################

def give(age):
    if age < 30:
        return 1
    else:
        return 0


df["age_flag"] = df["age"].apply(give).head()
df.head()
df["age_omer"] = df["age"].apply(give)
df.head()

############################################
# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız
############################################

import pandas as pd
import seaborn as sns

df = sns.load_dataset("Tips")
df.head()


############################################
# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch)
# göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz
############################################

df.groupby("time").agg({"total_bill": ["sum", "min", "max", "mean"]})


############################################
# Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz
############################################

df.groupby(["day", "time"]).agg({"total_bill": ["sum", "min", "max", "mean"]})

df.pivot_table("total_bill", "day", "time", aggfunc=["sum", "min", "max", "mean"])

# bu ikisi arasındaki fark groupby listede oluşan NAN değerleri göstermiyor
# ama pivot tablo  NAN değerleri de gösteriyor


############################################
# Görev 20: Lunch zamanına ve kadın müşterilere ait
# total_bill ve tip değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz
############################################

df[(df["time"] == "Dinner") & (df["sex"] == "female")].groupby("day").agg({"total_bill": ["sum", "min", "max", "mean"],
                                                                           "tip": ["sum", "min", "max", "mean"]})
"""
Group by işlemi, ilk olarak gruplama kriterini belirlemeniz gerektiği için
"category" gibi bir sütun adını belirtmeniz gerekmektedir. Sonrasında,
gruplama sonucunda üzerinde işlem yapmak istediğiniz sütun veya sütunları belirtmelisiniz.
gruplama kriterinden sonra köşeli parantez içinde belirttiğiniz sütunlar üzerinde istediğiniz işlemi gerçekleştirirsiniz
"""



############################################
# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)
############################################

df.loc[(df["size"] < 3) & (df["total_bill"] > 10)].mean()
df.loc[(df["size"] < 3) & (df["total_bill"] > 10), "total_bill"].mean()




############################################
# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz.
# Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
############################################

df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
df.head()


############################################
# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız
# ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
############################################

new_alignment = df.sort_values("total_bill_tip_sum", ascending=False).head(30)

df1 = pd.DataFrame(new_alignment)
df1.head()
df1.info()



















