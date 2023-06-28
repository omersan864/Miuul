#####################################
#lambda, map, filter , reduce
#####################################

#lambda bir kullan at fonksiyondur bir tanımlama yapılmaksızın kullanılabilir

def summer (a, b):
    return a+b
summer (1, 3) * 9

new_sum = lambda a, b : a+b

new_sum (5,2)

#map
#ben seni döngüden kurtarabilirim

salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary (x):
    return x*20/100 + x
new_salary(5000)

for salary in salaries:
    print(new_salary(salary))

list(map(new_salary, salaries))


list(map(lambda x : x * 20 /100 + x , salaries))


list(map(lambda x: x ** 2, salaries))

#FİLTER :

#lista içinde çit sayıları aldık
list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list(filter(lambda x: x % 2 == 0, list_store))


#REDUCE

from  functools import reduce

list_store= [1, 2, 3, 4]

reduce (lambda a, b : a + b , list_store)
