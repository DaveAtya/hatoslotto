from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('feltolt/huzas/', feltolt),
    path('feltolt/huzott/', feltolt),
    path('feltolt/nyeremeny/', feltolt),
    path('feltolt/huzas/post/', feltolt_huzas),
    path('feltolt/huzott/post/', feltolt_huzott),
    path('feltolt/nyeremeny/post/', feltolt_nyeremeny),
    path('feladat2', feladat2),
    path('feladat3', feladat3),
    path('feladat4', feladat4),
    path('feladat5', feladat5),
    path('feladat6', feladat6),
]