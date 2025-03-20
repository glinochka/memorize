from django.shortcuts import render, redirect
from .models import Articles
from .forms import NewArticle
from .utils import savy_html

def new_article(request): 
    last_article = Articles.objects.filter(user = request.user).last()
    if last_article:last_article = last_article.title
    
    if request.method == 'POST':
        form = NewArticle(request.POST,request.FILES)

        if form.is_valid():
            article = request.FILES.get('article')     
            Articles(user = request.user, article = article, title = request.POST['title'] ).save()

            savy_html(str(Articles.objects.get(title = request.POST['title']).article)) 

            return redirect('add')   
    else:
        form = NewArticle()
    
    context = {'form' : form,
               'last_article': last_article
               }
    return render(request, 'new_article.html', context)

def listof_articles(request):
    del_mes = '' 
    if request.method == 'GET':
        
        title = request.GET.get('delete')
        if title:
            try: 
                Articles.objects.get(title = title).article.delete(save=True)
                Articles.objects.get(title = title).delete()
            except WindowsError:
                del_mes = 'Упс не получилось удалить статью, попробуйте позже.'
            

    titles = []
    for i in Articles.objects.filter(user = request.user):
        titles += [i.title]

    context = {'titles' : titles,
               'del_mes': del_mes
               }
    return render(request, 'list.html', context)

def read_article(request): 
    if request.method == 'GET':
        title = request.GET.get('title')
        
        if title:
            dir = Articles.objects.get(title = title).article.file
            file_name = dir.name.split('/')[-1].split('\\')[-1]
            return render(request, f'{request.user.username}/{file_name}', {'title':title})
             
        else:
            text = 'Что-то пошло не так.'
            return render(request, f'read.html', {'text': text, 'title': title})
    
               
    

