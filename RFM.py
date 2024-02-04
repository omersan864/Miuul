########################################################
# RFM ile Müşteri Segmentasyonu (Customer Segmentaition with RFM)
########################################################

# 1. İş Problemi ( Business Problem )
# 2. Veriyi Anlama (Data Understanding)
# 3. Veriyi Hazırlama ( Data Preparation)
# 4. RFM Metriklerinin Hesaplanması ( Calculating RFM Metrics )
# 5. RFM Skorlarının Hesaplanması (Calculating RFM Scores )
# 6. RFM SEegmentlerinin oluşturulması ve Analiz Edilmesi (Creting & Analysing RFM Segments)
# 7. Tüm Sürecin Fonksiyonlaştırılması


###############################################
# 1. İş Problemi ( Business Problem )
###############################################

# Bir E-Ticaret şirketi müşterilerinin segmentlere ayırıp bu segmentlere göre
# pazarlama stratejileri belirlenmek isteniyor

# veri seti hikayesi
# https://archive.ics.uci.edu/ml/datasets/Online+Retail+II

# Online Retail II isimli veri seti İngiltere merkezli online bir satış mağazasının
# 01/12/2009 - 09/12/2011 tarihleri arasındaki satışlarını içeriyor.

# Değişkenler

# InvoiceNo: Fatura numarsı. Her işleme yeni faturaya ait eşsiz numara. C ile başlıyorsa iptal edilen işlem
# StockCode : Ürün Kodu her bir ürün için eşsiz bir numara
# Description : ürün ismi
# Quantity : Ürün adedi Faturalardaki ürünlerden kaçar adet satıldığını ifade etmektedir
# InvoiceDate : Fatura tarihi ve zamanı
# UnitPrice : Ürün Fiyatı (Sterlin cinsinden)
# CustomerID : Eşsiz Müşteri numarsı
# Country : Ülke ismi , Müşterinin yaşadığı Ülke



###############################################
# # 2. Veriyi Anlama (Data Understanding)
###############################################

import datetime as dt
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

df_ = pd.read_excel("CRM_analytic/datasets/online_retail_II.xlsx", sheet_name="Year 2009-2010")
df = df_.copy()
df.head()
df.shape # Out[4]: (525461, 8)
df.isnull().sum()  # customerID ve description sütunlarında eksik değer olduğunu gözlemliyoruz
# müşteri özelinde segmentasyon yapacağımız için ID bilgisi olmayan müşteriler işe yaramaz
# bu yüzden bu müşterileri siliyoruz

# eşsiz ürün sayısı nedir ?
df["Description"].nunique() # Out[8]: 4681 tane benzersiz ürünümüz vardır

df["Description"].value_counts().head() # ürün ve o üründen ne kadar Eşsiz olarak satıldığını gösterir

# yani faturada 10 tane geçsede de o faturda eşsiz olarak 1 ürün temsil ediliyor



# en cok sipariş edilen ürün hangisidir dersek

df.groupby("Description").agg({"Quantity": "sum"}).head()

df.groupby("Description").agg({"Quantity": "sum"}).sort_values(by="Quantity", ascending=False).head()
# her bir ürünün toplam satışını gösteriyor yani faturada 10 kere geçiyorsa 10 kez satılmıştır

# veri setinde eşsiz fatura sayısı nedir

df["Invoice"].nunique()  # burda toplamm 28818 fatura kesilmiş


# fatura başı toplam ne kadar kazanılmıştır

df.head()
df.groupby("Invoice").agg({"Price": "sum"})
# yukarıdaki işlem olmuyor cünkü fatura işlemleri coklanmış durumda aynı fatura her ürün için karşımıza çıkıyor

df["Monetary"] = df["Quantity"] * df["Price"]
df.head()

df = df.rename(columns={"Monetary": "Total_Price"})

# elde ettiğimiz Total_Price değişkeni ile ürün bazında toplam kazancı bulmuş olduk ancak fatura başı toplam kazanc lazım

df.groupby("Invoice").agg({"Total_Price": "sum"}).head()
# şu an fatura özelinde bir fatura için eşsiz olarak elde edilen bedel gösterildi

# bunu aşağıda görebilirsiniz toplam fatura adedini eşsiz olarak yukarıda çekmiştik
# şu an eşsiz her fatura için ödenen bedeli görebiliriz
omer = df.groupby("Invoice").agg({"Total_Price": "sum"})

omer.shape


###############################################
# # 3. Veriyi Hazırlama ( Data Preparation)
###############################################

df.head()
df.shape
df.isnull().sum()

# yukarda da bahsettiğimiz ID'si olmayan değişkenleri veri setinden çıkartıyoruz
# bunun sebebi Müşteri özelinde segmente etmemiz

df.dropna(inplace=True)  # eksik değerlerin hepsini silecek
# Out[53]: (417534, 9)  sonucunda elimizde kalan veri sayısı

df.describe().T

# iade edilen faturalrı işlemlerinizden çıkarmamız lazım

df[~df["Invoice"].str.contains("C", na=False)]  # Invoice değişkeni içinde başında c olan değişkenleri çıkardık şu an

df = df[~df["Invoice"].str.contains("C", na=False)]   # kalıcı olması için df değişkenine atama yaptık



###############################################
# 4. RFM Metriklerinin Hesaplanması ( Calculating RFM Metrics )
###############################################

# Recency ,frequency , Monetary

# Recency : Yenilik : müşterinin alışveriş yaptığı son zamandan bugüne kadar ki geçen süre (analiz tarihi - son satın alım)

# Frequency : müşterinin yaptığı toplam satın alma

# Monetary :  toplam satın alma neticesinde bıraktığı parasal değer


df.head()

# Not burda veri setinin tarihini ve analizi yaptığımız gün önem arz etmektedir
# analizi veri setinin oluşturulduğu zamanda yapmak istiyoruz o yüzden veri setinin son tarihine erişip üzerine
# iki gün ekliyoruz

df["InvoiceDate"].max()  # Out[57]: Timestamp('2010-12-09 20:01:00')

# analiz tarihini (2010-12-11) olarak belirliyoruz

today_date = dt.datetime(year=2010, month=12, day=11)

type(today_date)

rfm = df.groupby("Customer ID").agg({"InvoiceDate": lambda InvoiceDate: (today_date - InvoiceDate.max()).days,
                                     "Invoice": lambda Invoice : Invoice.nunique(),
                                     "Total_Price": lambda Total_Price: Total_Price.sum()})

rfm.head()


# customerID coklama durumunda ürünler coklama olduğundan dolayı

rfm.shape
rfm.columns = ["Recency", "Frequency", "Monetary"]

rfm.head()

# ne durumda olduğumuza bir bakalım

rfm.describe().T

# burda min değeri 0 olan bir monetary değeri istemiyoruz bu yüzden değeri sıfır olanları çıkartıyoruz

rfm = rfm[rfm["Monetary"] > 0]


# şu an metrik değerlerini elde ettik bunları skorlara dönüştürmemiz lazım segment aşamasına gidebilmek için


###############################################
# # 5. RFM Skorlarının Hesaplanması (Calculating RFM Scores )
###############################################

# burda unutulmaması gereken bir nokta standardize ederken büyüklük algısını
# recency için küçük olan değer daha değerli (örnek yeni alışveriş yapmış)
# frequency ve monetary için büyük olan daha değerli (örnek daha çok para ve alışveriş sayısı)

rfm["recency_score"] = pd.qcut(rfm["Recency"], 5, labels=[5, 4, 3, 2, 1])

"""
elimizde 1-100 arasında değişen değişken var bu değişkeni qcut fonksiyonu ile çeyrek değerlerine bölüp
oradaki isimlendirmeleri değiştirmek istediğimizi düşünelim 
farklı bir örenk olarak yaş değişkeni olsun 0-80 arasında değişiyor ben bunu çeyreklik değerlerine göre
bölüp segmente ettikten sonra isimlendirmek istiyorum (cocuk- genc- yaşlı gibi )
"""

rfm.head()

rfm["frequency_score"] = pd.qcut(rfm["Frequency"], 5, labels=[1, 2, 3, 4, 5])

rfm["frequency_score"] = pd.qcut(rfm["Frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])

rfm["monetary_score"] = pd.qcut(rfm["Monetary"], 5, labels=[1, 2, 3, 4, 5])

rfm["RFM"] = (rfm["recency_score"].astype(str) + rfm["frequency_score"].astype(str))

rfm.describe().T # yeni hesapladığım skor gelmedi çünkü str tipte

# örnek olarak en iyi müşterileri görmek istersek

sample = rfm[rfm["RFM"] == "55"]

sample.shape # burdan da en iyi kaç müşterimiz olduğunu görüyoruz


# bu kısma kadar skorlama işleminş bitirdik artık segment aşamasına geçebiliriz



###############################################
# 6. RFM SEegmentlerinin oluşturulması ve Analiz Edilmesi (Creting & Analysing RFM Segments)
###############################################

# RFM isimlendirmesi
seg_map = {
    r'[1-2][1-2]': 'hibernating',
    r'[1-2][3-4]': 'at_risk',
    r'[1-2]5': 'cant_loose',
    r'3[1-2]': 'about_to_sleep',
    r'33': 'need_attention',
    r'[3-4][4-5]': 'loyal_customers',
    r'41': 'promising',
    r'51': 'new_customer',
    r'[4-5][2-3]': 'potential_loyalist',
    r'5[4-5]': 'champions'
}


rfm["segmentation"] = rfm["RFM"].replace(seg_map, regex=True)

#rfm = rfm.drop("segmentation", axis=1)

rfm.head()

# burda işlemleri tamamladık şimdi yapmamız gereken anlamak ve analiz etmek
# ufak bir analiz ile başlayalım segment bazında müştr sayıslarını ve ort. bulalım


rfm[["segmentation", "Recency", "Frequency", "Monetary"]].groupby("segmentation").agg(["mean", "count"])

# burdan bir sınıfa odaklanmak istediğimizi düşünelim ve bu sınıfın müşterilerini seçelim

rfm[rfm["segmentation"] == "need_attention"].head()
rfm[rfm["segmentation"] == "cant_loose"].index
rfm[rfm["segmentation"] == "hibernating"].head()
rfm[rfm["segmentation"] == "new_customer"].head()

# index bilgilerine erişebildiğimiz bu müşterileri dışarı alalım

new_df = pd.DataFrame()
new_df["new_customer_id"] = rfm[rfm["segmentation"] == "new_customer"].index
new_df["new_customer_id"] = new_df["new_customer_id"].astype(int)

# şimdi dışarı çıkaralım

new_df.to_csv("new_customers.csv")
rfm.to_csv("rfm_segmentation.csv")



###############################################
# # 7. Tüm Sürecin Fonksiyonlaştırılması
###############################################

def create_rfm (dataframe, csv=False):

    # DATA PREPARATION
    dataframe["Total_Price"] = dataframe["Quantity"] * dataframe["Price"]
    dataframe.dropna(inplace=True)
    dataframe = dataframe[~dataframe["Invoice"].str.contains("C", na=False)]

    # RFM Metriklerinin Hazırlanması
    today_date = dt.datetime(year=2011, month=11, day=11)
    rfm = dataframe.groupby("Customer ID").agg({"InvoiceDate": lambda date: (today_date - date.max()).days,
                                                "Invoice": lambda num: num.nunique(),
                                                "Total_Price": lambda price: price.sum()})

    rfm.columns = ["Recency", "Frequency", "Monetary"]
    rfm = rfm[(rfm["Monetary"] > 0)]

    # RFM skorlarının hesaplanması
    rfm["recency_score"] = pd.qcut(rfm["Recency"], q=5, labels=[5, 4, 3, 2, 1])
    rfm["frequency_score"] = pd.qcut(rfm["Frequency"].rank(method="first"), q=5, labels=[1, 2, 3, 4, 5])
    rfm["monetary_score"] = pd.qcut(rfm["Monetary"], q=5, labels=[1, 2, 3, 4, 5])

    # cltv_df skorları kategorik değerlere dönüştürülüp df' eklendi
    rfm["RFM_SCORE"] = rfm["recency_score"].astype(str) + rfm["frequency_score"].astype(str)

    # SEGMENTLERİN İSİMLENDİRİLMESİ
    seg_map = {
        r'[1-2][1-2]': 'hibernating',
        r'[1-2][3-4]': 'at_risk',
        r'[1-2]5': 'cant_loose',
        r'3[1-2]': 'about_to_sleep',
        r'33': 'need_attention',
        r'[3-4][4-5]': 'loyal_customers',
        r'41': 'promising',
        r'51': 'new_customer',
        r'[4-5][2-3]': 'potential_loyalist',
        r'5[4-5]': 'champions'
    }
    rfm["segment"] = rfm["RFM_SCORE"].replace(seg_map, regex=True)
    #rfm = rfm[["Recency", "Frequency", "Monetary", "segment"]]
    rfm.index  = rfm.index.astype(int)

    if csv:
        rfm.to_csv("rfm_segmentation_fonk.csv")
    return rfm

rfm = create_rfm(df)























