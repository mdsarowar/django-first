from django .http import HttpResponse
from django .shortcuts import render

def first(request):
    # return HttpResponse('<h1 > hello world</h1> <a href=http//facebook.com >back</a>')
     return render(request,'fir.html')

def second(request):
    tt=request.POST.get('ddd','default')
    cc=request.POST.get('pank','off')
    up=request.POST.get('uper','off')
    nl=request.POST.get('newln','off')
    # print(tt)
    # print(cc)
    fultext=''
    if(cc=='on'):
        pun='''!@#$%^&(){}[]*_+;:'"z/?><,.'''
        punction=''
        for ch in tt:
            if ch not in pun:
                punction=punction+ch

        # gg={'per':'is puncation clear','textt':punction}
        fultext=punction
        print(fultext)
        # return render(request,'se.html',gg)

    if(up=='on'):
        punction=''
        for ch in fultext:
            punction=punction+ch.upper()

        # gg = {'per': 'upper case', 'textt': punction}
        fultext = punction
        print(fultext)
        # return render(request, 'se.html', gg)

    if(nl=='on'):
        punction=''
        for ch in fultext:
            if ch !='\n' and ch !='\r':
                punction=punction+ch



        fultext = punction
        print(fultext)
    gg = {'per': 'remove new line', 'textt': fultext}


    return render(request, 'se.html', gg)


        # return render(request, 'se.html', gg)


    # else:
    #     return HttpResponse('error')


# def thired(request):
#     return HttpResponse('<h1 > hello world</h1> <a href=http//facebook.com >back</a>')
#
#
# def fourth(request):
#     return HttpResponse('<h1 > hello world</h1> <a href=http//facebook.com >back</a>')
#
#
# def fifth(request):
#     return HttpResponse('<h1 > hello world</h1> <a href=http//facebook.com >back</a>')