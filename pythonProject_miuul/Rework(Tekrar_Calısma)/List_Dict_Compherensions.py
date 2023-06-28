###############################
# list - dict comprehensions uygulamalar
###############################


#############################
# bir veri setindeki değişken isimlerini değiştirmek
#############################

# before : ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous',
#        'ins_premium', 'ins_losses', 'abbrev']

# after : ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS',
#        'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']


import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

for col in df.columns:
    print(col.upper())

A = []

for col in df.columns:
    A.append(col.upper())

df.columns = A

# şimdi farklı bir yol ile yapalım
df = sns.load_dataset("car_crashes")
df.columns = [col.upper() for col in df.columns]

#########################################
# İsminde "INS" olan değişkenlerin başına Flag diğeroerine NO_FLAG eklemek istiyoruz
##########################################


import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns


[col for col in df.columns if "INS" in col ]

["FLAG_"+ col for col in df.columns if "INS" in col ]

["FLAG_"+ col if "INS" in col else col for col in df.columns ]

["FLAG_"+ col if "INS" in col else "NO_FLAG_"+ col for col in df.columns ]


df.columns = ["FLAG_"+ col if "INS" in col else "NO_FLAG_"+ col for col in df.columns ]


################################
# amaç key'i string value'si aşağıdaki gibi bir liste oluşturmak
# bu işlemi sadece sayısal değişkenler için yapmak istiyoruz
################################

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

# önce veri setinden sayısal olan değerleri seçeceğiz
num_cols = [col for col in df.columns if df[col].dtype != "O"]
dıct = {}
agg_list = ["mean", "min", "max", "sum"]

for col in num_cols:
    dıct[col] = agg_list


dıct = {col: agg_list for col in num_cols}

df[num_cols].agg(new_dict)





