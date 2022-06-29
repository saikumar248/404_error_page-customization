from django.shortcuts import render

# Create your views here.
def error_404_view(request,exception):
    return render(request,'404_error_page.html')
def home(request):
    return render(request,'home.html')



handler404 = 'travello.views.error_404_view'
