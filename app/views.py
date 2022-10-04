from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def perbarui(request, id):
    # pemesananobj = models.pemesanan.objects.get(idpemesanan=id)
    pemesananobj = models.pemesanan.objects.get(idpaketcpelanggan=id)
    if request.method == "GET":
        return render(request, 'perbarui.html', {
            "allpemesananobj" : pemesananobj
        })
    else:
        # allpemesananobj.idpemesanan = request.POST['idpemesanan']
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
            idlayanan = getlayanan,
            nama = nama,
            platnomor = platnomor,
            tanggalpesan = tanggalpesan
        ).save()
        return redirect ('index')