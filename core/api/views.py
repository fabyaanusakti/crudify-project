import requests
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjekSerializer
from core.models import ProjekModels

PROJECT_API_URL = 'http://127.0.0.1:8001/projek/'

@api_view(['GET'])
def projek_api_list(request):
    projeks = ProjekModels.objects.all()
    serializer = ProjekSerializer(projeks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def projek_api_create(request):
    serializer = ProjekSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 'success', 'data': serializer.data})
    return Response(serializer.errors, status=400)

def projek_api_send(request, pk):
    projek = get_object_or_404(ProjekModels, pk=pk)

    data = {
        'nama_projek': projek.nama_projek,
        'deskripsi': projek.deskripsi,
        'lokasi': projek.lokasi,
        'tanggal_mulai': projek.tanggal_mulai.isoformat(),
        'tanggal_selesai': projek.tanggal_selesai.isoformat(),
        'supervisor': projek.supervisor,
        'status_projek': projek.status_projek,
    }

    try:
        response = requests.post(PROJECT_API_URL, json=data)
        if response.status_code == 200:
            messages.success(request, 'Data berhasil dikirim ke Project B!')
        else:
            messages.error(request, 'Gagal mengirim data.')
    except Exception as e:
        messages.error(request, f'Error: {e}')

    return redirect('projek_list')

