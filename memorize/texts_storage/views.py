from django.shortcuts import render, redirect
from .models import Texts
from .forms import Newtext

def new_text(request): 
    last_text = Texts.objects.filter(user = request.user).last()
    if last_text:last_text = last_text.title
    
    if request.method == 'POST':
        form = Newtext(request.POST)
        text = request.FILES.get('text')

        if form.is_valid():          
            Texts(user = request.user, text = text, title = request.POST['title'] ).save()
            return redirect('add')   
    else:
        form = Newtext()
    
    context = {'form' : form,
               'last_text': last_text
               }
    return render(request, 'new_text.html', context)

def listof_texts(request): 
    if request.method == 'GET':
        
        title = request.GET.get('delete')
        if title:
            Texts.objects.get(title = title).text.delete(save=True)
            Texts.objects.get(title = title).delete()

    titles = []
    for i in Texts.objects.filter(user = request.user):
        titles += [i.title]

    context = {'titles' : titles
               }
    return render(request, 'list.html', context)

def read_text(request): 
    if request.method == 'GET':
        title = request.GET.get('title')
        
        if title:
            dir = Texts.objects.get(title = title).text.file
            text = ''
            with open(str(dir),'r') as file:
                text = file.read()
                
                    
                    

            
        else: text = 'Что-то пошло не так.'
    

    context = {'text' : text,
               'title': title,
               }
               
    return render(request, 'read.html', context)

