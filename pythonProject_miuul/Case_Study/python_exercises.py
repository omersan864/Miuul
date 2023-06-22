x = 8  # x değerine int bir değer atadık
type(x)

y = 3.2  # y değerine float bir değer atadık

z = bj + 18  # bunun bir adı vardı ama unuttum complex gibi birşeydi

a = "hello world"  # a değerine string bir değer atadık

b = True  # b değişkenine bool ifade atadık

c = 23 < 22  # c değişkenine koşul sorduk bize False döndü

l = [1, 2, 3, 4]  # l isimli int değerlerden oluşan bir liste tanımladık

d = {"name": "jake",  # d isimli bir dict sözlük tanımladım key ve value'lerden oluşan
     "age": 27,
     "address": "downtown"}

t = ("machine Learning", "data science")  # t adında bi tuple oluşturdum

s = {"python", "machine learning", "data science"}  # s adında bir set tanımladım

# GÖREV 2
"""Verilen string ifadelerin tüm harflerini büyük harfe çeviriniz 
virgül ve nokta yerine space koyunuz kelime kelime ayırınız"""


def convert_text(text):
    text = text.upper()  # Tüm harfleri büyük harfe çevirme
    text = text.replace(",", " ")  # Virgül yerine boşluk ekleme
    text = text.replace(".", " ")  # Nokta yerine boşluk ekleme
    words = text.split()  # Kelimeleri ayırma
    print(words)
    return words


text = "The goal is turn data into information, and information insight."
converted_text = convert_text(text)
print(converted_text)


def convert_text(text):
    text = text.upper()  # Tüm harfleri büyük harfe çevirme
    text = text.replace(",", " ")  # Virgül yerine boşluk ekleme
    text = text.replace(".", " ")  # Nokta yerine boşluk ekleme
    words = text.split()  # Kelimeleri ayırma
    return words


text = "The goal is turn data into information, and information insight."

convert_text(text)

"""
cevap : mentör  : bir fonksiyon ve döngü kullanmıyor 
direk atama yapıyor mentörümüz (dilara) 
"""


# GÖREV 3

# verilen listeye aşağıdaki adımları uygulayınız

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# 1. verilen listenin eleman sayısına bakınız

len(lst) # eleman sayısına ulaşmak için

# 2. sıfırıncı ve onuncu indeksdeki elemanları çağırınız

lst[0] # index değerleri "0" dan başlar
lst[10]
# bu iki elemanı liste içinde görmek  iki değeri liste içine al

# 3. verilen liste üzerinden  ["D", "A", "T", "A"] listesini oluşturunuz
# ilk 4 değeri almak gerekiyor

new_lst = lst[:4]

# 4. sekizinci indexteki elemanı siliniz

lst.pop(8)
lst

# 5. yeni bir eleman ekleyiniz
lst.append("ÖMER")
lst


# 6. sekizinci indexe "N" elemanını tekrar ekleyiniz

lst.insert(8, "N")
lst
# konumsal  olarak veri eklemek için  insert kullanabilirsin


# GÖREV 4 VERİLEN SÖZLÜK YAPISINA AŞAĞIDAKİ ADIMLARI UYGULAYINIZ

dict = {'christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ['Italy', 25]}

# 1. key değerlerine erişiniz
dict.keys()

# 2. value değerlerine erişiniz
dict.values()

# 3. daisy keyine ait 12 değerini 13 olarak güncelleyiniz

# bu kısımda update methodunu kullan
dict['Daisy'] = ["England", 13]
dict

# 4. key değeri ahmet value değeri ["Turkey", 24] olan bir değer ekle
dict['ahmet'] = ["Turkey", 24]
dict

# 5. antonio'yu dictionary'den siliniz
dict.pop('Antonio')
dict



# GÖREV 5
"""argüman olarak liste alan , listenin içindeki tek ve çift sayıları ayrı 
listelere atayan ve bu listeleri return eden bir fonksiyon yazınız
"""
l = [2, 13, 18, 93, 22]

tek = []
cift = []

def func(list):
    for i in list:
        if i % 2 == 0:
            cift.append(i)
        else:
            tek.append(i)
    return tek, cift
func(l)
# compherension ile yazarsan aşırı kısa ve kolya oluyor



# Görev 6
"""Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri
bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de
tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız."""

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for index, student in enumerate(ogrenciler,1):
    if index <= 3:
        print(f"mühendislik fakültesi {index}.öğrenci{student}")
    else:
        print(f"tıp fakültesi {index-3}.öğrenci{student}")

# eğer listenin uzunluğu bilinmese bile bu kod mükemmel çalışır
# enumerate kullanmadan da yapmayı dene

# GÖREV 7
"""aşağıda 3 adet liste verilmiştir listelerde sırası ile bir dersin kodu 
kredisi ve kontenjan bilgileri yer almaktadır zip kullanarak ders bilgilerini bastırınız"""

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

for credit, ders, kont in zip(kredi,ders_kodu,kontenjan):
    print(f"kredisi {credit} olan {ders_kodu} kodlu dersin kontenjanı {kont}kişidir")


# görev 8
"""
: Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını
eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir"""

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

kume2.difference(kume1)