from multiprocessing import context
from django.shortcuts import render



# Create your views here.
def index(request):
  
    return render(request,"index-6.html")

