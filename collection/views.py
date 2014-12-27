from django.shortcuts import render, render_to_response


def index(request):
   # this is your new view
   return render_to_response('index.html')
