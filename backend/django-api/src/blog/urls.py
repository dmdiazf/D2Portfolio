from django.urls import path
from blog.views import HelloWorld

urlpatterns = [
    path('', HelloWorld.as_view()),
]