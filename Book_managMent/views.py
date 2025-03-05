from django.shortcuts import render ,redirect,HttpResponse
from demo.models import Demo,Book


def book(request): 
    
    if request.method == 'POST':
        title=request.POST.get('title')
        author=request.POST.get('author')
        desc=request.POST.get('desc')
        puby=request.POST.get('puby')

        book=Book(title=title,author=author,description=desc,published_year=puby)
        book.save()
        return redirect('book')
        
    book_list=Book.objects.all()
    return render(request, 'book.html',{'book_list':book_list})
def register(request):
    if request.method == 'POST':
        f_name=request.POST.get('fname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if pass1==pass2:
            demo=Demo(ful_name=f_name,email=email,password=pass1,confirm_password=pass2)
            demo.save()
            return redirect('book')
    return render(request,'register.html')

def delete(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect('book')

def update(request,id):
    book=Book.objects.all()
    if request.method == 'POST':
        title=request.POST.get,id('title')
        author=request.POST.get('author')
        desc=request.POST.get('desc')
        puby=request.POST.get('puby')

        book.title=title
        book.author=author
        book.description=desc
        book.published_year=puby
        book.save()
        return redirect('book')
    return render(request,'update.html',{'book':book})
   