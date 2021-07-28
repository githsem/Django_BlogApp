from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
     return render(request, 'index.html',{'number':[1,2,3,4,5]})

def about(request):
     return render(request, 'about.html')     