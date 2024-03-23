from django.contrib import admin
from perpustakaan.models import Buku, Kumpulan

class BukuAdmin(admin.ModelAdmin):
    list_display = ['judul', 'penulis', 'kumpulan_id', 'jumlah']
    search_fields = ['judul', 'penulis', 'penerbit']
    list_filter = ['kumpulan_id',]

admin.site.register(Buku, BukuAdmin)
admin.site.register(Kumpulan)

# Register your models here.
