from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('index', views.index, name = 'index'),
    path('createdata', views.createdata, name ='createdata'),
    path('tampillayanan', views.indexlayanan, name ='tampillayanan'),
    path('bikinpaket', views.bikinpaket, name ='bikinpaket'),
    path('hapus/<str:id>', views.hapuslayanan, name="hapuslayanan"),
    path('hapus/<str:id>', views.hapus, name="hapus"),
    path('perbarui/<str:id>', views.perbarui, name ='perbarui'),
    path('perbaruilayanan/<str:id>', views.perbaruilayanan, name ='perbaruilayanan')
]   