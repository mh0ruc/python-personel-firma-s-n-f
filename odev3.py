class personel: 
    def __init__(self, ad, soyad,departman,calisma_yili,maas) :
        self.ad=ad
        self.soyad=soyad
        self.departman=departman
        self.calisma_yili=calisma_yili
        self.maas=maas

class firma:
    def __init__(self) :
        self.personel_listesi=[]

    def  personelekle(self,personel):
        self.personel_listesi.append (personel)
    
    def personellistele(self):
        for personeler in self.personel_listesi:
            print(" Ad : {} \n Soyad : {} \n Departman : {} \n calisma yili : {} \n maas : {} \n\n".format(personeler.ad , personeler.soyad , personeler.departman ,personeler.calisma_yili , personeler.maas))

    def maas_zam(self,personel,zam_orani):
        zam=(personel.maas *zam_orani)/100
        personel.maas+=zam
    def personel_cikar(self,personel):
        self.personel_listesi.remove(personel)
    

personel1 = personel("Ahmet","kum", "Muhasebe", 5, 5000)
personel2 = personel("Ayşe","kar", "İnsan Kaynakları", 3, 4500)
firma = firma()
firma.personelekle(personel1)
firma.personelekle(personel2)

firma.personellistele()
firma.maas_zam(personel2, 10)
print("Zam sonrası maaşlar:")
firma.personellistele()
firma.personel_cikar(personel2)
print("Bir personel çıkarıldı:")
firma.personellistele()