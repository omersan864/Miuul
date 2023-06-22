#################
# list_comprehension
################

# görev 1

"""
list comprehension yapısını kullanarak car_crashes verisindeki numeric
değişkenlerin  isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz
"""

import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns

df.columns = ["NUM" + col.upper() if df[col].dtypes in ["int", "float"] else col.upper() for col in df.columns]

df.info()


# görev 2
"""list comprehensions yapısı kullanarak car_crashes verisinde isminde "no"barındırmayan
değişkenlerin isimlerinin sonuna FLAG yazınız"""


import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns

#df.columns = [col.upper() + "_FLAG" if col not in "no" else col.upper() for col in df.columns]

df.columns = [col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]


#görev 3
"""
List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan
değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
"""

import seaborn as sns
import pandas as pd

df = sns.load_dataset("car_crashes")
df.columns

og_list = ["abbrev", "no_previous"]

new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]

print(new_df.head())
"""
Bu kodda, öncelikle Seaborn kütüphanesi aracılığıyla "car_crashes" veri setini df DataFrame'ine yükleriz. Ardından,
 og_list listesindeki değişkenlerin dışındaki değişkenleri seçmek için list comprehension yapısını kullanırız.
  List comprehension ifadesinde, df.columns üzerinde döngü oluşturarak her bir değişkeni kontrol ederiz. 
  Eğer değişken og_list listesinde bulunmuyorsa, new_cols listesine ekleriz.

Sonrasında, new_df DataFrame'ini oluşturmak için df[new_cols] ifadesini kullanırız.
 Bu şekilde, sadece istenilen değişkenlerden oluşan yeni bir DataFrame oluştururuz.

Son olarak, new_df DataFrame'ini ekrana yazdırarak beklenen çıktıyı elde ederiz.
"""

