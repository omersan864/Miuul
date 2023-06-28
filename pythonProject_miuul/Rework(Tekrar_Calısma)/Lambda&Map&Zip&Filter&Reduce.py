###########################
# ZİP
#############################
students = ["john", "Mark", "Venessa", "Mariam"]

departments = ["mathematics", "statistic", "physics", "astronomy"]

ages = [23, 30, 26, 22]

# bu 3 listenin elemanlarını eşlemek istersek birlikte kullanmak istiyoruz

# zip birbirinden farklı olan listeleri birlikte değerlendirme imkanı sağlar

# genel çıktının list olmasını istediğim için list fonksiyonunu kullan

list(zip(students, departments, ages))

############################
# lambda & map & filter & reduce
#############################

def summer (a,b):
    return a+b
summer(1, 3) * 9

# lambda kullan at fonksiyondur

new_sum = lambda a, b: a + b

new_sum (4, 5)

# map
"""mao fonksiyonu seni döngü yazmaktan kurtarmak istiyorum der 
bana içerisinde gezebileceğim iteratif bir nesne ver 
 ve bu fonksiyona uygulamak istediğin fonksiyonu ver 
 ben sana bu işlemi otomatik olarak yaparım der """


salaries =[1000, 2000, 3000, 4000, 5000]
# maaşların her birine zam yapmak istersek

#bu fonksiyon kendisine girilen değeri %20 zam uyguluyor
def new_salary  (x):
    return x * 20 / 100 + x

new_salary(1000)

for salary in salaries:
    print(new_salary(salary))

# öncelikle map a bu iki fonksiyonu verelim
# çıktının list() olmasını istediğim için list fonksiyonunu getir

list(map(new_salary,salaries))

# şimdi lamda ile map ilişkisine gelelim

list(map(lambda x : x * 20 / 100 + x, salaries))


list(map(lambda x : x**2, salaries))




# filter

# filtreleme işlemleri için kullanılır
# bu liste içinde belirli koşulu sağlayanları seçmek istediğimizi

list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list(filter(lambda x : x % 2 == 0, list_store))

# reduce  indirgemek anlamına gelmektedir

from functools import  reduce
list_store = [1, 2, 3, 4]
# ilgili elemanlara tek tek belirli bir işlemi uygulamak
# uygulamak istediğimiz işlemi lambda ile tanımlayalım

reduce(lambda a, b : a + b, list_store)
# lambda a ve b den oluşmaktadır  ve bunun görevi a ve b yi toplamaktır
# bunun list_store listesi üzerine göderirsek her bir elemanı toplar

import numpy as np
serie = np.arange(1,10)

x = [3, 4, 5]

serie[x]

import seaborn as sns
df = sns.load_dataset("titanic")

df.columns
df[["sex","survived"]].groupby("sex")