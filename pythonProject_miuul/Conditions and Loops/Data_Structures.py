# VERİ YAPILARINA GİRİŞ

# VERİ YAPILARINA GİRİŞ VE HIZLI ÖZET
# SAYILAR ; İNT , FLOAT , COMPLEX
# Karakter dizileri : strings str
# Boolen ( True - False) : bool
# liste (list)
# sözlük (dictionary)
# demet ( tuple)
# set

############################################
# Veri yapılarına giril ve hızlı özet
###########################################

#sayılar (integer)
x = 46
type(x)

#sayılar (float)

x= 20.3
type (x)

# string

x= "hello ai era"
type (x)

#Boolean

True
False
type(True)

#Liste

x= ["btc", "eth", "xrp"]
type(x)

#sözlük  (bir key değeri alır bir de value alır  )
x = {"name":"ömer", "age":23}
type(x)

#tuple

x=("python", "ML","ds")
type(x)

# set

x={"python","ml" , "ds"}
type(x)

# karakter

print ("ömer")

name ="ömer"

long_str = """"
hepsini bir karakter dizisi olarak görecektir 
1
TRUE

"""

name[0] # ilk harfe erişmek için kullanılır

name[0:2] # ikiye kadar git ve 2. indeks hariç "öm"

#\n  bir satır aşağı inmek için kullanılır

long_str = """"
hepsini bir karakter dizisi olarak görecektir 
1
TRUE

"""


"karakter" in long_str

################################3
#String (Karakter Dizisi) Metodları
###################################

dir(str)

# len

name = "john"

type(name)
type(len)

len(name)

len("omersan")

# eğer bir fonksiyon class yapısı içine tanımlanmışsa buna method denir

# upper() & lower () : küçük büyük dönüşümleri

"omersan".upper() # hepsini büyük yaptı

'OMERSAN'.lower()

#replace   karakter değiştirmek için kullanılır

hi = "hello ai era"
hi.replace("l","p")

#split: böler

"Hello ai era".split()

#capitalize ilk harfi büyütür

"hello ai era".capitalize()

############################
#Liste
############################

#değiştirilebilir
#sıralıdır . index işlemleri yapılabilir
#kapsayıcıdır

notes = [1,2,3,4]
type(notes)

name=["a", "b", "c", "d"]

not_nam=[1, 2, 3, "a", "b", True, [1, 2, 3]]

not_nam[0]
not_nam[5]
not_nam[6]
not_nam[6][1]

notes[0]=99
notes   # ilk elemanı değiştirdik

not_nam[0:4] # 4 dahil değil

len(notes)
len(not_nam)

notes.append(110)
notes

# pop indeks değerine göre silme işlemini yapar
notes.pop(0)
notes

# insert  indexe ekler

notes.insert(2,99)
notes


##########################
#Sözlük  (key & value)
##########################

#değiştirilebilir
# sırasız (3.7 sonra sıralı )
# kapsayıcı

# key-value

dictionary = {"REG" : "regression",
              "LOG": "Logistic Regression",
              "CART":"Classification and Reg"}

dictionary["REG"]


dictionary = {"REG": ["RMSE", 10],
              "LOG": ["MSE", 20],
              "CART": ["SSE", 30]}

dictionary = {"REG":  10,
              "LOG":  20,
              "CART":  30}


# Key sorgulama

"ysa" in  dictionary

dictionary.get("REG")

dictionary["REG"] = ["YSA", 10]
dictionary

# update ekleyebilirisin

###################
#demet ()Tuple
####################

#değiştirilemez
#sıralıdır index değerine göre
# kapsayıcı birden fazla veri türü tutabilir


t = {"johne", "mark", 1, 2}

type(t)

t[0]
t[0:3]

t = list(t)
t[0]=99

t= tuple(t)


################
#set
##############

#değiştirilebilir
#sırasız + eşsizdir
#kapsayıcıdır

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])


set1.difference(set2)

def cal (wage,hour):
    print(wage*hour)

cal (10,40)-200

students = ["Denise", "Arsen", "Tony", "Audrey"]

low = lambda x : x[0].lower()

print(list(map(low, students)))









