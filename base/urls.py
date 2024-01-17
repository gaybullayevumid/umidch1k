from django.urls import path
from .views import HomePageView


urlpatterns = [
    # path('about/', AboutPageView.as_view(), name='about'),
    # path('service/', ServicePageView.as_view(), name='service'),
    path('', HomePageView.as_view(), name='home'),
]