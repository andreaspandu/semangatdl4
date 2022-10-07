from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('index', views.index, name = 'index'),
    path('createdata', views.createdata, name ='createdata'),
    path('tampillayanan', views.indexlayanan, name ='tampillayanan'),
    path('hapuslayanan/<str:id>', views.hapuslayanan, name="hapuslayanan"),
    path('perbaruilayanan/<str:id>', views.perbaruilayanan, name ='perbaruilayanan'),
    path('tambahlayanan', views.tambahlayanan, name ='tambahlayanan'),
    path('tambahpaket', views.tambahpaket, name ='tambahpaket'),
    path('tampilpaket', views.indexpaket, name ='tampilpaket'),
    path('hapus/<str:id>', views.hapus, name="hapus"),
    path('perbarui/<str:id>', views.perbarui, name ='perbarui'),
    path('perbaruipaket/<str:id>', views.perbaruipaket, name='perbaruipaket'),
    path('hapuspaket/<str:id>', views.hapuspaket, name='hapuspaket'),
    path('detaillayanan', views.detaillayanan, name='detaillayanan'),
    path('detaillayanan<str:id>', views.detaillayanan, name='detaillayanan'),
    path('adddetaillayanan', views.adddetaillayanan, name='adddetaillayanan'),
    path('updatedetail', views.updatedetail, name='updatedetail'),
    path('updatedetail<str:id>', views.updatedetail, name='updatedetail' ),
    path('deletedetail<str:id>', views.deletedetail, name='deletedetail')
]