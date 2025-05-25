import requests
from django.shortcuts import render, redirect
from .forms import ProjekForm
from .models import ProjekModels

PROJECT_API_URL = 'http://127.0.0.1/api/projek/fetch/'

def projek_list(request):
    projeks = ProjekModels.objects.all()
    return render(request, 'projek/projek_list.html', {'projeks': projeks})

def projek_create(request):
    if request.method == 'POST':
        form = ProjekForm(request.POST)
        if form.is_valid():
            projek = form.save()

            try:
                data = {
                    'nama_projek': projek.nama_projek,
                    'deskripsi': projek.deskripsi,
                    'tanggal_mulai': projek.tanggal_mulai.isoformat(),
                    'tanggal_selesai': projek.tanggal_selesai.isoformat(),
                    'supervisor': projek.supervisor,
                    'status_projek': projek.status_projek,
                }
                requests.post(PROJECT_API_URL, json=data)
            except Exception as e:
                print("Failed to auto-sync:", e)

            return redirect('projek_list')
    else:
        form = ProjekForm()
    return render(request, 'projek/projek_form.html', {'form': form})


def projek_update(request, pk):
    projek = ProjekModels.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProjekForm(request.POST, instance=projek)
        if form.is_valid():
            form.save()
            return redirect('projek_list')
    else:
        form = ProjekForm(instance=projek)
    return render(request, 'projek/projek_form.html', {'form': form})

def projek_delete(request, pk):
    projek = ProjekModels.objects.get(pk=pk)
    if request.method == 'POST':
        projek.delete()
        return redirect('projek_list')
    return render(request, 'projek/projek_confirm_delete.html', {'projek': projek})

