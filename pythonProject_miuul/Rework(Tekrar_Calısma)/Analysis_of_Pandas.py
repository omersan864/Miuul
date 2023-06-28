import pandas as pd
s = pd.Series([10, 77, 12, 4, 5])
# index bilgisi iç özellik
type(s)  # series
s.index  # RangeIndex(start=0, stop=5, step=1)
s.dtype  #
s.size
s.ndim
s.values
type(s.values)  # numpy.ndarray
s.head()
s.tail()


#############################################
# Veri Okuma (reading Data )
#############################################

df = pd.read_csv("datasets/advertising.csv")

df.head()


#############################################
# Veriye Hızlı Bakış (Quick Look at Data)
#############################################

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")

df.head()
df.tail()
df.shape # boyut bilgisi
df.info()
df.columns
df.index
df.describe().T
df.isnull().values.any()   # True
df.isnull()
df.isnull().sum()  # işe yarayacak olan bu
df["sex"].value_counts()



###############################################
# Pandas'ta Seçim İşlemleri (Selection in Pandas)
###############################################

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()

df.index
df[0:13]
df.drop(0,axis=0).head()

delete_index = [1, 3, 5, 7]
df.drop(delete_index, axis=0).head()

#  1. yol ==> df = df.drop(delete_index,axis=0).head(10) diyebiliriz
#  df.drop(delete_index,axis=0, inplace=True).head(10) diyebiliriz


################################
# Değişkeni  İndex'e Çevirmek
################################

df["age"].head()


df.index = df["age"]
# yaş bilgisi bir değişken olarak eklendi

df.drop("age", axis=1).head()

df.drop("age", axis=1, inplace=True)
df.head()  # şu an yaş değişkeni olarak indexe atandı


#############################
# İndex İ değişkene çevirmek
###############################

df.index

df["age"] = df.index
df.head()

df.drop("age", axis=1, inplace=True)

df.reset_index().head()
df = df.reset_index()

df.index


##############################################
# Değişkenler üzerinde işlemler
##############################################

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns',None)
df = sns.load_dataset("titanic")
df.head()

"age" in df

df["age"].head()

type(df["age"].head())  # pandas series

# bir seçimin sonucunun dataframe olarak kalmasını istersek

df[["age"]].head()
type(df[["age"]].head())  # dataframe

# birden fazla değişken seçmek istersen

df[["age", "alive"]]

col_names = ["age", "embarked", "alive"]

df[col_names]

# değişken ekleme

df["age2"] = df["age"] * 2


df["age3"] = df["age"] / df["age2"]

# değişkeni silmek istersen

df.drop("age3", axis=1, inplace= True)

# birden fazla değişkeni silmek istersek ,

df.drop(col_names,axis=1).head()

# veri setinde belirli bir değişkeni barındıran ifadeleri silmek istersek

df.loc[:,~df.columns.str.contains("age")].head()





###############################################
# Loc & iloc
#################################################

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns',None)
df = sns.load_dataset("titanic")
df.head()

# iloc: integer label based selection
df.iloc[0:3]
df.iloc[0,0]

# loc: label based selection
df.loc[0:3]  # 3 de değere dahil


df.iloc[0:3,"age"]  # hata dönderir string ifade var

df.loc[0:3, "age"]

col_names = ["age", "embarked", "alive"]
df.loc[0:3, col_names]




##############################################
# Koşullu Seçim (Conditional Selection)
##############################################

import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("titanic")
df.head()

# yaşı 50'den büyük olanlara erişmek istersek

df[df["age"] > 50].head()

df[df["age"] > 50]["age"].count()

df.loc[df["age"] > 50, "class"].head()  # bu kısma dikkat et
df.loc[df["age"] > 50, ["age", "class"]].head()
df.loc[(df["age"] > 50) & (df["sex"] == "female"), ["age", "class"]].head()
df.loc[(df["age"] > 50) &
       (df["sex"] == "male") &
       (df["embark_town"] == "Cherbourg"),
       ["age", "class", "embark_town"]].head()

df["embark_town"].value_counts()

df_new = df.loc[(df["age"] > 50) &
                (df["sex"] == "male") &
                ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
                ["age", "class", "embark_town"]]

df_new["embark_town"].value_counts()


###############################################
# Toplulaştırma Ve Gruplaştırma (Aggregation & Grouping)
###############################################

# - Count()
# - first()
# - last()
# - mean()
# - median()
# - min()
# - max()
# - std()
# - var()
# - sum()
# - pivot table


import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("titanic")
df.head()


# kadın ve erkeklerin yaş ortalamasına erişmek istiyorum

df["age"].mean()

df.groupby("sex")["age"].mean()

# kadın ve erkeklerin yaşlarının toplamı ve ortalamsı

df.groupby("sex").agg({"age": ["mean", "sum"]})

df.groupby("sex").agg({"age": ["mean", "sum"],
                       "embark_town": "count"})

df.groupby("sex").agg({"age": ["mean", "sum"],
                       "survived": "mean" })


# sadece cinsiyete göre değil diğer bazı kategorik değişkenlere göre de kırılım yapalım

df.groupby(["sex", "embark_town"]).agg({"age": "mean",
                                        "survived": "mean"})

df.groupby(["embark_town", "sex" ]).agg({"age": "mean",
                                        "survived": "mean"})


df.groupby(["sex", "embark_town", "class"]).agg({"age": "mean",
                                                "survived": "mean"})

df.groupby(["sex", "embark_town", "class"]).agg({"age": "mean",
                                                 "survived": "mean",
                                                 "sex": "count"})






###################################################
# Pivot Table
###################################################

import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

# yaş ve gemiye binme açısından pivot tablo oluşturalım  kesişim yaş veya hayatta kalma ü

df.pivot_table("survived", "sex", "embark_town")

df.pivot_table("survived", "sex", "embarked", aggfunc="std")

df.pivot_table("survived", "sex", ["embarked", "class"])

df.pivot_table("survived", ["sex", "alive"], ["embarked", "class"])

# yaşlara göre de kırılım istersek numerik olan yaşı kategorik yaparız

df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90] )

df.head()

df.pivot_table("survived", "sex", "new_age")
df.pivot_table("survived", "sex", ["new_age", "class"])



###########################################
# Apply & lambda
###########################################
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

# apply satır veya sütunlara otomatik fonksiyon uygulanmasını sağlar
# lambda  kullan at fonksiyondur

df["age2"] = df["age"] * 2
df["age3"] = df["age"] * 5

# veri seti içindeki yaş değişkenlerinin 10 a bölünmesini istiyoruz

(df["age"] / 10).head()
(df["age2"] / 10).head()
(df["age3"] / 10).head()


for col in df.columns:
    if "age" in col:
        df[col] = df[col] / 10

df.head()

df[["age", "age2", "age3"]].apply(lambda x: x / 10 ).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: x / 10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()


def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

df.loc[:, ["age", "age2", "age3"]] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()




############################################
# Birleştirme işlemleri (Join)
#############################################

import numpy as np
import pandas as pd

m = np.random.randint(1,  30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99


pd.concat([df1, df2])

pd.concat([df1, df2], ignore_index=True)


###############################
# Merge İle Birleştirme İşlemleri
################################

df1 = pd.DataFrame({"employees": ["John", "dennis", "mark", "maria"],
                    "group": ["accounting", "engineering", "engineering", "hr"]})

df2 = pd.DataFrame({"employees": ["mark", "john", "dennis", "maria"],
                    "start_date": [2010, 2009, 2014, 2019]})



# her çalışanın işe başlangıç tarihine erişmek istiyoruz
# - hem çalışan bilgisi
# - hem grup bilgisi
# - başlangıç tarihi

pd.merge(df1, df2)
df3 = pd.merge(df1, df2, on="employees")


# her çalışanın müdür bilgisine erişmek istiyoruz

df4 = pd.DataFrame({"group": ["accounting",  "engineering", "hr"],
                    "manager": ["caner", "mustafa", "berkcan"]})


pd.merge(df3, df4)





























