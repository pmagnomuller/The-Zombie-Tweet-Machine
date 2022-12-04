from django.urls import path

from . import views

urlpatterns = [
    path(
        "", views.HomeView.as_view(), name="home"
    ),
    path("create-tweet/", views.TextBlockCreateView.as_view(), name="create-tweet"
    ),

]