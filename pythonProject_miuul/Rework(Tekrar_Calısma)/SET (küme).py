########################
# set
########################

# değiştirilebilir
# sırasız + eşsizdir
# kapsayıcıdır

########################
# iki kümenin farkı difference()
#########################

set1 = set([1, 3, 5]) # bir liste üzerinden set oluşturuluyor küme
set2 = set([1, 2, 3])

# set 1 de olup 2 de olmayanlar nelerdir

set1.difference(set2)
set1 - set2 # iki küme arası farkı böyle de alabiliriz

# set 2 de olup set 1 de olmayanlar nelerdir

set2.difference(set1)


############################
# symmetric_difference() : iki küme de de birbirlerine göre olmayanlar
###########################

set1.symmetric_difference(set2)
set2.symmetric_difference(set1)




##############################
# intersection() : iki kümenin keşimi
###############################

set1.intersection(set2)
set2.intersection(set1)

set1 & set2  # bu şekilde iki kümenin kesişimini alabiliriz



#######################
# union() : iki kümenin birleşimi
######################

set1.union(set2)
set2.union(set1)



#########################
# isdisjoint() : iki kümenin kesişimi boş mu
##########################

set1.isdisjoint(set2) # cevap False dönecek bool

set2.isdisjoint(set1)



#######################
# issubset() : bir küme diğer kümenin alt kümesi mi
###########################

set1.issubset(set2) # alt küme olmadığı için false döndü

###############
# issuperset() : bir küme diğer kümeyi kapsıyor mu
################

set1.issuperset(set2) # diğer kümeyi kapsamadığı için false döndü



