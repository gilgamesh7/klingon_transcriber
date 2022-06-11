from django.shortcuts import render

from klingon.forms import InputKlingonForm


# Create your views here.
def klingon_transcriber(request):
    input_klingon = ""

    if request.method == 'GET':
        print(request)

        input_klingon = request.GET.get('input_klingon')

        klingon_image_list = get_klingon_image_list(input_klingon)

    form = InputKlingonForm()

    context = {'form': form, 'klingon_images': klingon_image_list, 'input_klingon': input_klingon}

    return render(request, 'klingon/klingon.html', context)
    

def get_klingon_image_list(input_klingon):
    print(input_klingon)
    image_list = ['klingon/images/batleth.png']
    
    if input_klingon is not None :
        # for character in input_klingon:
        index = 0 
        while index < len(input_klingon) :
            character = input_klingon[index]

            if character == 'a':
                image_list.append('klingon/images/a.png')
            elif character == 'b':
                image_list.append('klingon/images/b.png')
            elif character == 'c':
                image_list.append('klingon/images/ch.png')
                index += 1
            elif character == 'D':
                image_list.append('klingon/images/D.png')
            elif character == 'e':
                image_list.append('klingon/images/e.png')
            elif character == 'g':
                image_list.append('klingon/images/gh.png')
                if input_klingon[index+1] == 'h' :
                    index += 1
            elif character == 'H':
                image_list.append('klingon/images/H.png')
            elif character == 'I':
                image_list.append('klingon/images/I.png')
            elif character == 'j':
                image_list.append('klingon/images/j.png')
            elif character == 'l':
                image_list.append('klingon/images/L.png')
            elif character == 'm':
                image_list.append('klingon/images/m.png')
            elif character == 'n':
                if input_klingon[index+1] == 'g' :
                    index += 1
                    image_list.append('klingon/images/ng.png')
                else :
                    image_list.append('klingon/images/n.png')
            elif character == 'o':
                image_list.append('klingon/images/o.png')
            elif character == 'p':
                image_list.append('klingon/images/p.png')
            elif character == 'q':
                image_list.append('klingon/images/q.png')
            elif character == 'Q':
                image_list.append('klingon/images/q1.png')
            elif character == 'r':
                image_list.append('klingon/images/r.png')
            elif character == 'S':
                image_list.append('klingon/images/S.png')
            elif character == 't':
                if input_klingon[index+1] == 'l' and input_klingon[index+2] == 'h':
                    image_list.append('klingon/images/tlh.png')
                    index += 2
                else :
                    image_list.append('klingon/images/t.png')
            elif character == 'u':
                image_list.append('klingon/images/u.png')
            elif character == 'v':
                image_list.append('klingon/images/v.png')
            elif character == 'w':
                image_list.append('klingon/images/w.png')
            elif character == 'y':
                image_list.append('klingon/images/y.png')
            elif character == '\'':
                image_list.append('klingon/images/qaghwI.png')
            elif character == ' ':
                image_list.append('klingon/images/space.png')

            index += 1

    image_list.append('klingon/images/batleth.png')

    print(image_list)
    return image_list
