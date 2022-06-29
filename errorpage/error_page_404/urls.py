
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
]
#handler404='error_page_404.views.error_404_view'