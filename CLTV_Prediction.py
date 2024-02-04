####################################################
# Customer Lİfetime Value Prediction (müşteri yaşam boyu değeri tahmini)
####################################################

# CLTV = Satın alma sayısı   * Satın alma başına ortalama kazanc

# CLTV = (Customer Value / Churn rate) * profit margin

# customer value = Purchase Frequency * Average order value

# yapmamız gereken şey müşteri kitlesinin satın alma davranışları ve satın alma başına bırakacağı
# ortalama kazancı olasılıksal olarak modellemeli ve bu olasılıksal modelin üzerine bir kişinin


# CTLV : Expected Number of Transaction * Expected Average Profit

# CLTV : BG/ NBD model * Gamma Gamma Submodel


####################################################
# BG / NBD (Beta Geometric / Negative Binomial Distribution) ile
# Expected Number of Transaction
####################################################

# Burada kitleden bir dağılım yapısı öğreneceğiz , bu dağılım yapısı kitledeki insanların satın alma
# davranışlarının dağılımı olacak , bu olasılık değerinin bir beklenen değeri olacaktır
# bu olasılıksal beklenilen değeri koşullandırarak yani bireyler özelinde biçimlendirerek
# her bir birey için beklenen işlem değerini tahmin etmeye çalışacağz

# bu modelin diğer adı : Buy Till you die (ölene kadar satın al )


# BG/ NBD modeli Expected Number of Transaction için iki süreci olasılıksal olarak modeller

# 1. Transaction Process (Buy):
# 2. Dropout Process (till you die)


# 1. Tranaction Process (Buy)
# Alive olduğu sürece Belirli bir zaman periyodunda bir müşteri tarafından gerçekleştirilebilecek
# işlem sayısı transaction rate parametresi ile possion dağılır

# yukarıdaki tanımı basite indirgeyelim
# bir müşteri alive olduğu sürece kendi transactionu etrafında rastgele satın alma yapmaya devam edecektir
# Transaction rate'ler her müşteriye göre değişir ve tüm kitle için gamma dağılır (r,a)


# 2. Dropout Process (Till you die) :

# Her bir müşterinin p olasılığı ile dropout rate (dropout probability)'i vardır.
# Bir müşteri alışveriş yaptıktan sonra belirli bir olasılıkla drop olur
# Dropout rate'ler her bir müşteriye göre değişir ve tüm kitle için beta dağılır (a,b)


####################################################
#  Gamma Gamma submodel (satın alma başına ortalama kazanc)
####################################################

# Bir müşterinin İşlem başın ne kadar kar getirebileceğini hesaplamak için kullanılır

# Özellikleri

# 1. Bir müşterinin işlemlerinin parasal değeri (monetary) transaction value'larının ortalaması
#    etrafında rastgele dağılır
# 2. ortalama transaction value zaman içinde kullanıcılar arasında değişebilir fakat tek
#    tek bir kullanıcı için değişmez
# 3. ortalama transaction value  tüm müşteriler arasında gamma dağılır


####################################################
#  CLTV Prediction with BG/NBD & Gamma Gamma
####################################################

# 1. Data preparation (verinin hazırlanması)
# 2. BG / NBD model with Expected Number of Transaction
# 3. Gamma Gamma model with expected average profit
# 4. BG/ NBD ve Gamma Gamma models with calculate CLTV
# 5. Creation of segments by CLTV
# 6. Functionalization of the work (Calışmanın fonksiyonlaştırılması)


####################################################
#  CLTV Prediction with BG/NBD & Gamma Gamma
####################################################

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

################################
# Gerekli kütüphane ve fonksiyonlar
################################

# pip install lifetimes
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from lifetimes import BetaGeoFitter
from lifetimes import GammaGammaFitter
from lifetimes.plotting import plot_period_transactions
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import MinMaxScaler

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
pd.set_option('display.float_format', lambda x: '%.4f' % x)


def outlier_tresholds(dataframe, variable):
    quartile1 = dataframe[variable].quantile(0.01)
    quartile3 = dataframe[variable].quantile(0.99)
    interquartile_range = quartile3 - quartile1
    up_limit = quartile3 + 1.5 * interquartile_range
    low_limit = quartile1 - 1.5 * interquartile_range
    return low_limit, up_limit


def replace_with_treshold(dataframe, variable):
    low_limit, up_limit = outlier_tresholds(dataframe, variable)
    # dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit
    dataframe.loc[(dataframe[variable] > up_limit), variable] = up_limit


df_ = pd.read_excel("CRM_analytic/datasets/online_retail_II.xlsx", sheet_name="Year 2010-2011")
df = df_.copy()

df.describe().T

"""
'Quantity' ve 'Price' değerlerinde dikkatimizi çeken durum min değer negatif olarak görünüyor
    bu iki değişken için max değerler de oldukça yüksek görünüyor bu durumların önüne geçebilmek adına 
    önişlme (data preparation) işleminin gerçekleştirilmesi gerekmektedir
"""

df.head()
"""
değişkenlerimiz arasında "Quantity" ve "Price" adından iki değişken var 
bu değişkenlerin içinde ürünün birim fiyatı ve satış adedi bulunmakta bu iki
değişkenden faydalanarak her bir ürüne toplam ne kadar ödendiğini bulabiliriz
(daha sonrasında bunu kullanıcı özelinde genişletmemiz mümkün fakat burda dikkat edilmesi gereken nokta 
hesaplanan total price bir ürün adedi ile fiyatın çarpımı fakat bize gereken bir fatura için ne kadar ödediğimiz
bu yüzden hesaplanan totalprice'ın sum değeri alınır ve fatura başına ne kadar ödediğimiz
belirlenir)


"""

################################
# Data Preparation
################################

# Öncelikle veri seti içindeki eksik değerleri gözlemleyelim
df.isnull().sum()  # hangi değişkende kaç eksik değer var
"""
müşteri özelinde işlem yaptığımız için ID değeri olmayan müşterileri silmemiz gerekiyor

"""

df.dropna(inplace=True)

# bu işlemden sonra değişiklik olup olmadığını kontrol etmek için tekrar
# df.describe().T fonksiyonunu çalıştırdıktan sonra değişiklikleri kontrol edebiliriz
"""
tanımlayıcı istatistik değerlerin baktıktan son yapabileceğimiz bir diğer çıkarım 

=> değişkenin %75'lik değeri 12 olurken max değeri 80995 olması bir aykırı değer problemini ortaya koymaktadır

=> Bir diğer durum Invoice değişkeninde 'C' ile ifade edilen değerler iade edilen faturaları göstermektedir
    Bu yüzden bu değerleri dataframe'den çıkarmamız gerekmektedir
"""

df = df[~df['Invoice'].str.contains("C", na=False)]

df.shape
# Değişiklikleri tekrar görmek adına df.describe().T fonksiyonunu tekrar çalıştırıyoruz
# hesaplamalarda adetler için sıfır değerinin altında kalanları yine dataframe den çıkarmak adına

df = df[df['Quantity'] > 0]
df = df[df['Price'] > 0]

"""
Bu dataframe de 'Quantity' ile 'Price' değişkenleriyle yeni değişkenler oluşturacağız ve yine bu değerler üzerinden 
modellerimizi kuracağız dolayısı ile bu değişkenlerin içinde yer alan aykırı değerlerden kurtulmamız gerekmektedir
(içerde yer alan ayrkırı değerler yapılacak olan genellemelerde sapmalara neden olabilir) eşik değerler ile .

"""

replace_with_treshold(df, "Quantity")
replace_with_treshold(df, "Price")

# değişiklikleri gözlemlemek adına tekrar tanımlayıcı istatistik değerlerine bakalım


# Her bir ürüne Ödenen tutarı bulmak için total Price adında bir değişken oluşturuyoruz

df["TotalPrice"] = df["Quantity"] * df["Price"]

# Bir fatura için ne kadar ödediğimi bulmak istersem müşteri özelinde segmente ettikten sonra
# total price değerinin sum'ını almam yeterli olacaktır

# bir diğer işlemimize geçelim analizi yaptığımız günü programa verilim

today_date = dt.datetime(year=2021, month=12, day=11)

####################################################
#  Preparation of Lifetime Data Structure (Lifetime veri yapısının hazırlanması)
####################################################

# BG/NBD ve Gamma Gamma modellerinin beklediği özel bir veri formatı var
# Veriyi Kullanıcı bazında özelleştirmemiz gerekmektedir

# Recency : Son satın alma üzerinden geçen zaman. Haftalık (Kullanıcı Özelinde)
# T: müşterinin yaşı.Haftalık . (Analiz tarihinden ne kadar süre önce ilk satın alma yapılmış)
# Frequency : tekrar eden toplam satın alma sayısı  (frequency > 1)
# monetary_value : satın alma başına ortalama kazanç

cltv_df = df.groupby("Customer ID").agg({"InvoiceDate": [lambda InvoiceDate: (InvoiceDate.max() - InvoiceDate.min()).days,
                                                         lambda InvoiceDate: (today_date - InvoiceDate.min()).days],
                                         "Invoice": lambda num: num.nunique(),
                                         "TotalPrice": lambda TotalPrice: TotalPrice.sum()})
"""
=> Yukarıda 'InvoiceDate' değişkeni ile date.max() diyerek son alışveriş tarihinden date.min() diyerek ilk alışveriş
tarihinden çıkarıyoruz bu sayde müşterinin Recency değerini elde ediyoruz

=> ardından müşterinin yaşını hesaplamak 
istiyruz analiz yaptığımız tarihten müşterinin ilk alışveriş yaptığı tarihi çıkartıyoruz 

=> 'Invoice' değişkeni ile müşteriye ait benzersiz fatura adedini öğreniyoruz (Frequency)

=> 'TotalPrice' değişkeni ile müşteri bazlı  bir faturada yer alan ürün kalemlerinin parasal toplam değerini alıyoruz
"""

cltv_df.columns = cltv_df.columns.droplevel(0)

cltv_df.columns = ['recency', 'T', 'frequency', 'monetary']

cltv_df['monetary'] = cltv_df['monetary'] / cltv_df['frequency']
"""
monetary değerini  müşterinin alışveriş sıklığına bölersek eğer ortalam olarak bir alışverişte bıraktığı 
parasal değeri bulmuş oluruz
"""

cltv_df.describe().T

cltv_df = cltv_df[(cltv_df['frequency'] > 1)]

cltv_df["T"] = cltv_df["T"] / 7  # HAFTALIK DEĞERE DÖNÜŞTÜRDÜM

####################################################
# 2. BG / NBD model with Expected Number of Transaction (Model Kurulumu)
####################################################


bgf = BetaGeoFitter(penalizer_coef=0.001)
"""
BetaGeoFitter(penalizer_coef=0) ile bir model nesnesi oluşturacağız ve bu model nesnesi aracılığıyla 
fit() methodunu kullanarak frequency recency ve müşteri yaşlarını fit() methoduna verdiğimizde modeli kurmuş olacağız

"""

bgf.fit(cltv_df['frequency'],
        cltv_df['recency'],
        cltv_df['T'])

##################################################
# 1 hafta içinde en çok satın alma beklediğimiz müşteri Kimdir ?
##################################################


bgf.conditional_expected_number_of_purchases_up_to_time(1,
                                                        cltv_df['frequency'],
                                                        cltv_df['recency'],
                                                        cltv_df['T']).sort_values(ascending=False).head(10)

"""
Verimizi haftalık değerlere göre oluşturduğumuz için yukarı 1 değerini girdik bu sayede 1 haftalık period içinde 
tahmin edeğerimizi elde edeceğiz

yukarda verilen tahmin işleminde kullanılan fonksiyonun adı çok uzun aynı işlevi gören farklı bir fonksiyonumz
daha var örnek gösterimi aşağıda yer almakta
"""
bgf.predict(1,
            cltv_df['frequency'],
            cltv_df['recency'],
            cltv_df['T']).sort_values(ascending=False).head(10)

cltv_df["expected_purch_1_week"] = bgf.predict(1,
                                               cltv_df['frequency'],
                                               cltv_df['recency'],
                                               cltv_df['T'])


##################################################
# 1 ay içinde en çok satın alma beklediğimiz müşteri Kimdir ?
##################################################

cltv_df["expected_purch_1_month"] = bgf.predict(4,
                                                cltv_df['frequency'],
                                                cltv_df['recency'],
                                                cltv_df['T']).sort_values(ascending=False).head(10)

cltv_df["expected_purch_1_month"] = bgf.predict(4,
                                                  cltv_df['frequency'],
                                                  cltv_df['recency'],
                                                  cltv_df['T'])

#cltv_df = cltv_df.drop('expected_purch_1_nonth', axis=1)


"""
Örnek çıkarım madem bütün müşteriler adına çıkarımda bulunabiliyoruz o zaman şirket adına düşünüp
aylık bazda ne kadar satın alma olabileceğini öngörebiliriz 
"""

bgf.predict(4,
            cltv_df['frequency'],
            cltv_df['recency'],
            cltv_df['T']).sum()


##################################################
# 3 ayda tüm şirketin beklenen satış sayısı nedir ?
##################################################


bgf.predict(4 * 3,
            cltv_df['frequency'],
            cltv_df['recency'],
            cltv_df['T']).sum()

cltv_df["expected_purch_3_month"] = bgf.predict(4 * 3,
                                                cltv_df['frequency'],
                                                cltv_df['recency'],
                                                cltv_df['T'])





##################################################
# Tahmin sonuçlarının değerlndirilmesi
##################################################

# basit bir grafik ile tahmin sonuçlarının başarısı değerlendirilebilir

plot_period_transactions(bgf)
plt.show()





####################################################
# 3. Gamma Gamma model with expected average profit
####################################################

ggf = GammaGammaFitter(penalizer_coef=0.01)

ggf.fit(cltv_df["frequency"], cltv_df["monetary"])

ggf.conditional_expected_average_profit(cltv_df["frequency"],
                                        cltv_df["monetary"]).head(10)

cltv_df["expected_average_profit"] = ggf.conditional_expected_average_profit(cltv_df["frequency"],
                                                                             cltv_df["monetary"])



cltv_df.sort_values("expected_average_profit", ascending=False).head(10)





####################################################
# 4. BG/ NBD ve Gamma Gamma models with calculate CLTV
####################################################

cltv = ggf.customer_lifetime_value(bgf,
                                   cltv_df["frequency"],
                                   cltv_df["recency"],
                                   cltv_df["T"],
                                   cltv_df["monetary"],
                                   time= 3,  # 3 aylık
                                   freq="W",  # T'nin frekans bilgisi
                                   discount_rate=0.01)



cltv.head()

cltv = cltv.reset_index()

cltv_final = cltv_df.merge (cltv, on = "Customer ID", how = "left")
cltv_final.sort_values(by="clv", ascending=False).head(10)


"""
Recency değeri kendi içinde yüksek olan müşteriler nasıl oluyorda en büyük değeri vaad ediyor ? 
(aslında recency değerinin düşük olmasının iyi olduğunu düşünürsek)
BUY TİLL YOU DİE kavramı der ki "senin düzenli bir ortalama işlem kapasiten olan müşterin eğer churn olmadıysa 
(eğer DROPOUT olmadıysa) müşterinin recency değeri arttıkça satın alma olasılığı yükseliyor der"

recency : müşterinin son satın alması üzerinden geçen zaman diliminin süresini ifade eder
"""





####################################################
# 5. Creation of segments by CLTV
####################################################


cltv_final["segment"] = pd.qcut(cltv_final["clv"], 4,labels=["D", "C", "B", "A"])

cltv_final.sort_values(by="clv", ascending=False).head(50)

cltv_final.groupby("segment").agg({"count", "mean", "sum"})


####################################################
# 6. Functionalization of the work (Calışmanın fonksiyonlaştırılması)
####################################################

def create_cltv_p(dataframe, month=3):
    # 1. Data Preparation
    dataframe.dropna(inplace=True)
    dataframe = dataframe[~dataframe["Invoice"].str.contains("C", na=False)]
    dataframe = dataframe[dataframe["Quantity"] > 0]
    dataframe = dataframe[dataframe["Price"] > 0]
    replace_with_treshold(dataframe, "Quantity")
    replace_with_treshold(dataframe, "Price")
    dataframe["Total_Price"] = dataframe["Quantity"] * dataframe["Price"]
    today_date = dt.datetime(2011,12,10)

    cltv_df = dataframe.groupby("Customer ID").agg({'InvoiceDate': [lambda InvoiceDate: (InvoiceDate.max() - InvoiceDate.min()).days,
                                                               lambda InvoiceDate: (today_date - InvoiceDate.min()).days],
                                                'Invoice': lambda Invoice : Invoice.nunique(),
                                                'Total_Price': lambda TotalPrice: TotalPrice.sum()})

    cltv_df.columns = cltv_df.columns.droplevel(0)
    cltv_df.columns = ["recency", "T", "frequency", "monetary"]
    cltv_df["monetary"] = cltv_df["monetary"] / cltv_df["frequency"]
    cltv_df = cltv_df[cltv_df["frequency"] > 1]
    cltv_df["recency"] = cltv_df["recency"] / 7
    cltv_df["T"] = cltv_df["T"] / 7

    #BG / NBD creating model

    bgf = BetaGeoFitter(penalizer_coef=0.001)
    bgf.fit(cltv_df["frequency"],
            cltv_df["recency"],
            cltv_df["T"])

    cltv_df["expected_purch_1_week"] = bgf.predict(1,
                                                   cltv_df["recency"],
                                                   cltv_df["recency"],
                                                   cltv_df["T"])

    cltv_df["expected_purch_1_month"] = bgf.predict(4,
                                                   cltv_df["recency"],
                                                   cltv_df["recency"],
                                                   cltv_df["T"])
    cltv_df["expected_purch_3_month"] = bgf.predict(12,
                                                   cltv_df["recency"],
                                                   cltv_df["recency"],
                                                   cltv_df["T"])

    # 3. Gamma Gamma  creating model

    ggf = GammaGammaFitter(penalizer_coef=0.01)
    ggf.fit(cltv_df["frequency"], cltv_df["monetary"])
    cltv_df["expected_average_profit"] = ggf.conditional_expected_average_profit(cltv_df["frequency"],
                                                                                 cltv_df["monetary"])

    # BG / NBD VE GG modeli ile CLTV'nin hesaplanması

    cltv = ggf.customer_lifetime_value(bgf,
                                       cltv_df["frequency"],
                                       cltv_df["recency"],
                                       cltv_df["T"],
                                       cltv_df["monetary"],
                                       time=month,
                                       freq="W",
                                       discount_rate=0.01)

    cltv = cltv.reset_index()
    cltv_final = cltv_df.merge(cltv, on="Customer ID", how="left")
    cltv_final["segment"] = pd.qcut(cltv_final["clv"], 4, labels=["D", "C", "B", "A"])

    return cltv_final

df = df_.copy()

cltv_final2 = create_cltv_p(df)

cltv_final2.to_csv("cltv_prediction.csv")

cltv_final2.groupby("segment").agg({"count", "mean", "sum"})




















