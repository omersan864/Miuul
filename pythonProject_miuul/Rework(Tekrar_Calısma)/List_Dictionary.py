###########################
# Liste list
###########################

# değiştirilebilir
# sıralı
# ve kapsayıcı bir veri yapısıdır

notes = [1, 2, 3, 4]
type(notes)

names = ["a", "b", "v", "d"]

not_nam = [1, 2, 3, "a", "b", True, [1, 2, 3]] # bu kapsayıcılığını gösterir
# not_nam değeri 7 elemandan oluşan bir listedir içinde int , string , bool ifade tutar
# içerisinde birden fazla veri yapısını tutabilir

# diyelim ki not_nam içerisinde ilk elemana erişmek istediğimizde
not_nam[0]
not_nam[5]
not_nam[6][1] # içerisindeki listenin ikinci elemanına eriştik
# kontrol etmek amacı ile tip bilgisini isteyebiliriz

type(not_nam[6]) # list dönüyor çıktı olarak
type(not_nam[6][1]) # int dönüyor değer olarak
# bu kısımda da listelerin sıralı yapıda olduğunu görüyoruz
# buradan da yola çıkarak index işlemleri yapılabilir diyoruz

notes[0] # çıktı olarak 1 değerini verdi
# bu değeri değiştirmek istediğimizde
notes[0] = 99

notes[0] # şu an çıktı olarak 99 değerini veriyor
# bu kısımda da listelerin değiştirilebilir olduğunun farkına varıyoruz


# slice dilimleme işlemi gerçekleştirilebilir
not_nam[0:4] # sıfırdan 4 a kadar gir dediğimizde
# Out[16]: [1, 2, 3, 'a'] çıktı olarak bu değeri elde ederiz

################################
# Liste metodları (list methods)
################################

# bu liste veri yapısına uygulanabilecek olan fonksiyon ve metodlar aklımıza gelmeli

# dir(notes) diyerek uygulayabileceğimiz metodlara ulaşabiliriz

len(notes) # boyutun 4 olduğu bilgisine ulaştık
len(not_nam) # 7 elemanlı olduğu bilgisine ulaştık


###########################
# append : eleman ekler
##########################

# append metodu listelere eleman eklemek için kullanılan  yaygın bir metoddur

notes
notes.append(100) # girmiş olduğumuz değeri listeye ekledi


######################
# pop : indexe göre eleman silmek için kullanılır
######################

notes.pop(0) # çıktı olaral 99 verdi
# özellik olarak sıfırıncı indexde ne varsa siler ve sildiği değeri çıktı olarak verir


##############################
# insert : index e göre eleman ekler
############################
# metod önce index değerini ister sonra içeri göndereceğimiz objet değerini alır

notes.insert(2, 99)


##############################
# Sözlük (dictionary)
#############################

# sözlükler key & value çiftleri ile veri tutmayı sağlayan veri yapısıdır
# - değiştirilebilir
# - sırasız (3.7 sürümünden sonra sıralı)
# - kapsayıcı


dictionary = {"REG": "Regression",
              "LOG": "Logistic Regression",
              "CART": "Classiication and Reg"}

dictionary["REG"] # BU KEY değerini çağırdğımızda value değeri gelir

dictionary = {"REG": ["RMSE", 10],
              "LOG": ["MSE", 20],
              "CART": ["SSE", 30]}

# BU KISIMDA  sözlük içine key value değerlerinde value olarak liste de girebiliriz

dictionary = {"REG": 10,
              "LOG": 20,
              "CART": 30}

# key değerimiz string iken value değerimiz integer olabilir

dictionary["REG"] # çıktı olarak 10 değerini aldım bu benim value değerim



dictionary["CART"] # çıktı olarak Out[34]: ['SSE', 30] değeri geliyor
# sadece 30 değerine ulaşmak istersek

dictionary["CART"][1] # çıktı olarak 30 değerine ulaştık


# bu key değerleri üzerinde sorgulama işlemleri gerçekleştirebiliyoruz

#############################
# Key sorgulama
###########################

"REG" in dictionary
"YSA" in dictionary # çıktıyı false olrak aldık çünkü sözlük içinde böyle bir değer yok
10 in dictionary # false cevap

# unutma value sorgulamıyoruz key sorguluyoruz ordan value ye erişebiliriz

#################
# Key' e göre Value ye erişmek
###################

dictionary["REG"] # ÇIKTI OLARAK  Out[40]: ['RMSE', 10]
dictionary.get("REG") # AYNI ÇIKTIYI ALABİLİRİZ  Out[41]: ['RMSE', 10]



###########################
# Value değiştirmek
############################

dictionary["REG"] = ["YSA", 10]
# BU KISIMDA  sözlük içerisinde key ile eriştiğimiz değerin value değerini değiştirdik
# bu kısımdan sonra sözlük değerini tekrar çalıştırdık
# Out[44]: {'REG': ['YSA', 10], 'LOG': ['MSE', 20], 'CART': ['SSE', 30]}


# elimizdeki bir sözlüğün bütün key değerlerine erişebilir miyiz

##########################
# Tüm key değerlerine erişmek
###########################

dictionary.keys()
dictionary.values()

#############################
# tüm çiftleri Tuple halinde listeye çevirme
#############################

dictionary.items()


#####################
# key & value değerlerini güncellemek
######################

dictionary.update({"REG": 11})

###########################
# KEY & VALUE  değeri eklemek
##############################

dictionary.update({"RF": 10})

