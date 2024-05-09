from django.shortcuts import render,redirect
from .models import Book

def index(request):
    context = {"books": Book.objects.all(), "title": "Home"}
    print("len", context.get("books").count())
    return render(request, "books/index.html", context)

def add(request):
    if request.method == "POST":
        book = Book.objects.create(
            title=request.POST.get("title"),
            author=request.POST.get("author"),
            image=request.POST.get("image"),
            rating=request.POST.get("rating"),
            views=request.POST.get("views"),
            description=request.POST.get("description"),
        )
        book.save()
        print("book", book)
        return redirect("/")
    else:
        return render(request, "books/add.html", {"title": "Add New Book"})

def detail(request, id):
    book = Book.objects.get(id=id)
    context = {"book": book}
    print(context["book"])
    return render(request, "books/detail.html", context)

def edit(request, id):
    book=Book.objects.get(id=id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.image = request.POST.get("image")
        book.rating = request.POST.get("rating")
        book.views = request.POST.get("views")
        book.description = request.POST.get("description")
        book.save()
        print("book", book.rating)
        return redirect("/")
    else:
        context = {"book": book, "title": "Edit Book - " + str(id)}
        return render(request, "books/edit.html", context)

def delete(request, id):
    Book.objects.get(id=id).delete()
    return redirect("/")