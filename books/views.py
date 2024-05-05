from django.shortcuts import render,redirect
# Create your views here.

books = [
    {
        "id": 1,
        "title": "Book Title",
        "author": "Book Author",
        "image": "https://placehold.co/300x150",
        "rating": 4.5,
        "views": 100,
        "description": "A brief description of the book.",
    },
    {
        "id": 2,
        "title": "Book Title",
        "author": "Book Author",
        "image": "https://placehold.co/300x150",
        "rating": 4.5,
        "views": 100,
        "description": "A brief description of the book.",
    },
    {
        "id": 3,
        "title": "Book Title",
        "author": "Book Author",
        "image": "https://placehold.co/300x150",
        "rating": 4.5,
        "views": 100,
        "description": "A brief description of the book.",
    },
]


def index(request):
    context = {"books": books, "title": "Home"}
    print("len", len(books))
    return render(request, "books/index.html", context)

def add(request):
    if request.method == "POST":
        books.append({
            "id": len(books) + 1,
            "title": request.POST.get("title"),
            "author": request.POST.get("author"),
            "image": request.POST.get("image"),
            "rating": request.POST.get("rating"),
            "views": request.POST.get("views"),
            "description": request.POST.get("description"),
        })
        print("books", books)
        return redirect("/")
    else:
        return render(request, "books/add.html", {"title": "Add New Book"})

def detail(request, id):
    context = {"book": books[id - 1], "title": "Book - " + str(id)}
    print(context["book"])
    return render(request, "books/detail.html", context)

def edit(request, id):
    if request.method == "POST":
        books[id - 1]["title"] = request.POST.get("title")
        books[id - 1]["author"] = request.POST.get("author")
        books[id - 1]["image"] = request.POST.get("image")
        books[id - 1]["rating"] = request.POST.get("rating")
        books[id - 1]["views"] = request.POST.get("views")
        books[id - 1]["description"] = request.POST.get("description")
        print("books", books)
        return redirect("/")
    else:
        context = {"book": books[id - 1], "title": "Edit Book - " + str(id)}
        return render(request, "books/edit.html", context)

def delete(request, id):
    books.pop(id - 1)
    return redirect("/")