#######################
# FONKSİYONLAR, KOŞULLAR, DÖNGÜLER, COMPHERENSIONS
#################
# FONKSİYONLAR (Functions)
# koşullar (Conditions)
# Döngüler (Loops)
# Comprehesions


#############################
# FONKSİYONLAR (Functions)
#############################
# belirli görevleri yerine getirmek için yazılan kod dizeleri

#############################
# Fonksiyon Okuryazarlığı
############################

print("a")

print("a", "b", sep="--")  # iki argümanı "--" ile birleştirerek yaz


#####################
# Fonksiyon Tanımlama
#######################

# girilen sayıları iki ile çarpacak bir fonksiyon tanımlayalım

def calculate(x):
    print(x * 2)


calculate(5)


# iki argüman/parametreli bir fonksiyon tanımlayalım

def summer(arg1, arg2):
    print(arg1 + arg2)


summer(7, 8)
summer(arg1=8, arg2=7)


#########################
# DocString
########################

def summer(arg1, arg2):
    print(arg1 + arg2)


def summer1(arg1, arg2):
    """
sum of two numbers
    Args:
        arg1: int , float
        arg2:int , float

    Returns:
        int, float

    """
    # konsol üzerinde ?summer1 yazarsak bu fonksiyonun gereksimlerine ulaşılabilir
    print(arg1 + arg2)


summer1(1, 3)


############################
# Fonksiyonların Statement / Body  Bölümü
###########################

# def function_name(parameters/ arguments):
#     statements (function body)

def say_hi(string):
    print(string)
    print("hi")
    print("hello")


say_hi("miuul")


# girilen iki sayıyı çarpan ve önce bir nesne de tutan  ve ondan sonra da yazdıran bir fonksiyon yaz

def sum2(arg1, arg2):
    a = arg1 * arg2
    print(a)


sum2(3, 5)

# girilen değerleri birbiri ile çarpıp liste içinde saklayacak bir fonksiyon

liste_store = []


def add_element(a, b):
    c = a * b
    liste_store.append(c)
    print(liste_store)


add_element(3, 8)
add_element(5, 6)


#######################
# Ön Tanımlı Argümanlar (default parameters/ Arguments)
#######################

def divide1(a, b):
    print(a / b)


def divide(a, b=1):
    print(a / b)


divide(10)


def say_hi(string="merhaba"):
    print(string)
    print("hello")
    print("hi")


say_hi()

###################
# Ne Zaman Fonksiyon Yazılır
####################
# bir belediyenin işe girdik ve belediyenin çeşitli alanlarda sokak lambaları var
# varm, moisture, charge (ısı nem pil)
# don't speed your self
(56 + 15) / 80


# DRY

def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)


calculate(10, 20, 30)


##########################
# Return Fonksiyon Çıktılarını Girdi Olarak Kullanmak
#########################

def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)


calculate(10, 20, 30)


def calculate(varm, moisture, charge):
    return (varm + moisture) / charge


a = calculate(10, 20, 30) * 10


# verilen değerleri 2  ile çarptık sonra her değeri yazdırkık son olarak calculate işlemi yaptık
def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge
    return varm, moisture, charge, output


calculate(10, 20, 30)
varm, moisture, charge, output = calculate(10, 20, 30)
type(calculate(10, 20, 30))  # tuple


##########################
# Fonksiyon İçerisinden Fonksiyon Çağırmak
##############################


def calculate(varm, moisture, charge):
    return int(varm + moisture) / charge


calculate(10, 20, 30) * 10


def standardization(a, p):
    return a * 100 / 100 * p * p


standardization(45, 1)


def all_calculation(varm, moisture, charge, p,a):
    a = calculate((varm, moisture, charge))
    b = standardization(a, p)
    print(b * 10)


all_calculation(1, 3, 5, 12)


############################
# Global And Lokal Değişkenler
###############################


liste_store= [1,2]

def add_Elements(a, b):
    c = a + b
    liste_store.append(c)
    print(liste_store)
    #lokal etki alanından global etki alanını etkilemek

add_Elements(1,9)

