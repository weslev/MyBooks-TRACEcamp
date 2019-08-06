from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
import requests 
from bookinfo.models import BookModel
import json

# Create your views here.

# Homepage
class HomeView(TemplateView):
    template_name = ('homepage.html')

# Search page
class SearchView(TemplateView):
    template_name = ('searchpage.html')

# Sends the books to the list page to be displayed
def book_list(request):
    books = BookModel.objects.all()
    context = {
        'books':books
    }
    return render(request, 'list.html', context = context)

# Adds the user's desired book and comment to the list
def add_book(request):
    if request.method == 'POST':
        print(request.POST.get('author'))
        book = BookModel(
            author = request.POST.get('author'),
            title = request.POST.get('title'),
            ISBN = request.POST.get('ISBN'),
            cover = request.POST.get('cover'),
            comment = request.POST.get('comment')
        )
        book.save()
        return HttpResponseRedirect('/bookinfo/list')
    
# Finds a book's details by ISBN with the OpenLibrary API
def book_search(request):
    #book 0670034851
    if request.method == 'GET':
        key = request.GET.get('ISBN', "NOT FOUND")
        url = ("https://openlibrary.org/api/books?bibkeys=ISBN:" + key + "&jscmd=details&format=json")
        urlPhoto = "http://covers.openlibrary.org/b/isbn/" + key + "-L.jpg"
        keyISBN = ("ISBN:" + key)
        bookinfo = requests.get(url).json()

        author = bookinfo[keyISBN]['details']['authors'][0]['name']
        title = bookinfo[keyISBN]['details']['title']

        context = {
            "ISBN": key,
            "author": author,
            "title": title,
            "cover": urlPhoto,
        }
    return render(request, 'result.html', context = context)