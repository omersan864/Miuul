###################################
# Sayısal değişken analizi (analysis of numerical variables)
#######################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)

df = sns.load_dataset("titanic")
df.head()

df[["age", "fare"]].describe().T



#programatik olarak numeric değişkenleri veri setinden nasıl çekerim  ?

cat_cols = [col for col in df.columns if str(df[col].dtype) in ["category", "bool", "object"]]
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtype) in ["category", "object"]]
cat_cols = cat_cols + num_but_cat
cat_cols = [col for col in cat_cols if col not in cat_but_car]


df[["age", "fare"]].describe().T

num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]
num_cols = [col for col in num_cols if df[col].dtypes not in cat_cols]


def num_summary(dataframe, numerical_col):
    print(dataframe[numerical_col].describe().T)

"""
yukarıda num_summary fonksiyonunda 
print yazdır işlevini görüyor 
dataframe[numerical_cols] fonksiyondan gelen sütun ismi 
describe diyerek istatistik alabiliriz
"""

num_summary(df, "age")

for col in num_cols:
    num_summary(df, col)

#aşağıdaki fonksiyona bir özellik ekleyelim
def num_summary(dataframe, numerical_col, plot=False):
    print(dataframe[numerical_col].describe().T)

    if plot :
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block= True)

num_summary(df, "age", plot = True)

for col in num_cols:
    num_summary(df, col, plot=True)