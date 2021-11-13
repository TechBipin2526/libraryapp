from django.shortcuts import render, redirect
from .models import Book
from .forms import BookCreate
from django.http import HttpResponse

# Create your views here.

def index(request):
    shelf = Book.objects.all()
    return render(request, 'app/library.html', {'shelf': shelf})

def upload(request):
    upload = BookCreate()
    if request.method == "POST":
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid:
            upload.save()
            return redirect('/')
        else:
            return HttpResponse("""Wrong Form, reload on <a href="{{url: 'index'}}">Reload</a>""")
    else:
        return render(request, 'app/upload_form.html', {'upload_form': upload})
    
def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('/index')
    book_form = BookCreate(request.POST or None, instance=book_sel)
    if book_form.is_valid:
        book_form.save()
        return redirect('/index')
    return render(request, 'app/upload_form.html', {'upload_from': book_form})

def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('/index')
    book_sel.delete()
    return redirect('/')
        