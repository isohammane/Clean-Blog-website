from django.urls import path
from .views import Home ,Contact ,About ,Post

urlpatterns = [
    path("",Home ,name="homepage"),
    path("about/",About,name="aboutpage"),
    path("contact-me/",Contact ,name="contactpage"),
    path("post/<int:id>/",Post,name="postpage"),
]
