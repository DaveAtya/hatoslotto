from django.db import models

# Create your models here.
class Huzas(models.Model):

    id = models.IntegerField(primary_key=True)
    ev = models.IntegerField()
    het = models.IntegerField()

    def feltolt(inputcsv):
        sorok = [ sor.strip() for sor in inputcsv.strip().split('\n')]
        darab = 0

        for i, sor in enumerate(sorok[1:]):
            sortomb = sor.split('\t')

            if len(sortomb)<3:
                return (darab, f'a(z) {i+1}. rekordban kevés a tabulátorok száma!')
  
            try:
                az_id = int(sortomb[0])
            except:
                return (darab, f'a(z) {i+1}. rekordban az első mezőben nem egész szám található!')

            try:
                az_ev = int(sortomb[1])
            except:
                return (darab, f'a(z) {i+1}. rekordban a második mezőben nem egész szám található!')

            try:
                a_het = int(sortomb[2])
            except:
                return (darab, f'a(z) {i+1}. rekordban a harmadik mezőben nem egész szám található!')


            _, is_created = Huzas.objects.get_or_create(
                id = az_id,
                ev = az_ev,
                het = a_het
            )

            if  is_created:
                darab += 1

        return (darab, None)
    

    class Meta:
        verbose_name = "Húzás"
        verbose_name_plural = "Húzások"

    def __str__(self):
        return self.name
    

class Huzott(models.Model):

    id = models.IntegerField(primary_key=True)
    huzasid = models.ForeignKey(Huzas, on_delete=models.CASCADE)
    szam = models.IntegerField()

    def feltolt(inputcsv):
        sorok = [ sor.strip() for sor in inputcsv.strip().split('\n')]
        darab = 0

        for i, sor in enumerate(sorok[1:]):
            sortomb = sor.split('\t')

            if len(sortomb)<3:
                return (darab, f'a(z) {i+1}. rekordban kevés a tabulátorok száma!')
  
            try:
                az_id = int(sortomb[0])
            except:
                return (darab, f'a(z) {i+1}. rekordban az első mezőben nem egész szám található!')

            try:
                a_huzasid = int(sortomb[1])
            except:
                return (darab, f'a(z) {i+1}. rekordban a második mezőben nem egész szám található!')

            try:
                a_szam = int(sortomb[2])
            except:
                return (darab, f'a(z) {i+1}. rekordban a harmadik mezőben nem egész szám található!')


            _, is_created = Huzott.objects.get_or_create(
                id = az_id,
                huzasid = Huzas.objects.filter(id=a_huzasid).first(),
                szam = a_szam
            )

            if  is_created:
                darab += 1

        return (darab, None)
    

    class Meta:
        verbose_name = "Húzott"
        verbose_name_plural = "Húzottak"

    def __str__(self):
        return self.name



class Nyeremeny(models.Model):
    id = models.IntegerField(primary_key=True)
    huzasid = models.ForeignKey(Huzas, on_delete=models.CASCADE)
    talalat = models.IntegerField()
    darab = models.IntegerField()
    ertek = models.IntegerField()

    def feltolt(inputcsv):
        sorok = [ sor.strip() for sor in inputcsv.strip().split('\n')]
        db = 0

        for i, sor in enumerate(sorok[1:]):
            sortomb = sor.split('\t')

            if len(sortomb)<5:
                return (db, f'a(z) {i+1}. rekordban kevés a tabulátorok száma!')
  
            try:
                az_id = int(sortomb[0])
            except:
                return (db, f'a(z) {i+1}. rekordban az első mezőben nem egész szám található!')

            try:
                a_huzasid = int(sortomb[1])
            except:
                return (db, f'a(z) {i+1}. rekordban a második mezőben nem egész szám található!')

            try:
                a_talalat = int(sortomb[2])
            except:
                return (db, f'a(z) {i+1}. rekordban a harmadik mezőben nem egész szám található!')

            try:
                a_darab = int(sortomb[3])
            except:
                return (db, f'a(z) {i+1}. rekordban a negyedik mezőben nem egész szám található!')
            
            try:
                az_ertek = int(sortomb[4])
            except:
                return (db, f'a(z) {i+1}. rekordban az ötödik mezőben nem egész szám található!')
            

            _, is_created = Nyeremeny.objects.get_or_create(
                id = az_id,
                huzasid = Huzas.objects.filter(id=a_huzasid).first(),
                talalat = a_talalat,
                darab = a_darab,
                ertek = az_ertek

            )

            if  is_created:
                db += 1

        return (db, None)
    

    class Meta:
        verbose_name = "Nyeremény"
        verbose_name_plural = "Nyeremények"

    def __str__(self):
        return self.name
