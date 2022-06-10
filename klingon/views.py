from django.shortcuts import render


# Create your views here.
def klingon_transcriber(request):

    image_list = ['klingon/images/a.png', 'klingon/images/b.png', 'klingon/images/ch.png']

    form_display = {'images': image_list}
    
    return render(request, 'klingon/klingon.html', form_display)
