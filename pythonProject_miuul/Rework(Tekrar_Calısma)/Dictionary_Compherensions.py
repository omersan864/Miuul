###############################
# Dict Compherensions
###############################

dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4}

dictionary.keys() # key değerlerine erişmek istersek

dictionary.values() # value değerlerine erişmek istersek

dictionary.items()  # eğer item çiftlerine bir liste formunda ama her bir elemanı tuple şeklinde ifede edilmiş şekilde

# her bir valuenin karesini almak istiyoruz

{k : v ** 2 for (k, v) in dictionary.items() }
"""
yukarda k değeri key değerlerini  v değeri ise value değerini temsil etmekte 
"""

{k.upper() : v ** 2 for (k, v) in dictionary.items() }


############################
# uygulama - mülakat sorusu
############################

# amaç : çift sayıların karesi alınarak bir sözlüğe eklenmek istenmektedir
# key'ler orjinal değerler value ise değiştirilmiş değerler olacaktır


# bir sözlük içinde gezinmek gerekiyor
# eleman ataması yapılması gerekmekte ama çiftlere atayacağız  teklere atama yapmayacağız
# ve  key value çiftlerini atama yapmadan önceki ve işin daha önemli noktası key değerleri değerlerin kendisi
# value değerleri ise karesi alınmış şekilleri olacak

numbers = range (10) # sıfırdan 10 a kadar sayıları ifade etmektedir
new_dict = {}  # boş bir sözlük oluşturalım



len ("miuul")
len (range(10))

for n in numbers :
    if n % 2 == 0 :
        new_dict[n] = n ** 2
# numbers içinde n olarak gezin
# eğer n değerinin 2 ile bölümünden kalan ifade çift ise
# [] içine girilen değerleri key bölümüne ekliyor otomatik olarak
# aynı n ifadesini = den sonra belirli işleme soktuğumuzda
# value bölümüne ise işleme sokulmuş halini atıyor

{n : n ** 2 for n in numbers if n % 2 == 0  }





