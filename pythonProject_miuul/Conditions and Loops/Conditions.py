############################
# KOŞULLAR (CONDITIONS)
############################

# Program akışının belirli koşullar altında ilerlemesini sağlayan yapılardır

# True-False hatırlayarak başlayalım
1 == 1
1 == 2  # False dönmek zorunda

# if

if 1 == 1:
    print("something")

if 1 == 2:
    print("something")

number = 10

if number == 10:
    print("number is 10")


def number_check(number):
    if number == 10:
        print("number is 10")


number_check(12)
number_check(10)


# else

def number_check(number):
    if number == 10:
        print("number is 10")
    elif number <= 10:
        print("10'dan küçük")
    elif number >= 10:
        print("10'dan büyük")
    else:
        print("number is not 10")


number_check(12)
number_check(10)
number_check(8)

###########################
#Döngüler (LOOPS)
###########################

#FOR LOOPS

students = ["john", "mark", "venessa", "mariam"]

students[0]
students[1]
students[2]
students[3]

for student in students :
    print(student)

for student in students:
    print(student.upper())
    #her öğrencinin isimlerini büyük harf ile yazdık

salaries = [1000, 2000, 10000, 30000, 50000]

for i in salaries:
    print(i)

for i in salaries:
    print(int((i*20)/100+i))


def new_salary (salary,rate):
    return int(salary *rate/100+salary )

new_salary(1500,10)
new_salary(2000,50)


for salary in salaries:
    print (new_salary(salary,10)) # bütün maaşlara %10 zam yaptık

salaries2 = [12000, 22000, 30000, 120000, 320000, 520000]

for salary in salaries2:
    print(new_salary(salary, 10))

for salary in salaries2:
    if salary > 30000:
        print(new_salary(salary,50))
    elif salary < 30000:
        print (new_salary(salary ,100))


#####################################
#UYGULAMA - MÜLAKAT SORUSU
#####################################

# Amaç Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz

#before : "hi my name is john and i am learning python"
# after : "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

# Tek index değerine sahip  ifadeleri büyüt çift index değerine sahip ifadeleri küçült

range(len("miuul"))
range(0, 5)

for i in range (len("miuul")):
    print(i)



def alternating (string):
    new_string = ""
    #girilen string'in index değerinde gez.
    for string_index in range(len(string)):
        #index çift ise büyük harfe çevir
        if string_index % 2 == 0 :
            new_string += string[string_index].upper()
            #index tek ise küçük harfe çevir
        else:
            new_string += string[string_index].lower()
    print(new_string)

alternating("ömerşan")
alternating("Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN")
alternating("hi my name is john and i am learning python")


