from django.shortcuts import render


def index(request):
   # this is your new view
   return render(request, 'index.html')
