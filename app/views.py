from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def perbarui(request, id):
    pemesananobj = models.pemesanan.objects.get(idpemesanan=id)
    if request.method == "GET":
        return render(request, 'perbarui.html', {
            "allpemesananobj" : pemesananobj
        })
    else:
        pemesananobj.idpemesanan = request.POST['idpemesanan']
        pemesananobj.idpaketpelanggan = request.POST['idpaketpelanggan']
        pemesananobj.nama = request.POST['nama']
        pemesananobj.platnomor = request.POST['platnomor']
        pemesananobj.tanggalpesan = request.POST['tanggalpesan']
        pemesananobj.save()
        return redirect ('index')

def hapus(request, id):
    pemesananobj = models.pemesanan.objects.get(idpemesanan = id)
    pemesananobj.delete()   
    return redirect('index') 

def index(request):
    allpemesananobj = models.pemesanan.objects.all()
    getpemesananobj = models.pemesanan.objects.get(idpemesanan = 1)
    filterpemesananobj = models.pemesanan.objects.filter(tanggalpesan = "2022-01-01")
   
    return render (request, 'pemesanan.html', {
        'allpemesananobj' : allpemesananobj,
        'getpemesananobj' : getpemesananobj,
        'filterpemesananobj' : filterpemesananobj
    })

def createdata (request):
    if request.method == "GET":
        paket = models.paketlayanan.objects.all()
        return render (request, 'createdata.html',{
            'pakettersedia' : paket

        })
    else:
        # idpemesanan = request.POST['idpemesanan']
        idpaketpelanggan = request.POST['idpaketpelanggan']
        nama = request.POST['nama']
        platnomor = request.POST ['platnomor']
        tanggalpesan = request.POST ['tanggalpesan']
        # paketobj = models.paketlayanan.objects.get(idpaketpelanggan = models.paketlayanan)

        newpemesanan = models.pemesanan(
            # idpemesanan = idpemesanan,
            idpaketlayanan = idpaketpelanggan,
            nama = nama,
            platnomor = platnomor,
            tanggalpesan = tanggalpesan
        ).save()
        return redirect ('index')