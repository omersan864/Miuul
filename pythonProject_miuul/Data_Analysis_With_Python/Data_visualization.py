##########################################
# Data Visualization  : Matplotlib & Seaborn
##########################################

##########################################
# MATPLOTLIB
##########################################

""""
1. kategorik verileri  : sütun grafiği ile gösterebiliriz :   countplot & bar
2. sayısal değişkenleri : hist , boxplot

"""
import numpy as np
#########################################
# Kategorik değişken görselleştirme
##########################################

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns',None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df["sex"].value_counts().plot(kind = 'bar') # bu fonksiyon her zaman kullanacağımız önemli fonksiyonlardan biridir
plt.show(block=True)


#######################################
# Sayısal değer görselleştirme
########################################

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns',None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

plt.hist(df["age"])
plt.show(block = True)

plt.boxplot(df["fare"])
plt.show(block = True)


###########################################
# Matplotlib özellikleri
############################################

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns',None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

###############################
# plot
################################
import  numpy as np
x = np.array([1, 8])
y = np.array([0, 150])

plt.plot(x, y)
plt.show(block = True)

plt.plot(x, y,'o')
plt.show(block = True)

x= np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])

plt.plot(x, y)
plt.show(block = True)

############################
# marker
###############################

y = np.array([13, 28, 11, 100])
plt.plot(y, marker='o')
plt.show(block = True)

#################################
# line
#################################

y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle = "dashed", color = "red")
plt.show(block = True)

y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle = "dotted")
plt.show(block = True)

y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle = "dashdot")
plt.show(block = True)


#################################
# Multiple lines
#################################

y = np.array([23, 18, 31, 10])
x = np.array([13, 28, 11, 100])

plt.plot(x)
plt.plot(y)
plt.show(block = True)

#################################
# labels
#################################
import  numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

x = np.array([80, 85, 90,95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)
plt.show(block = True)

plt.title("bu ana başlık")

plt.xlabel("x ekseni isimlendirmesi")