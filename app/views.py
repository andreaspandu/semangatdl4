from ast import Return
from encodings.utf_8_sig import IncrementalDecoder
from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def updatedetail(request, id):
    detail_obj = models.layanan.objects.filter(idlayanan= id)
    detail = models.detaillayanan.objects.get(idpemesanan=id)
    # dee = models.pemesanan.objects.get(idpemesanan= id)
    # detailobj = models.detaillayanan.objects.get(idlayanan_id=id)
    updatedetail_obj = models.layanan.objects.all()
    if request.method == "GET":
        return render(request, 'updatedetail.html', {
            'allupdatedetailobj' : detail_obj,
            'updatedetail' : updatedetail_obj,
            'detailobj' : detail
        } )
    else:
        # jenislayanan = request.POST['idlayanan']
        detail.idlayanan.jenislayanan = request.POST['idlayanan']
        detail.save()
        # getlayanan = models.layanan.objects.get(idlayanan = jenislayanan)
        # # newdeta = models.detaillayanan(
        # #     idlayanan = getlayanan ).save()
        # detail.idlayanan.save()
        return redirect ('index')

def deletedetail(request, id):
    detaillayananobj = models.layanan.objects.get(idlayanan = id)
    detaillayananobj.delete()
    return redirect('index')

def perbaruilayanan(request, id):
    layananobj = models.layanan.objects.get(idlayanan = id)
    layanan_obj = models.layanan.objects.all()
    if request.method == "GET":
        return render(request, 'perbaruilayanan.html', {
            'alllayananobj' : layananobj,
            'layananobj' : layanan_obj
        })
    else:
        # idlayanan = request.POST['idlayanan']
        # getlayanan = models.layanan.objects.get(idlayanan = idlayanan)
        layananobj.jenislayanan = request.POST['jenislayanan']
        layananobj.harga = request.POST['harga']
        layananobj.save()
        return redirect ('tampillayanan')

def adddetaillayanan(request):
    detaillayananobj = models.layanan.objects.all()
    pemesananobj = models.pemesanan.objects.all()
    if request.method == "GET":
        return render(request, 'adddetaillayanan.html', {
            'detail' : detaillayananobj,  
            'pemesanan' : pemesananobj
        })
    else:
        idpemesanan = request.POST['idpemesanan']
        jenislayanan = request.POST['idlayanan']
        getlayanan = models.layanan.objects.get(idlayanan = jenislayanan)
        getpemesanan = models.pemesanan.objects.get(idpemesanan = idpemesanan)
        # getid = models.detaillayanan.objects.get(idlayanan = idlayanan)
        # pemesanan_obj =  models.pemesanan.objects.all().last()
        newdetail = models.detaillayanan(
            idpemesanan = getpemesanan,
            idlayanan = getlayanan
        ).save()
            
        return redirect ('index')
        
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

def hapuspaket(request, id):
    paketlayananobj = models.paketlayanan.objects.get(idpaketlayanan = id)
    paketlayananobj.delete()
    return redirect('tampilpaket')

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
    data=[]
    allpemesananobj = models.pemesanan.objects.all()
    for item in allpemesananobj:
        dummy = []
        # print(item,'woy')
        id_pemesanan = item.idpemesanan
        specificdetail = models.detaillayanan.objects.filter(idpemesanan= id_pemesanan)
        dummy.append(item)
        dummy.append(specificdetail)
        data.append(dummy)
    return render (request, 'pemesanan.html', {
        'pemesanan' : data
    })

def detaillayanan(request,id):
    detaillayananobj = models.detaillayanan.objects.filter(idpemesanan = id)
    alldetaillayananobj = models.detaillayanan.objects.all()
    return render(request, 'detaillayanan.html', {
        'alldetaillayananobj' : detaillayananobj,
        'detail_layanan' : detaillayananobj
    })

def indexpaket(request):
    allpaketlayananobj = models.paketlayanan.objects.all()

    return render(request, 'tampilpaket.html', {
        'allpaketlayananobj' : allpaketlayananobj
    })
def tambahlayanan(request):
    tambahlayanan = models.layanan.objects.all()
    if request.method == "GET":
        return render(request, 'tambahlayanan.html', {
        })
    else:
        jenislayanan = request.POST['jenislayanan']
        harga = request.POST['harga']

        newlayanan = models.layanan(
            jenislayanan = jenislayanan,
            harga = harga
        ).save()
        return redirect('tampillayanan')
def perbaruipaket(request, id):
    paketlayananobj = models.paketlayanan.objects.get(idpaketlayanan=id)
    paket_obj = models.paketlayanan.objects.all()
    if request.method == "GET":
        return render(request, 'perbaruipaket.html', {
            "allpaketlayananobj" : paketlayananobj,
            'idpaketlayanan' : paket_obj
        })
    else:
        # allpemesananobj.idpemesanan = request.POST['idpemesanan']
        # idpaketlayanan = request.POST['idpaketlayanan']
        # getpaketbaru = models.paketlayanan.objects.get(idpaketlayanan= idpaketlayanan)
        # pemesananobj.idpaketpelanggan = getpaketbaru
        # paketlayananobj.idpaketlayanan = request.POST['idpaketlayanan']
        paketlayananobj.jenispaket = request.POST['jenispaket']
        paketlayananobj.keteranganpaket = request.POST['keteranganpaket']
        paketlayananobj.harga = request.POST['harga']
        paketlayananobj.save()
        return redirect ('tampilpaket')

def tambahpaket(request):
    tambahpaket = models.paketlayanan.objects.all()
    if request.method == "GET":
        return render(request, 'tambahpaket.html', {
        })
    else:
        jenispaket = request.POST['jenispaket']
        keteranganpaket = request.POST['keteranganpaket']
        harga = request.POST['harga']

        newpaket = models.paketlayanan(
            jenispaket = jenispaket,
            keteranganpaket = keteranganpaket,
            harga = harga
        ).save()
        return redirect('tampilpaket')

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
        harga = request.POST['harga']
        jenislayanan = request.POST['jenislayanan']


        newlayanan = models.detaillayanan(
            idlayanan = getlayanan,
            harga = harga,
            jenislayanan = jenislayanan
        ).save()
        return redirect ('index')
# bikinlayanan masih bingung di idlayanan pas input itu masukin idnya ngambil dari mana, bikin baru kah atau gimana kah