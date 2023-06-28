####################################
# COMPREHENSIONS
####################################
# birden fazla satırda yapılacak işlemleri tek satırda yapmaya çalışmak

########################
# list Comprehensions
########################

# bir liste üzerinde gezip bu elemanlara çeşitli islemler uygulayıp
# daha sonra bu işlem uygulanmış elemanları tekrar bir liste üzerinde görmek istediğimizde

# boş bir liste oluştur , var olan bir liste içerisinde gez  , elemanlara bir işlem yap
# ve hatta if else bloğu ekleyerek  bir koşula göre işlem yap ve sonrasında işlem neticesindeki bu elemanları
# belirli bir liste içerisine tekrar koy

# yukarıdaki işlemler çok işlem adımını barındırmakta bunu tek satırda gerçekleştirmek için_compherensions_kullanırız

salaries = [1000, 2000, 3000, 4000, 5000]


# maaş zammı yapmak istediğimizi düşünelim
# bütün elemanları tek tek yakala ve yazdır

def new_salary(x):
    """
    aldığı x değerini %20 zamlı halini yazdırma fonksiyonu
    Parameters
    ----------
    x : int


    Returns

    -------

    """
    return x * 20 / 100 + x

for salary in salaries:
    print(new_salary(salary))


# zam yapılmış bu maaşları bir listede saklamak istediğimizi düşünelim
new_salaries = []

for salary in salaries:
    print(new_salary(salary))
    new_salaries.append(new_salary(salary))

# eğer burdaki maaşlar 3000'den büyükse tekrar %50 zam yapalım

new_salaries = []

for salary in salaries:
    if salary >= 3000 :
        new_salaries.append(new_salary(salary))
    else:
        new_salaries.append(new_salary(salary*2))



# bu işlem adımlarını list compherension adımları ile nasıl yapabiliriz


[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries]

# adım adım yazalım bir liste oluşturarak başlar
"""
içerisine if else döngü ve matematiksel işlemler yerleştirilerek buradan çıkacak 
olan sonucun tek bir liste halinde  çıkması beklenir 

aşağıda maaşlar listesinde her bir maaşı 2 ile çarpmak istediğimizi düşünelim
"""
# [for salary in salaries] bu şekilde her maaş üzerinde gezeriz

#[salary for salary in salaries ] şu an bütün maaşları yazdırdık

#[salary * 2 for salary in salaries] şu an bütün maaşları 2 ile çarptık

# şimdi maaşı 3000'den az olanları iki ile çarpalım

[salary * 2 for salary in salaries if salary < 3000 ]

"""
DİKKAT !!!!!!!!!!!!

COMPHERENSİONS YAPISINDA EĞER TEK İF KULLANACAKSAK BU FOR YAPISININ SAĞ TARAFINDA OLUR 
İF VE ELSE YAPISINI BİRLİKTE KULLANCAKSAK EĞER FOR YAPISININ SOL TARAFINDA YER ALIR 


"""

[ salary * 2 if salary < 3000 else salary * 0 for salary in salaries ]

# elimizde var olan bir fonksiyonu da bu yapı içerisinde kullanmak istersek

[new_salary(salary * 2 ) if salary < 3000 else salary * 0 for salary in salaries ]


students = ["john", "Mark", "venessa", "mariam"]

students_no = ["john", "venessa"]

# students_no bulunan öğrencilerin isimlerini küçük  student listesinde bununan ama students_no listesinde olamayan
# öğrencilerin adlarını büyük yazdırmak istiyorum

[student.upper() for student in students if student in students_no]
#eğer student değeri students_no içerisinde var ise ismi büyük yap

#ilerleyelim

[student.lower() if student in  students_no else student.upper() for student in students ]

[student.upper() if student not in  students_no else student.lower() for student in students]