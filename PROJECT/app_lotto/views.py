from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound, HttpResponseServerError, HttpResponseBadRequest, HttpResponseNotAllowed
from django.db.models import Sum, Count, Min

# Create your views here.
def index(request):
    context = {}
    template = "index.html"
    return render(request, template, context)

def feltolt(request):
    template = "feltolt.html"
    context = {}
    return render(request, template, context)

def feltolt_huzas(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed('Nem gombra nyomva jutottál ide!')
    
    darab, error = Huzas.feltolt(request.POST['inputcsv'])

    if error != None:
        return HttpResponseServerError(f'Hát sikerült {darab} db rekordot felvinni, aztán történt egy kis probléma... '+ error)

    return HttpResponse(f'Sikerült!! {darab} db új elem jött létre az adatbázisban, így most összesen {Huzas.objects.all().count()} db rekord van az adatbázisban.')


def feltolt_huzott(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed('Nem gombra nyomva jutottál ide!')
    
    darab, error = Huzott.feltolt(request.POST['inputcsv'])

    if error != None:
        return HttpResponseServerError(f'Hát sikerült {darab} db rekordot felvinni, aztán történt egy kis probléma... '+ error)

    return HttpResponse(f'Sikerült!! {darab} db új elem jött létre az adatbázisban, így most összesen {Huzott.objects.all().count()} db rekord van az adatbázisban.')

def feltolt_nyeremeny(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed('Nem gombra nyomva jutottál ide!')
    
    darab, error = Nyeremeny.feltolt(request.POST['inputcsv'])

    if error != None:
        return HttpResponseServerError(f'Hát sikerült {darab} db rekordot felvinni, aztán történt egy kis probléma... '+ error)

    return HttpResponse(f'Sikerült!! {darab} db új elem jött létre az adatbázisban, így most összesen {Nyeremeny.objects.all().count()} db rekord van az adatbázisban.')

def feladat2(request):
    return render(request, "feladat2.html", {"huzasok":Huzas.objects.filter(ev__lt=2001, nyeremeny__talalat=6).order_by("ev","het")})

def feladat3(request):
    return render(request, "feladat3.html", {"adatok":Nyeremeny.objects.order_by("huzasid__het", "-talalat").values("huzasid__het", "talalat").annotate(szelvenyszam = Count("id"), osszeg = Sum("ertek"))})

def feladat4(request):
    adat = Huzas.objects.order_by("ev").values("ev").annotate(darab=Count("id")).filter(darab=52).first()
    return render(request, "feladat4.html", {"adat":adat})

def feladat5(request):
    return render(request, "feladat5.html", {"huzasok":[huzas for huzas in Huzas.objects.order_by("ev","het") if huzas.huzott_set.filter(szam=1).exists() and huzas.huzott_set.filter(szam=6).exists()]})

def feladat6(request):
    return render(request, "feladat6.html", {"adatok":Huzas.objects.filter(ev__range=(2001, 2010)).order_by("ev").values("ev").annotate(osszeg=Sum("nyeremeny__ertek"))})