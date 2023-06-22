###################################
# Hedef değişken analizi  (analysis of target variable)
#######################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)

df = sns.load_dataset("titanic")
df.head()
df.info()

for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)


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

#cat_th bir değişken sayılsal olsa dahi  benzersiz değer sayısı 10 dan küçük ise kategorik değişken diyeceğiz
def grab_col_names(dataframe, cat_th = 10 , car_th = 20):
    """
    veri setindeki kategorik, numeric ve kategorik fakat kardinal değişkenlerin isimlerini verir

    Parameters
    ----------
    dataframe: dataframe
        değişken isismleri alınmak istenen dataframe dir
    cat_th : int, float
        numeric fakat kategorik olan değişkenler için sınıf eşik değeri
    car_th : int , float
        kategorik fakat kardinal değişkenlerin isimlerini verir

    Returns
    -------
    cat_cols : list
        kategorik değişken listesi
    num_cols: list
        numeric değişken listesi
    cat_but_car : list
        kategorik görünümlü kardinal değiken listesi

    Notes
    -------
    cat_cols + num_cols + cat_but_car = toplam değişken sayısı
    num_but_cat in  cat_cols'un içerisinde
    return alan 3 liste toplam değişken sayısına eşittir : cat_cols + num_but_cat + cat_but_car


    """
    cat_cols = [col for col in df.columns if str(df[col].dtype) in ["category", "bool", "object"]]

    num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]

    cat_but_car = [col for col in df.columns if
                   df[col].nunique() > 20 and str(df[col].dtype) in ["category", "object"]]

    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]

    num_cols = [col for col in num_cols if df[col].dtypes not in cat_cols]

    print(f"Observation (gözlemler) :{dataframe.shape[0]}")
    print(f"Variable (değer) :{dataframe.shape[1]}")
    print(f"cat_cols :{len(cat_cols)}")
    print(f"num_cols :{len(num_cols)}")
    print(f"cat_but_car :{len(cat_but_car)}")
    print(f"num_but_cat :{len(num_but_cat)}")

    return cat_cols, num_cols, cat_but_car


cat_cols, num_cols, cat_but_car = grab_col_names(df)

#hedef değişkenimiz survived değişkeni (yolcuların hayatta kalıp kalmadığı)
#sonuca survived üzerinden erişebiliriz fakat hayatta kalma durumunu etkileyen şey nedir
cat_summary(df, "survived")


###################################
# Hedef değişkenin kategorik değişkenler ile analizi
#######################################

#iki tane kategorik değişkeni çaprazladık ve ilişkisine baktık kadınların hayatta kalma oranı yüksek diyoruz
df.groupby("sex")["survived"].value_counts()
df.groupby("sex")["survived"].mean()
df.groupby("sex")["survived"].size()

def target_summary_with_cat(dataframe, target, categorical_col):
    """
    veri setinde hedef değişken ile kategorik değişken ilişkisini bulmak için
    Parameters
    ----------
    dataframe : dataframe
        değişken isismleri alınmak istenen dataframe dir
    target : int, float, string, bool
        Analiz için hedef bağımsız değişken
    categorical_col : int, float, string, bool
        Analiz için bağımlı değişken


    Returns
    -------

    """
    print(pd.DataFrame({"Target_Mean": dataframe.groupby(categorical_col)[target].mean()}),end="\n\n\n")

target_summary_with_cat(df, "survived", "pclass")

for col in cat_cols:
    target_summary_with_cat(df, "survived", col)


###################################
# Hedef değişkenin sayısal değişkenler ile analizi
#######################################

# hayatta kalanların yaş ortalamsı 28
# hayatta kalamayanların yaş ortalaması 30
df.groupby("survived")["age"].mean()
df.groupby("survived")["age"].size()

df.groupby("survived").agg({"age": "mean"})

def target_summary_with_num (dataframe, target,numerical_cols):
    print(dataframe.groupby(target).agg({numerical_cols: "mean"}),end="\n\n\n")

target_summary_with_num(df, "survived", "pclass")

for col in num_cols:
    target_summary_with_num(df, "survived", col)
