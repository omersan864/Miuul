###################################
# Değişkenlerin Yakalanması Ve işlemlerin genelleştirilmesi
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


def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))

    print("###########################################################")

cat_summary(df, "sex")

for col in cat_cols:
    cat_summary(df, col)



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




# Bonus

df = sns.load_dataset("titanic")
df.info()

for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)


cat_cols, num_cols, cat_but_car = grab_col_names(df)


def cat_summary(dataframe, col_name, plot= False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))

    print("###########################################################")

    if plot:
        sns.countplot(x = dataframe[col_name],data=dataframe)
        plt.show(block=True)


for col in cat_cols:
    cat_summary(df, col, plot=True)

for col in num_cols:
    num_summary(df, col, plot=True)






