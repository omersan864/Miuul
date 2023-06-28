############################
#ENUMARATE : Otomatik Sayıcı / Index ile for loop
###########################

#bir iterative nesne içerisinde gezinirken  elemanlarına bir şey yaparken aynı zamanda
# o elemanların index bilgilerini de takip etmek istediğimizde

#her bir elemanın index değerini elde etmek için

students =["john", "Mark", "Venessa", "Mariam"]


for index,student  in  enumerate (students):
    print (index, student)


A= []
B= []

for index, student in enumerate (students):
    if index % 2 == 0 :
        A.append(student)
    else:
        B.append(student)


#################################
#Uygulama - Mülakat Sorusu
#################################

#divide_students fonksiyonu yazınız
#çift indexte yer alan öğrncileri bir listeye alınız
#tek indexte yer alan öğrencileri bir listeye alınız
#fakat bu iki liste tek bir liste olarak return olsun

students =["john", "Mark", "Venessa", "Mariam", "Omer"]

A = []
B = []

def divide_students (students):
    groups= [[], []]

    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    return groups


st = divide_students(students)

#####################################
#alternating fonksiyonunun enumerate ile yazılması
#####################################

def altenating_with_enumerate (string):
    new_string = ""
    for i, letter in enumerate (string):
        if i % 2 == 0 :
            new_string += letter.upper()
        else:
            new_string += letter.lower()

    print(new_string)

altenating_with_enumerate("ömersanbir dahi")


###################################
#Zip
#################################
#verilen 3 farklı listenin elemanlarını index değerlerine göre match ediyor

students = ["john", "mark", "venessa", "mariam"]

departments = ["mathematics", "statistic", "physics", "astronomy"]

ages = [23, 30, 26, 22]

list(zip(students,departments,ages))



