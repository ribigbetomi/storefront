from django.urls import path
from . import views

# so url with playround/hello will route to this first endpoint as initial playground/ is already set in urls.py file in storefront folder
# URLConfiguration
urlpatterns = [
    path('hello/', views.say_hello)
]
