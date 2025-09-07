from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Function-Based View: list all books
    path("books/", views.list_books, name="list_books"),

    # Class-Based View: show library details
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    # User Authentication
    path("register/", views.register_view, name="register"),  # <-- updated here
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),

    # Admin-only view
    path("admin-view/", views.admin_view, name="admin_view"),
    path("admin-view/", views.admin_view, name="admin_view"),
path("librarian-view/", views.librarian_view, name="librarian_view"),
path("member-view/", views.member_view, name="member_view"),

]
