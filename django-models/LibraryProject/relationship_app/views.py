from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Book, Library, UserProfile
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# ----------------------------
# Book Views
# ----------------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# ----------------------------
# Library Views
# ----------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# ----------------------------
# Authentication Views
# ----------------------------
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, "relationship_app/list_books.html")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request, "relationship_app/list_books.html")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")


# ----------------------------
# Role Checks
# ----------------------------
def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"

def is_librarian(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Librarian"

def is_member(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Member"


# ----------------------------
# Role-Based Views
# ----------------------------
@login_required
@user_passes_test(is_admin, login_url="login")
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


@login_required
@user_passes_test(is_librarian, login_url="login")
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


@login_required
@user_passes_test(is_member, login_url="login")
def member_view(request):
    return render(request, "relationship_app/member_view.html")
