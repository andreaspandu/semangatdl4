from django.db import models

# Create your models here.
class paketlayanan(models.Model):
    idpaketlayanan = models.AutoField(primary_key=True)
    jenispaket = models.CharField(max_length=10)
    keteranganpaket = models.CharField(max_length=50)
    harga = models.IntegerField()

    def __str__(self):
        return str(self.idpaketlayanan)

class layanan(models.Model):
    idlayanan = models.AutoField(primary_key=True)
    jenislayanan = models.CharField(max_length=10)
    harga = models.IntegerField()

    def __str__(self):
        return str(self.jenislayanan)

class pemesanan(models.Model):  
    idpemesanan = models.AutoField(primary_key=True)
    idpaketpelanggan = models.ForeignKey(paketlayanan,on_delete=models.CASCADE)
    nama = models.CharField(max_length=50)
    platnomor = models.CharField(max_length=11)
    tanggalpesan = models.DateField()

    def __str__(self):
        return str(self.idpemesanan)

class detaillayanan(models.Model):
    iddetaillayanan = models.AutoField(primary_key=True)
    idlayanan = models.ForeignKey(layanan,on_delete=models.CASCADE)
    idpemesanan = models.ForeignKey(pemesanan,on_delete=models.CASCADE)
    

    def __str__(self):
        return str(self.idpemesanan)