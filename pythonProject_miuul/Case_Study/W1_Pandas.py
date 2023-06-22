#görev 1  titanic veri setini tanımlayınız
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("titanic")
df.head()

# görev 2 titanic veri setinde kadın ve erkek yolcu sayısını bulunuz
df["sex"].value_counts()
"""
df[""]  parantez ile sütunlar arasından istediğim değişkeni seçebilir 
.value_counts() seçilen değişken içerisinde yer alan kategori
 veya değereri saydırabilirim 
"""

# görev3 her bir sütuna ait uniq değerlerin  sayısını bulunuz


