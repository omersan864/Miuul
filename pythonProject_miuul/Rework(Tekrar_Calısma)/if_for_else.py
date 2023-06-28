###########################
# Koşullar (conditions)
###########################

# koşullar program  yazımı esnasında akış denetimi sağlayan
# ve belirli kurallara ve koşullara göre nasıl hareket etmesi gerektiğini programa bildiren yapılardır

# örnek : eğer bu koşul sağlanıyorsa bunu yap sağlanmıyorsa bunu yap gibi

# True- False 'yi hatırlayrak başlayalım  ilk koşullarımız bunlar

1 == 1  # True
1 == 2  # False

# if    eğer demektir bu sağlanıyorsa bunu yap sağlanmıyorsa bunu yap

if 1 == 1:
    print("something")
else:
    print("olmadı")  # somthing döndü

if 1 == 2:
    print("something")
else:
    print("olmadı")  # olmadı döndü

number = 11

if number == 10:
    print("number is ten ")
number = 10
number = 20


# kendimizi tekrar etmeye başladık o yüzden fonksiyon yazacağız


def dogrulama(x):
    if x == 10:
        print("number is ten ")
    else:
        print("number is not ten")


dogrulama(40)

dogrulama(10)


def number_check(number):
    if number == 10:
        print("number is ten")
    else:
        print("number is not ten")


number_check(15)
number_check(10)


###################################
# if & else
################################

# verilen yapı true ise ilk print çalışır ama false ise 2. print çalışır

def number_check(number):
    if number == 10:
        print("number is ten")
    else:
        print("number is not ten")


# bir sayının 10 a esit veya büyük veya küçük olma durumunu ele alalım

def number_check(number):
    if number > 10:
        print("number greater than 10 ")
    elif number < 10:
        print("number less 10 ")
    else:
        print("number is ten")


number_check(12)
number_check(9)
number_check(10)

##############################
# döngüler (LOOPS)
#################################

# for loop

students = ["John", "Mark", "Venessa", "Mariam"]

# bu listedeki her bir elemana erişmek istersek

stundents[0]
stundents[1]
stundents[2]
stundents[3]

for i in students:
    print(i)
# her bir elemanı yazdırdık

great_students = []
# yakaladığımız her öğrencinin ismini büyütmek istediğimizi düşüneli

for student in students:
    great = student.upper()
    great_students.append(great)
    print(student.upper())
    print(great_students)

for student in students:
    great = student.upper()
    print(great)

salaries = [1000, 2000, 3000, 4000, 5000]

for i in salaries:
    print(i)

for i in salaries:
    zam = int((i * 10) / 100 + i)
    print(zam)


def new_salary(x):
    for i in salaries:
        zam = int((i * x) / 100 + i)
        print(zam)


new_salary(20)


def new_salary(salary, rate):
    return (salary * rate) / 100 + salary


new_salary(2000, 50)

for salary in salaries:
    print(new_salary(salary, 50))

########################
# özet
############################

salaries = [1000, 2000, 3000, 4000, 5000]


def new_salary(salary, rate):
    return (salary * rate) / 100 + salary


for salary in salaries:
    print(new_salary(salary, 50))

"""
yukarı kısımda kendini tekrar etmeden bir listeye erişip içindeki maaşlara %50
zam yaptık bunu def ve for kullanarak yaptık 
"""

salaries2 = [10700, 25000, 30400, 40300, 50200]

"""
bir döngü aracılığı ile bir listenin bütün elemanlarında geziyoruz 
gezdiğimiz bir elemanı alıp bir fonksiyonun içerisine atıyoruz 
"""

def new_salary(salary, rate):
    return (salary*rate)/100+salary


for salary in salaries2:
    print(new_salary(salary,15))

# maaşı 30000 altında olanlara farklı üstünde olanlara farklı zam yapalım


for salary in salaries2:
    if salary < 30000:
        print(new_salary(salary, 0))
    else:
        print(new_salary(salary, 100))


#############################
#uygulama
############################

# amaç aşağıdaki şekilde string değiştiren bir fonksiyon yaz

# before : hi my name is john and i am learning python
# after :  Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN


range(len("miuul")) # boyut bilgisine ulaştık
# range bize iki değer arasında sayı üretme imkanı sağlar
range(0, 5)
# bu yapı 0 dan 5 e kadar sayıları ifade een veri yapısıdır
# range içinde 0,1,2,3,4  değerlerini tutuyor bu değerler üzerinde gezinme işlemi yapabiliriz

for i in range(0, 5): # çıktı olarak 0,1,2,3,4 değerlerini verdi
    print(i)


for i in range(len("miuul")): # çıktı olarak 0,1,2,3,4 değerlerini verdi
    print(i)

# yaptığım işlemleri kayıtt altına almak için boş bir değişken değeri oluşturduk

"""
def alternating(string):
    new_string = ""
    for string_index in range(len(string)):
        print(string_index)
        
yukarıdaki yapı sayesinde girilen bir değerin bütün index değerleri üzerinde 
sayısal index değerleri olarak gezebiliriz 
"""
def alternating(string):
    new_string = ""
    for string_index in range(len(string)):
        if string_index % 2 == 0 :
            new_string += string[string_index].upper()
        else:
            new_string += string[string_index].lower()

    print(new_string)



alternating("hi my name is john and i am learning python")

alternating("bu nasıl dünya ")


####################################################################

# biz yapalım yukarıdaki işlemi

def problem(string):
    new_string = ""
    for string_index in range(len(string)):
        if string_index % 2 == 0 :
            new_string += string[string_index].upper()
        else:
            new_string += string[string_index].lower()
    print(new_string)


problem("do you hear me ")







