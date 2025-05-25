from django.db import models

# Create your models here.
class ProjekModels(models.Model):

    STATUS_PROJEK = [
        ('berlangsung', 'Berlangsung'),
        ('selesai', 'Selesai'),
        ('gagal', 'Gagal'),
    ]

    nama_projek = models.CharField(max_length=255)
    deskripsi = models.TextField(blank=True)
    lokasi = models.CharField(max_length=255, blank=True)
    tanggal_mulai = models.DateField()
    tanggal_selesai = models.DateField()
    supervisor = models.CharField(max_length=255)
    status_projek = models.CharField(
        max_length=20,
        choices=STATUS_PROJEK,
        default='berlangsung',
        verbose_name='Status Projek'
    )