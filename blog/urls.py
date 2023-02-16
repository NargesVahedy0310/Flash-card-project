from django.urls import path
from .views import BlogMe
urlpatterns = [
    path('viewBlog/', BlogMe.as_view())
    ]