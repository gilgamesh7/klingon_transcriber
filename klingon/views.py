from django.shortcuts import render


# Create your views here.
def klingon_transcriber(request):
    return render(request, 'klingon/klingon.html')
