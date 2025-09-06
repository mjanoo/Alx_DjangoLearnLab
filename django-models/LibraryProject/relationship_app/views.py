from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from .models import Book, Library, UserProfile

# ----------------------------
# Book Views
# ----------------------------

def list_books(request):
    """Function-Based View: List all books"""
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# ----------------------------
# Library Views
# ----------------------------

class LibraryDetailView(DetailView):
    """Class-Based View: Show library details"""
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# ----------------------------
# Authentication Views
# ----------------------------

def register_view(request):
    """Register a new user"""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


def login_view(request):
    """Login an existing user"""
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
    """Logout the current user"""
    logout(request)
    return render(request, "relationship_app/logout.html")


# ----------------------------
# Admin-Only View
# ----------------------------

def is_admin(user):
    """Check if the user has an Admin role"""
    try:
        return user.userprofile.role == "Admin"
    except UserProfile.DoesNotExist:
        return False

@login_required
@user_passes_test(is_admin, login_url='list_books')
def admin_view(request):
    """View only accessible by Admin users"""
    return HttpResponse("Welcome Admin! This page is only for Admin users.")
