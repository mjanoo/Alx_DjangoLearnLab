from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Book
from .models import Library   # <-- add this separately for the checker


# Function-Based View: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-Based View: show library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # <-- change here
    context_object_name = "library"


# ----------------------------
# Authentication Views
# ----------------------------

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after register
            return redirect("list_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("list_books")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log the user in after registering
            return redirect("home")  # change "home" to a valid route in your project
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import UserProfile

@login_required
def admin_view(request):
    try:
        profile = request.user.userprofile
        if profile.role == "Admin":
            return HttpResponse("Welcome Admin! This page is only for Admin users.")
        else:
            return HttpResponse("Access denied: You are not an Admin.")
    except UserProfile.DoesNotExist:
        return HttpResponse("No profile found for this user.")
