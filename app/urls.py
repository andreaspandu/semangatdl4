from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('index', views.index, name = 'index'),
    path('createdata', views.createdata, name ='createdata'),
    path('tampillayanan', views.indexlayanan, name ='tampillayanan'),
    path('hapuslayanan/<str:id>', views.hapuslayanan, name="hapuslayanan"),
    path('perbaruilayanan/<str:id>', views.perbaruilayanan, name ='perbaruilayanan'),
    path('bikinlayanan', views.bikinlayanan, name ='bikinlayanan'),
    path('bikinpaket', views.indexpaket, name ='bikinpaket'),
    path('hapus/<str:id>', views.hapus, name="hapus"),
    path('perbarui/<str:id>', views.perbarui, name ='perbarui'),
    path('perbaruipaket/<str:id>', views.perbaruipaket, name='perbaruipaket'),
    path('hapuspaket/<str:id>', views.hapuspaket, name='hapuspaket')
]   