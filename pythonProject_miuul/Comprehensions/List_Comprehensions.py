#################################
#COMPREHENSIONS
#################################
#Birden fazla satır ve kod ile  yapılabilecek işlemleri  tek bir satırda gerçekleştirme


#################################
#List Comprehensions
#################################

salaries = [1000, 2000, 3000, 4000, 5000]


def new_salary (x):
    return x * 20 / 100 + x

null_list = []

for salary in salaries:
    null_list.append(new_salary(salary))

null_list = []
for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary* 2))



[new_salary(salary * 2 ) if salary < 3000 else new_salary(salary) for salary in salaries]

# []  parantez ile başlarız olaya

[salary * 2 for salary in salaries ] # maaşları iki ile çarptık

maas = [salary * 2 for salary in salaries if salary < 3000] # maaşı 3k dan küçük olan maaşları 2 ile çarptık

#eğer tek bir if kullanıyorsak else olmadan yani  o zaman if değeri sağa yazılır
# eğer else ile yazacaksak for bölümü sağ tarafta kalmalıdır

maas = [salary * 2 if salary < 3000 else salary * 0 for salary in salaries ] #

maas = [new_salary( salary * 2 ) if salary < 3000 else new_salary(salary * 0.2)for salary in salaries ]


students = ["john", "mark", "venessa", "mariam"]

students_no = ["john", "Venessa"]

ogr= []
ogr=[student.upper() if student not in students_no else student.lower() for student in students]



