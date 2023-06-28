########################################
# DATA STRUCTURE
#######################################
# bu kısımda göreceklerimiz

# veri yapılarına giriş ve hızlı bir özet
# sayılar (Numbers) : int , float, complex
# karakter Dizileri (Strings): str
# Boolean : True False
# Liste  (list)
# Sözlük (Dictionary)
# Demet (Tuple)
# Set

# veri programlamanın en küçük veri yapılarından biridir


########################################
# veri yapılarına giriş ve hızlı bir özet
#######################################

# her bir veri yapısının oluşturulmasını ve tip bilgisinin sorulmasını ele alacağız

# sayılar : İnt

x = 46
type(x)

# sayılar : float

x = 10.3
type(x)

# sayılar : complex

x = 2j+1
type(x)

# String
x = "Hello ai era"
type(x)


#Boolean
True
False

type(True)

5 == 4 # False (Boolean)

# Liste

x = ["btc", "eth", "xrp"] # içeride string değer var
type(x) # list

# Dictioary (Sözlük)

x = {"name" : "peter",
     "Age" : 36}
# sözlük oluşturulurken süslü parantez kullanılır
# elemanlar virgül ile ayrılır
#  sözlükler key & value değerlerinden oluşur
# iki noktadan önce key olur sonrasında value olur

type(x) # dict

# Tuple

x = ("python", "ml", "ds")
type(x) # listenin aksi hali gibi

# set

x = {"python", "ml", "ds"}
type(x) # set süslü parantez var ama iki nokta yok key&value yok


# Liste, tuple, set ve dictionary veri yapıları aynı zamanda python Collections (Array) olarak geçmektedir


##########################
# sayılar (Numbers) : int float complex
########################

a = 5
b = 10.5

a * 3
a / 7
a * b / 10
a ** 2

# elimizdeki veri yapısını çevirmek istersek

####################################
#Tipleri Değiştirmek
####################################

int(b) # b float değerini ondalık değerini silerek int değerine dönüştürdük
float (a) # a değerinin sonuna ondalık ekleyecek dönüşüm yaptı

int (a * b / 10)  #parantez içindeki işlemin sonucu float ama sonucu int olarak alabiliriz



######################################
# Karakter dizileri (Strings)
#######################################


print("john")
print('john')

"john"

name = "john"

##########################
# çok satırlı karakter dizileri
##########################

""" veri yapılarına giriş ve hızlı bir özet
 sayılar (Numbers) : int , float, complex
 karakter Dizileri (Strings): str
 Boolean : True False
Liste  (list)
Sözlük (Dictionary)
Demet (Tuple)
 """
long_str = """veri yapılarına giriş ve hızlı bir özet
 sayılar (Numbers) : int , float, complex
 karakter Dizileri (Strings): str
 Boolean : True False
Liste  (list)
Sözlük (Dictionary)
Demet (Tuple)"""


################################
# karakter dizilerinin elemenlarına erişmek
###############################

name [0]
name[3]

###########################
#karakter dizilerinde slice işlemi
###########################

name
name[0:2] # ikiye kadar git iki hariç

long_str [0:10]

#############################
#sting içinde karakter sorgulama
############################

"veri" in long_str  # True

"BOOL" in long_str


###############################
# String (karakter dizisi) metodları
###############################

# method nedir : çeşitli görevleri yerine getiren fonksiyon benzeri yapılardır
# diğer ifadesi ile class içerisinde tanımlanan fonksiyonlardır

# öncelikle bir veri yapısının metodlarına nasıl erişebileceğimizi değerlendirelim

# bu veri yapılarına özel bazı methodlar var yani fonksiyonlar var
# örneğin karakter dizileri için karakterleri küçültmek ve büyültmeye yarayan fonksiyonlar var
# örneğin listelerde listeye bir eleman eklemek için tanımlanan bir fonksiyon var
# dir (int) diyerek int ile kullanabileceğimiz fonksiyonlara erişebiliriz

#########################
# len fonksiyonu
##########################

# stringlerde boyut bilgisine erişmek için kullanır
# içerisine girilen ifadenin noyut bilgisini verir

name = "john"
type(name)
type(len)

len(name)

type(len(name))

len("ömerşan")

# kullanmış olduğumuz ifadenin metod mu yoksa fonksiyon mu olduğunu nasıl ayırırız
# EĞER BİR FONKSİYON CLASS YAPISI İÇERİSİNDE TANIMLANDI İSE BUNA METHOD DENİR
# EĞER BİR CLASS YAPISI İÇERİSİNDE DEĞİL İSE FONKSİYONDUR
# len() bir fonksiyondur bir class içerisine tanımlanmamış




##########################
# upper() & lower() : küçük büyük dönüşümleri
#############################

# karakter dizilerini büyütmek ve küçültmek için kullanılır
# upper yapısı bir fonksiyondur class yapısı içerisine tanımlanmıştır
# bu yüzden type bilgisini istediğimizde erişemeyiz

"ömer".upper() # çıktı olarak bütün harfleri büyük verdi

"ÖMER".lower() # çıktı olarak bütün harfleri küçük verdi


################################
# replace : karakter değiştirme
#################################

hi = "Hello AI era"
# amaç hello yazısındaki ll harfleri yerine p yazmak olsun

hi.replace("l","p") # ilk kısma değiştirmek istediğimiz argümanı
# ikinci kısma ise ne ile değiştirmek istersek o argümanı gireceğiz


#################################
# spit : bölme işlemi için kullanılır
#################################

hi = "Hello AI era"

"Hello AI era".split() # ön tanımlı değer boşluktur eğer argüman verirsen ona göre böler
# Out[13]: ['Hello', 'AI', 'era']

###########################
# strip : kırpma metodudur
##########################

" ofofo ".strip()# ön tanımlı olarak kırpma işlemini boşluğa göre yapar
# boşlukarı kırptı ve "ofofo" ifadesi kaldı

"ofofo".strip("o")
#"ofofo".strip("o")
#Out[15]: 'fof' kırpma işlemini o lara göre yaptı


#####################################
# capitalize : ilk harfi büyütür
######################################

"fco".capitalize() # çokto olarak "Fco" çıktısını verir


















