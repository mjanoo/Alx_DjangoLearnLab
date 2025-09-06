from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Function-Based View: list all books
    path("books/", views.list_books, name="list_books"),

    # Class-Based View: show library details
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    # User Authentication
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
]

