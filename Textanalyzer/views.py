from django.shortcuts import render,HttpResponse

def index(request):
    return render(request,'index.html')

def ex1(request):
    s='''<h1>Navigation Bar</h1><br>
    <table border='1'>
    <tr><td><a href="https://www.google.com/">Google link</a></td></tr>
    <tr><td><a href="https://www.codewithharry.com/">Code With Harry link</a></td></tr>
    <tr><td><a href="https://www.facebook.com/">Face book link</a></td></tr>
    <tr><td><a href="https://www.youtube.com/">Youtube link</a></td></tr>
    
    </table border>
    
    '''
    return HttpResponse(s)

def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    #Checkbox Vlaue
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extrespaceremover=request.GET.get('extrespaceremover','off')
    charactercounter=request.GET.get('charactercounter','off')


    #Check whis Checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Changed to UPPERCASE ', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n":
                analyzed=analyzed+char.strip()
        params = {'purpose': 'Removed Newline ', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(extrespaceremover=="on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        params = {'purpose': 'Removed Extra Spaces ', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(charactercounter=="on"):
        analyzed=""
        for char in djtext:
                count=0
                analyzed=analyzed+char.count()
                
        if djtext=="":
            count=0
            print("null")
        params = {'purpose': 'Removed Extra Spaces ', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error')

def removepunc(request):
     djtext = request.GET.get('text', 'default')
    #Checkbox Vlaue
     removepunc=request.GET.get('removepunc','off')
     return render(request,'removepunc.html')

    

