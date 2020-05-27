from django.shortcuts import render
from django.http import HttpResponse
from .models import Post 


def home(request):
	dummy = {
	'posts':Post.objects.all()
	}
	return render(request,"blog/home.html",dummy)

def about(request):
	return render(request,"blog/about.html")