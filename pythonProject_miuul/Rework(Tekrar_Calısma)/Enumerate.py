############################
# Enumerate : otomatik Counter / Indexer ile for loop
#############################

"""
bir iteratif nesne içinde gezip elemanlarına bir şey yaparken  aynı zamanda
o elemanların indeks bilgilerini de takip etmek istediğimizde  ve genelde derinlemesine
bir projenin içinde  karşılaşıp nasıl çözüleceğine dair uzun zamanlar harcanan bir problemdir


örneğin iteratif / liste içinde gezerken  bu elemanlara belirli bir işlem
uygularken aynı zamanda işlem uygulanan elemanların  indeks bilgisini de tutup
gerekirse bu index bilgisine göre de işlem  yapmak istediğimizde  hayat kurtaran bir yapıdır

"""

# indexi tek olanlara bir işlem çift olanlara başka bir işlem yapmak istediğimiz düşünelim
students = ["John", "Mark", "Venessa", "Mariam"]


for i in students:
    print(students)


for index, student in enumerate(students):
    print(index, student)

A = []
B = []

for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)

################################
# uygulama  -  mülakat sorusu
##############################

# divide_students fonksiyonunu yazınız
# çift indexte yer alan öğrencileri bir listeye
# tek indexte yer alan öğrencileri bir listeye alınız
# fakat bu iki liste tek bir liste olarak return olsun

students = ["John", "Mark", "Venessa", "Mariam"]


def divide_student(students):
    group = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            group[0].append(student)
        else:
            group[1].append(student)
    print(group)
    return group

st = divide_student(students)

st[0][0]


##############################
# alternating fonksiyonunun enumerate ile yazılması
##############################
"""
öyle bir fonksiyon yazalım ki kendisine girilen string ifadelerin çift 
indexte yer alanlarını büyütsün tek indexte yer alanlar küçülsün
"""

def alternating_with_enumerate (string):
    new_string = ""
    for i, letter in enumerate(string) :
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()

    return new_string

alternating_with_enumerate("benim adım ömer şan ")


city_name = ["london", "paris", "berlin"]

def plate (cities):
    for index , city in enumerate (city_name, 1):
        print (f"{index} : {city}")

plate(city_name)


wages = [1000, 2000, 3000, 4000, 5000]

new_wages = lambda x: x*0.20 + x

list (map(new_wages,wages))


dictn = {"ömer":10,
         "ali":12,
         "ahmet":15,
         "demir":17,
         }
new_dictn = {k:v*2+3 for (k,v) in dictn.items()}
new_dictn

def alternating (string):
    new_string = ""
    for string_index,letter in enumerate (string):
        if string_index % 2 == 0 :
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)

alternating("naber lan oluyor mu")

import  numpy as np
import pandas as pd
a = pd.Series([2,4,6,8])
a**2




