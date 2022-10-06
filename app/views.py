from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def perbaruilayanan(request, id):
    layanan = models.layanan.objects.all()
    layananobj = models.layanan.objects.get(idlayanan = id)
    if request.method == "GET":
        return render(request, 'tampillayanan.html', {
            'alllayanan' : layanan,
            'layananobj' : layananobj
        })
    else:
        idlayanan = request.POST['idlayanan']
        getlayanan = models.layanan.objects.get(idlayanan = idlayanan)
        layananobj.harga = request.POST['harga']

def perbarui(request, id):  
    pemesananobj = models.pemesanan.objects.get(idpemesanan=id)
    paket_obj = models.paketlayanan.objects.all()
    if request.method == "GET":
        return render(request, 'perbarui.html', {
            "allpemesananobj" : pemesananobj,
            'paket' : paket_obj
        })
    else:
        # allpemesananobj.idpemesanan = request.POST['idpemesanan']
        idpaketlayanan = request.POST['idpaketpelanggan']
        getpaketbaru = models.paketlayanan.objects.get(idpaketlayanan= idpaketlayanan)
        pemesananobj.idpaketpelanggan = getpaketbaru
        pemesananobj.nama = request.POST['nama']
        pemesananobj.platnomor = request.POST['platnomor']
        pemesananobj.tanggalpesan = request.POST['tanggalpesan']
        pemesananobj.save()
        return redirect ('index')

def hapus(request, id):
    pemesananobj = models.pemesanan.objects.get(idpemesanan = id)
    pemesananobj.delete()   
    return redirect('index') 

def hapuslayanan(request, id):
    layananobj = models.layanan.objects.get(idlayanan = id)
    layananobj.delete()   
    return redirect('tampillayanan') 

def indexlayanan(request):
    alllayananobj = models.layanan.objects.all()

    return render(request, 'tampillayanan.html', {
        'alllayananobj' : alllayananobj
    })

def index(request):
    allpemesananobj = models.pemesanan.objects.all()
   
    return render (request, 'pemesanan.html', {
        'allpemesananobj' : allpemesananobj
    })

def createdata (request):
    paket = models.paketlayanan.objects.all()
    layanan = models.layanan.objects.all()
    if request.method == "GET":
        return render (request, 'createdata.html',{
            'pakettersedia' : paket,
            'layanantersedia' : layanan
        })
    else:
        # idpemesanan = request.POST['idpemesanan']
        idpaketpelanggan = request.POST['idpaketpelanggan']
        getpaketbaru = models.paketlayanan.objects.get(idpaketlayanan = idpaketpelanggan) #harus di get dulu baru bisa. karena dari html pas ngepost itu hasilnya cuma string. misal kalian di html pilih paket 1. itu datanya yang kekirim cuma "1". jadi harus diget dulu, jadiin si "1" itu sebagai parameter.
        idlayanan = request.POST['idlayanan']
        getlayanan = models.layanan.objects.get(idlayanan = idlayanan)
        nama = request.POST['nama']
        platnomor = request.POST ['platnomor']
        tanggalpesan = request.POST ['tanggalpesan']
        # paketobj = models.paketlayanan.objects.get(idpaketpelanggan = models.paketlayanan)

        newpemesanan = models.pemesanan(
            # idpemesanan = idpemesanan,
            idpaketpelanggan = getpaketbaru, #harusnya idpaketpelanggan, bukan idpaketlayanan. soalnya di models itu id paket pelanggan. Kalau namain variabel gausa ribet biar ga salah
            nama = nama,
            platnomor = platnomor,
            tanggalpesan = tanggalpesan
        ).save()
        
        pemesanan_obj =  models.pemesanan.objects.all().last()
        newlayanan = models.detaillayanan(
            idpemesanan = pemesanan_obj,
            idlayanan = getlayanan,
        ).save()
        return redirect ('index')

def bikinlayanan(request):
    layanan = models.layanan.objects.all()
    if request.method == "GET":
        return render (request, 'bikinlayanan.html',{
            'layanantersedia' : layanan
        })
    else:
        idlayanan = request.POST['idlayanan']
        getlayanan = models.layanan.objects.get(idlayanan = idlayanan)
        layanan.harga = request.POST['harga']

        newlayanan = models.detaillayanan(
            idlayanan = getlayanan,
        ).save()
        return redirect ('index')

def bikinpaket(request):
    paket = models.paketlayanan.objects.all()
    if request.method == "GET":
        return render (request, 'bikinpaket.html',{
            'pakettersedia' : paket,
        })
