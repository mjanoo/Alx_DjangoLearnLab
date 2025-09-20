"""
URL configuration for LibraryProject project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookshelf.urls')),  # if bookshelf has urls.py
    path('accounts/', include('accounts.urls')),  # if accounts has urls.py
]