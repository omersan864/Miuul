##############################
# Koreleasyon analizi (analysis of correlation)
#################################

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 100)
df = pd.read_csv("C:/Users/omer/PycharmProjects/pythonProject/datasets/breast_cancer.csv")
df = df.iloc[:, 1:-1]
df.head()

# amacımız ısı haritası yolu ile koreleasyonlarına bakmak ve daha sonra
# yüksek koreleasyonlubir değişken setindeki  yüksek koreleasyonlardan bazılarını
# dışarıda bırakabilmeyi görmektir

num_cols = [col for col in df.columns if df[col].dtype in [int, float]]

corr = df[num_cols].corr()

sns.set(rc={'figure.figsize': (12, 12)})
sns.heatmap(corr, cmap="RdBu")
plt.show(block=True)

######################################
# Yüksek KOreleasyonlu değişkenlerin silinmesi
#####################################
# koreleasyon değerini yüksek olması değişkenlerden birinin işe yaramadığını ifade eder

# bütün koreleasyonları mutlak değerden geçiriyoruz
cor_matrix = df.corr().abs()

# aşağıda elde etmek istediğimiz çıktı bulunuyor

#           0         1         2         3
# 0  1.000000  0.117570  0.871754  0.817941
# 1  0.117570  1.000000  0.428440  0.366126
# 2  0.871754  0.428440  1.000000  0.962865
# 3  0.817941  0.366126  0.962865  1.000000


#     0        1         2         3
# 0 NaN  0.11757  0.871754  0.817941
# 1 NaN      NaN  0.428440  0.366126
# 2 NaN      NaN       NaN  0.962865
# 3 NaN      NaN       NaN       NaN

upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool))
"""
(np.ones(cor_matrix.shape),k=1)

birlerden oluşan ve oluşturduğumuz matrisin boyutunda bir numpay array i oluşturuyoruz
bu numpy array ini bool a çeviriyoruz  ==>> astype(np.bool)
yukarda gösterilen yapıya dönüştürmek için numpy fonksiyonunu kullanıyoruz  ==>> np.triu


bu matrisi oluşturmak için önce  boş bir numpy array i oluşturduk  bunu true false 
ile doldurduk ve  daha sonra köşegen elemanlarından kurtulduktan sonra 
kalanlar true olacağından dolayı 
bunu bu matris de ver  ====>>>>  cor_matrix.where  koşulu sağlayanları getir 

"""

drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > 0.90)]

cor_matrix[drop_list]

df.drop(drop_list, axis=1)


def high_correleated_cols(dataframe, plot=False, corr_th=0.90):
    corr = dataframe.corr()
    cor_matrix = corr.abs()
    upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool))
    drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > corr_th)]
    if plot:
        import seaborn as sns
        import matplotlib.pyplot as plt
        sns.set(rc={'figure.figsize': (15, 15)})
        sns.heatmap(corr, cmap='RdBu')
        plt.show(block=True)
    return drop_list


high_correleated_cols(df)
drop_list = high_correleated_cols(df, plot=True)
df.drop(drop_list, axis=1)
high_correleated_cols(df.drop(drop_list, axis=1), plot=True)

df = pd.read_csv("C:/Users/omer/PycharmProjects/pythonProject/datasets/ieee-fraud-detection/train_transaction.csv")
len(df.columns)
df.head()

drop_list = high_correleated_cols(df, plot=True)

len(df.drop(drop_list,axis=1).columns)