###################################
# FONKSİYONLAR , KOŞULLAR , DÖNGÜLER , COMPHERENSİONS
####################################

# - Fonksiyonlar (Functions)
# - Koşullar (Conditions)
# - Döngüler (Loops)
# - comprehesions


###################################
# FONKSİYONLAR (FUNCTİONS)
####################################

# FONKSİYON BELİRLİ GÖREVLERİ YERİNE GETİRMEK İÇİN YAZILAN KOD PARÇALARIDIR


###################################
# FONKSİYONLAR (FUNCTİONS) tanımlama
####################################

# noinspection PyTypeChecker
def calculate(a, b):
    print(a + b)


calculate(3, 5)


# iki argümanlı bir fonksiyon oluşturalım

def summer(arg1, arg2):
    print(arg1 + arg2)


summer(7, 8)


#########################
# Docstring
#######################

def summer(arg1, arg2):
    """

    Parameters
    ----------
    arg1
    arg2

    Returns
    -------

    """
    print(arg1 + arg2)


###################
# fonksiyonların gövde bölümü
####################

def say_hi():
    print("merhaba")
    print("hi")
    print("hello")


say_hi()


def say_hi(str):
    print(str)
    print("hi")
    print("hello")


say_hi("ömer")
say_hi(32)


# girilen iki nesneyi tutan ve bu nesneleri bir değerde tutan ve sonra ekrana yazdıran

def calculate(x, y):
    a = x * y
    print(a)


calculate(10, 30)

# girilen değerleri bir liste içinde saklayacak bir liste tanımlayalım

liste = []


def cach(arg):
    liste.append(arg)
    print(liste)


cach("ömer")


############################
# ön tanımlı argümanlar
###############################


def divide(arg1, arg2):
    print(arg1 / arg2)


divide(30, 10)


def divide(arg1, arg2=1):
    print(arg1 / arg2)


divide(10)


def say_hi(str="merhaba"):
    print(str)
    print("hi")
    print("hello")


say_hi("ömer")
say_hi()  # bu kısımda ön tanımlı argüman devreye girer


##############################
# ne zaman fonksiyon yazmaya ihtiyacımız olur
#################################

# varm, moisture, charge
# dont repeat your self  kendini tekrar eden görevler olduğunda fonksiyon yaz

# DRY

def calculate(a, b, c):
    d = (a + b) / c
    print(d)


calculate(98, 12, 78)


###############################
# RETURN : Fonksiyon çıktılarını girdi olarak kullanmak
##############################


def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge
    return varm, moisture, charge, output


calculate(98, 12, 78)

varm, moisture, charge, output = calculate(98, 12, 78)


#########################
# Fonksiyon içerisinden onksiyon çağırmak
#########################


def calculate(varm, moisture, charge):
    return int((varm + moisture) / charge)


calculate(90, 12, 12) * 10


# bu sayının float olmasını değil de int olmasını istiyorum

def standardization(a, p):
    return a * 10 / 100 * p * p


standardization(45, 1)


def all_calculation(varm, moisture, charge, p):
    a = calculate(varm, moisture, charge)
    b = standardization(a, p)
    print(b * 10)


all_calculation(1, 3, 5, 12)
