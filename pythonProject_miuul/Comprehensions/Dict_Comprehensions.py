#########################
#Dict Comprehensions
#########################
from typing import Dict

dictionary: dict[str, int] = {'a': 1,
              "b": 2,
              'c': 3,
              'd': 4}

dictionary.keys()
dictionary.values()
dictionary.items()


#her valuenin karesini almak istiyoruz

kare = [values * values for  values in dictionary]

# her value değerinin karesini aldık ve harfleri büyüttük
{k.upper(): v ** 2 for (k, v) in dictionary.items()}


##########################
#Uygulama: Mülakat Sorusu
##########################

#Amaç çift sayıların karesi alınarak bir sözlüğe eklenmek istenmektedir
#keyler orjinal değerler olacak valuenin ise değiştirilmiş değerler olacak

numbers= range(10)

new_dict = {}

for n in numbers :
    if n % 2 == 0 :
        new_dict[n] = n ** 2

{n: n ** 2 for n in numbers if n % 2 == 0 }


#################################
#List & Dict comprehension uygulamalar
#################################

##############################
#bir veri setindeki  değişken isimlerini değiştirmek
#############################

#before
#['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous','ins_premium', 'ins_losses', 'abbrev']

#after
#

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

for col in df.columns:
    print(col.upper())

A = []

for col in df.columns:
    A.append(col.upper())

df.columns = A

df = sns.load_dataset("car_crashes")

df.columns = [col.upper() for col in df.columns ]

######################################
#İsminde "INS" olan değişkenlerin başına FLAG  diğerlerine NO_FLAG eklemek istiyoruz
#####################################

#Before
#['TOTAL',
# 'SPEEDING',
#'ALCOHOL',
# 'NOT_DISTRACTED',
#'NO_PREVIOUS',
# 'INS_PREMIUM',
# 'INS_LOSSES',
# 'ABBREV']

#after
#['NO_FLAG_TOTAL',
# 'NO_FLAG_SPEEDING',
# 'NO_FLAG_ALCOHOL',
# 'NO_FLAG_NOT_DISTRACTED',
# 'NO_FLAG_NO_PREVIOUS',
# 'NO_FLAG_INS_PREMIUM',
# 'NO_FLAG_INS_LOSSES',
# 'NO_FLAG_ABBREV']


[col for col in df.columns if "INS" in col]

["FLAG_" + col for col in df.columns if "INS" in col]

["FLAG_"+ col if col in "INS" else "NO_FLAG_"+ col  for col in df.columns]

df.columns = ["FLAG_"+ col if col in "INS" else "NO_FLAG_"+ col  for col in df.columns]
##########################
#amaç key'i string, value' su aşağıdaki gibi bir liste olan sözlük oluşturmak
########################

import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns

num_cols = [col for col in df.columns if df[col].dtype != "O"]

soz = {}

agg_list = ["mean", "min", "max", "var"]

for col in num_cols:
    soz[col] = agg_list


#kısa yol
new_dict = {col : agg_list for col in num_cols}

df[num_cols].head()

df[num_cols].agg(new_dict)






















